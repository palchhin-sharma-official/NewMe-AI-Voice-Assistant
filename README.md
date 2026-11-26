# NewMe – AI Voice Assistant

NewMe is a Python-based voice assistant that listens to voice commands and performs basic tasks such as opening websites and launching desktop applications.


## Features

- Voice recognition
- Text-to-speech responses
- Greeting and conversational commands
- Open Google
- Open YouTube
- Launch Notepad
- Launch Calculator
- Exit using a voice command


## Technologies Used

- Python
- SpeechRecognition
- pyttsx3
- PyAudio
- Webbrowser
- Subprocess


## Project Structure

AI-Voice-Assistant/

│

├── venv/

├── main.py

├── commands.py

├── requirements.txt

├── README.md

└── .gitignore


## Installation

**1. Clone the repository**
git clone https://github.com/palchhin-sharma-official/NewMe-AI-Voice-Assistant.git

**2. Navigate to the project folder**
cd AI-Voice-Assistant

**3. Create a virtual environment**
python -m venv venv

**4. Activate the virtual environment (Windows PowerShell)**
.\venv\Scripts\Activate.ps1

**5. Install dependencies**
pip install -r requirements.txt


## How to Run

Execute the following command:

python main.py

Speak clearly into your microphone to give NewMe a command.


## Requirements

- Python 3.12 or compatible version
- Working microphone
- Internet connection for Google speech recognition


## Note

NewMe uses Google's speech recognition service through the SpeechRecognition library. An internet connection is required for voice recognition.


## Author

Created as a Python learning and development project.
