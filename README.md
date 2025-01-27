# Generative AI for Automated Functional Reach Test (FRT)

## Overview
This project leverages **Generative AI** and **Computer Vision** to automate cognitive health assessments, particularly focusing on the Functional Reach Test (FRT). The goal is to provide accessible, efficient, and reliable tools for assessing balance and fall risk using widely available technologies like smartphones, tablets, and webcams.

---

## Features

1. **Cognitive Health Assessment**:
   - User-friendly interface for self-assessment.
   - AI-driven evaluation to determine the need for FRT.

2. **Functional Reach Test (FRT)**:
   - Option to perform FRT via video upload or live using a device camera.
   - Real-time feedback and recommendations.

3. **Advanced AI Models**:
   - Analyze cognitive health and balance indicators.
   - Provide recommendations for medical consultation when necessary.

4. **Accessibility**:
   - Designed for remote and underserved areas.
   - Eliminates the need for specialized equipment.

---

## Methodology

1. **Data Collection**:
   - User-provided data (age, symptoms, standardized cognitive assessments).
   - Video analysis for FRT performance.

2. **System Design**:
   - Intuitive graphical user interface.
   - AI models for in-context learning and analysis.
   - Recommendation engine to provide actionable insights.

3. **Implementation**:
   - Backend: Flask.
   - AI Models: TensorFlow, PyTorch.
   - Computer Vision: OpenCV, MediaPipe.

4. **Evaluation**:
   - Metrics: Accuracy, usability, reliability.
   - Validation: Clinical comparisons, user feedback.

---

## Tools and Technologies

### Software
- **Programming Languages**: Python, JavaScript.
- **Libraries**: TensorFlow, PyTorch, OpenCV, MediaPipe.
- **Frameworks**: Flask.

### Hardware
- Devices with cameras (smartphones, tablets, webcams).
- Modern desktops or laptops (8GB+ RAM).

---

## Challenges and Solutions

### Challenges
- Ensuring accurate in-context learning prompts.
- Measuring real-time distances from camera input.
- Safeguarding user privacy.

### Solutions
- Optimized prompts for AI models.
- Hard-coded calibration for distance measurement.
- Robust data security and privacy measures.

---

## Future Enhancements

- Integration of additional assessments for comprehensive evaluations.
- Improved computer vision models for greater accuracy.
- Personalized user experiences based on profiles and preferences.

---

## How to Use

1. **Setup**:
   - Install required libraries and frameworks (see dependencies).
   - Deploy the backend and frontend applications.

2. **Perform Assessments**:
   - Register and provide basic details.
   - Follow instructions for the cognitive health assessment.
   - Conduct the FRT either via live feed or video upload.

3. **Get Results**:
   - Receive real-time feedback on cognitive health and fall risk.
   - Access personalized recommendations.

---

## References
- Duncan, P. W. et al. (1990). *Functional Reach: A New Clinical Measure of Balance.*
- Esteva, A. et al. (2019). *A Guide to Deep Learning in Healthcare.*
- Topol, E. J. (2019). *High-Performance Medicine: The Convergence of Human and Artificial Intelligence.*

For a full list of references, refer to the report.

---

## License
This project is licensed under the [MIT License](LICENSE).
