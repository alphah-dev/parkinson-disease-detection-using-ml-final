# Parkinson's Disease Detection Using AI

This project is a fully-fledged, interactive, and informative website designed to detect Parkinson's disease using machine learning (ML), educate users about the condition, and provide therapy tools to improve motor skills. The website features a modern dark-themed design with animations, a user-friendly login system, ML-based detection with 22 parameters, and engaging interactive elements.

## Overview

- **Purpose:** Early detection of Parkinson's disease using ML and support through therapy exercises.
- **Features:**
  - Login page with age and observation questions (e.g., tremors, slowness).
  - ML detection tool supporting manual input or Excel file uploads (22 parameters like MDVP:Fo(Hz), Shimmer).
  - Therapy section with Photo Gallery, Drawing Exercises, Big Write, Calibration Test, and Progress Tracking.
  - Educational content on causes, treatments, and living with Parkinson's.
  - Additional features: Chatbot, Community Forum, Gamification, Voice Assistant.
- **Design:** Dark theme (deep blues, blacks, teal accents), GSAP animations (fade-ins, hover effects), Roboto/Montserrat fonts, responsive layout.
- **Technologies:** React.js (frontend), Flask (backend), SQLite (database), GSAP (animations).

## Project Structure
 
PARKINSON_DISEASE_DETECTION_USING_AI/ ├── static/ # Static files (CSS, JS, images) │ ├── telemonitoring/ # Telemonitoring data │ ├── parkinsons_updrs.data # UPDRS data │ └── parkinsons_updrs.names # UPDRS names ├── templates/ # HTML templates │ ├── index.html # Main HTML file │ └── venv/ # Virtual environment ├── .gitignore # Git ignore file ├── app.py # Flask backend application ├── data_script.py # Data processing script ├── Parkinson_model.pkl # Trained ML model ├── parkinsons.data # Parkinson’s dataset ├── parkinsons.names # Dataset names ├── parkinsons.zip # Zipped dataset ├── Praat.exe # Praat executable ├── README.md # Project documentation ├── requirements.txt # Python dependencies ├── scaler.pkl # Data scaler ├── test_data.py # Test data script ├── test_data.xlsx # Test Excel data ├── test_data1.xlsx # Additional test data ├── test_data2.xlsx # Additional test data └── updated_voice_report.xlsx # Updated voice report
text
Copy

## Prerequisites

- **Python 3.8+**
- **Node.js 14+**
- **npm**
- **Git**

## Installation

### Backend Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/parkinsons-detection.git
   cd PARKINSON_DISEASE_DETECTION_USING_AI
2.	Set Up Virtual Environment: 
bash
Copy
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3.	Install Dependencies: 
bash
Copy
pip install -r requirements.txt
4.	Run the Backend: 
bash
Copy
python app.py
The backend will run on http://localhost:5000.
Frontend Setup
1.	Navigate to Frontend Directory: 
bash
Copy
cd frontend
2.	Install Dependencies: 
bash
Copy
npm install
3.	Run the Frontend: 
bash
Copy
npm start
The frontend will run on http://localhost:3000.
Usage
1.	Access the Website: 
o	Open http://localhost:3000 in your browser.
o	Click "Get Started" to navigate to the login page.
2.	Login/Sign Up: 
o	Enter username and password to log in.
o	Use "Sign Up" to create an account, providing age and answering observation questions (e.g., "Do you have tremors?").
3.	Detection: 
o	Go to the Detection section.
o	Choose "Manual Input" to enter 22 ML parameters or "Upload File" to upload an Excel file.
o	Click "Predict" to see results (e.g., "95% Accuracy: High Risk") with a loading animation.
4.	Therapy: 
o	Explore tools like Photo Gallery, Drawing Exercises, Big Write, and Calibration Test.
o	Track progress with the analytics dashboard.
5.	Education: 
o	Read about Parkinson’s causes, treatments, and living tips in collapsible sections.
o	Take the quiz for interactive learning.
6.	Additional Features: 
o	Use the chatbot (bottom-right icon) for support.
o	Join the Community Forum to connect with others.
o	Earn badges via gamification.
o	Use voice commands with the Voice Assistant.
ML Model
•	Training Data: parkinsons.data, processed via data_script.py.
•	Model: Parkinson_model.pkl (trained with 22 parameters).
•	Prediction: API endpoint /predict handles input and returns accuracy/risk.
Contributing
1.	Fork the repository.
2.	Create a new branch: git checkout -b feature-branch.
3.	Commit changes: git commit -m "Description".
4.	Push to the branch: git push origin feature-branch.
5.	Submit a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.
Disclaimer
This tool is for screening purposes only and should not be used as a substitute for professional medical advice.
Contact
For issues or questions, contact HARSH KATIYAR  at katiyarh76@gmail.com .

