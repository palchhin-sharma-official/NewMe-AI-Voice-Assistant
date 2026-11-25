
import pyttsx3
import speech_recognition as sr

# WHY: Import the command-processing function from commands.py.
from commands import process_command


# WHY: Initialize the text-to-speech engine.
engine = pyttsx3.init()

# WHY: Create an object for speech recognition.
recognizer = sr.Recognizer()


# WHY: Configure NewMe's voice.
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)


# WHY: Convert text into spoken audio.
def speak(text):
    engine.say(text)
    engine.runAndWait()


# WHY: Capture and recognize the user's voice.
def listen():

    with sr.Microphone() as source:
        print("NewMe is listening...")

        # WHY: Reduce background noise.
        recognizer.adjust_for_ambient_noise(source, duration=1)

        # WHY: Capture audio from the microphone.
        audio = recognizer.listen(source)

    try:
        # WHY: Convert recorded audio into text.
        command = recognizer.recognize_google(audio)

        print("You said:", command)

        return command.lower()

    except sr.UnknownValueError:
        print("Could not understand your voice.")
        return ""

    except sr.RequestError:
        print("Speech recognition service error.")
        return ""


# WHY: Welcome the user when NewMe starts.
speak("Hello! I am NewMe. How can I help you?")


# WHY: Keep NewMe running until the user exits.
running = True

while running:

    # WHY: Listen for the user's command.
    user_command = listen()

    # WHY: Process only successfully recognized commands.
    if user_command:
        running = process_command(user_command, speak)
