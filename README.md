# Parkinson's Disease Detection Using AI

# refer to this video for complete implementation :- https://youtu.be/1Z0WeU_kDLs?si=9tIEEA0SuJEb54-3
**LinkedIn :- https://www.linkedin.com/in/harsh-katiyar-46682625b/**

This project is an interactive web application aimed at detecting Parkinson's Disease using machine learning (ML), providing therapy tools, and educating users about the condition. It combines a user-friendly interface with a robust backend to assist in early screening and support.

## Overview

**Purpose:**  
To facilitate early detection of Parkinson's Disease through ML, and provide supportive tools for therapy and learning.

**Key Features:**

- User authentication with age and observation-based inputs.
- ML-based detection using 22 biomedical voice and movement parameters.
- Option for manual input or uploading Excel files for predictions.
- Therapy section including drawing exercises, photo gallery, calibration tests, and progress tracking.
- Educational content covering causes, treatments, and lifestyle tips.
- Additional features such as chatbot support, a community forum, gamification elements, and a voice assistant.

**Design:**  
Dark-themed UI with deep blue and teal accents, animated transitions using GSAP, and responsive layouts using Roboto and Montserrat fonts.

**Technology Stack:**

- **Frontend:** React.js
- **Backend:** Flask (Python)
- **Database:** SQLite
- **Animations:** GSAP

## Project Structure
PARKINSON_DISEASE_DETECTION_USING_AI/ ├── static/ ├── templates/ ├── telemonitoring/ ├── uploads/ ├── venv/ ├── app.py ├── data_script.py ├── Parkinson_model.pkl ├── scaler.pkl ├── test_data.py ├── *.xlsx (Test Data Files) ├── parkinsons.data ├── parkinsons.names ├── Praat.exe (Optional) ├── requirements.txt └── README.md

## Prerequisites

- Python 3.8+
- Node.js 14+
- npm
- Git

## Installation

### Backend Setup

```bash
git clone https://github.com/your-username/parkinsons-detection.git
cd PARKINSON_DISEASE_DETECTION_USING_AI

python -m venv venv
venv\Scripts\activate  # For Windows
# or
source venv/bin/activate  # For macOS/Linux

pip install -r requirements.txt
python app.py
# Backend runs at http://localhost:5000
Usage
1.	Open http://localhost:3000 in your browser.
2.	Use the login/signup page to authenticate. Users are required to enter age and answer observation-based questions.
3.	Navigate to the Detection section. Choose between manual input of 22 parameters or upload a test Excel file.
4.	Click "Predict" to view prediction results.
5.	Explore the Therapy section to access writing/drawing tools and track progress.
6.	Read informative content and take quizzes in the Education section.
7.	Access the chatbot, community forum, and voice assistant via the dashboard.
Machine Learning Model
•	Training Dataset: parkinsons.data (processed via data_script.py)
•	Model: Parkinson_model.pkl
•	Scaler: scaler.pkl
•	Endpoint: /predict (Flask API for prediction)
Contributing
1.	Fork this repository.
2.	Create a new branch: git checkout -b feature-branch
3.	Make your changes and commit: git commit -m "Add new feature"
4.	Push the branch: git push origin feature-branch
5.	Open a pull request for review.
License
This project is licensed under the MIT License. See the LICENSE file for details.
Disclaimer
This tool is for screening and educational purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment.
Contact
For any issues or questions, please contact:

Harsh Katiyar
katiyarh76@gmail.com
contact
