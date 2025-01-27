import os
from flask import Flask, render_template, request, jsonify
from langchain.chains import LLMChain
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.messages import SystemMessage
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq
from frt_processing import process_frt, live_frt
from video_upload import upload_video

app = Flask(__name__)

# Get Groq API key
groq_api_key = os.environ.get("API", "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")
model = 'llama3-8b-8192'

# Initialize Groq Langchain chat object and conversation
groq_chat = ChatGroq(
        groq_api_key=groq_api_key, 
        model_name=model
)

system_prompt = '''You are tasked with performing the FRT (Functional Rating Test). Follow these steps to gather and validate information from the user:

Personal Details:
Ask for the following details one by one:
What is your name?
What is your age?
What is your gender?
What is your weight (kg)?
What is your marital status?

Presenting Complaints:
Ask each question one by one. If the user answers “yes,” ask for the duration in days.
Do you have memory problems, particularly remembering recent events? If yes, mention the duration.
Do you have increasing confusion? If yes, mention the duration.
Do you have reduced concentration? If yes, mention the duration.
Do you have behavior changes? If yes, mention the duration.
Do you have withdrawal? If yes, mention the duration.
Do you have loss of ability to do everyday tasks? If yes, mention the duration.

History of Presenting Illness:
Ask the following questions one by one:
What is the onset of your symptoms? (Sudden or Gradual)
What factors aggravate the above symptoms?
What factors relieve the symptoms?
Any other associated factors? (e.g., diarrhea, constipation, digestion problems)

Evaluation Scale:
Validate the duration of symptoms against the following criteria:
Memory problems: more than 2 days
Increasing confusion: more than 5 days
Reduced concentration: more than 6 days
Behavior changes: more than 7 days
Withdrawal: more than 8 days
Loss of ability to do everyday tasks: more than 10 days

Conclusion:
If any of the symptoms meet or exceed the specified duration, respond with: “Proceed with the FRT.”
If none of the symptoms meet the criteria, respond with: “There is no need to do the FRT.”'''  # Same system_prompt as before

conversational_memory_length = 20  # number of previous messages the chatbot will remember during the conversation
memory = ConversationBufferWindowMemory(k=conversational_memory_length, memory_key="chat_history", return_messages=True)


UPLOAD_DIR = 'uploads'
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    user_question = request.json.get('question')
    
    if user_question:
        # Construct a chat prompt template using various components
        prompt = ChatPromptTemplate.from_messages(
            [
                SystemMessage(content=system_prompt),
                MessagesPlaceholder(variable_name="chat_history"),
                HumanMessagePromptTemplate.from_template("{human_input}")
            ]
        )

        # Create a conversation chain
        conversation = LLMChain(
            llm=groq_chat,
            prompt=prompt,
            verbose=False,
            memory=memory,
        )

        response = conversation.predict(human_input=user_question)
        # Initialize the variable to store the FRT recommendation status
        frt_recommended = 0


        # Check if the exact phrase is in the response
        if "Proceed with the FRT" in response:
            frt_recommended = 1
        elif "proceed with the FRT" in response:
            frt_recommended = 1
        elif "proceeding with the FRT" in response:
            frt_recommended = 1

        print("This is the FRT:")
        print(frt_recommended)

        return jsonify({"answer": response, "frt_recommended": frt_recommended})

    return jsonify({"answer": "Sorry, I didn't understand that."})

@app.route('/upload', methods=['POST'])
def upload():
    if 'video' not in request.files:
        return jsonify({'error': 'No video file provided'}), 400

    video_file = request.files['video']
    if video_file:
        filename, error = upload_video(video_file)
        if error:
            return jsonify({'error': error}), 400
        
        video_path = os.path.join(UPLOAD_DIR, filename)
        result = process_frt(video_path)
        print(result)
        return jsonify({'filename': filename, 'result': result}), 200

    return jsonify({'error': 'File upload failed'}), 500

@app.route('/live_frt', methods=['GET'])
def live_frt_route():
    result = live_frt()
    return jsonify({'result': result})

if __name__ == "__main__":
    app.run(debug=True)
