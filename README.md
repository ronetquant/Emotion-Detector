# Emotion-Detector
coursera
# Emotion Detector

## Project Description
This is a web-based application developed as part of a software engineering project. The application utilizes a **Watson NLP library** via an API to perform emotion detection on user-provided text. The system analyzes the input and returns scores for **anger, disgust, fear, joy, and sadness**, while also identifying the **dominant emotion**.

## Features
* **AI-Powered Analysis:** Integrates IBM Watson NLP for high-accuracy emotion prediction.
* **RESTful API:** Built with Flask to handle web requests.
* **Error Handling:** Robustly manages blank or invalid user inputs.
* **Unit Tested:** Includes a suite of tests to ensure logic accuracy.
* **Static Code Analysis:** Score of 10/10 on PyLint for PEP 8 compliance.

## Project Structure
- `EmotionDetection/`: Logic package for the emotion analysis.
- `server.py`: The main Flask application.
- `test_emotion_detection.py`: Unit testing script.
- `static/` & `templates/`: Frontend files for the web interface.

## How to Run
1. Clone the repository.
2. Ensure you have the `requests` and `flask` libraries installed:
   ```bash
   pip install requests flask
