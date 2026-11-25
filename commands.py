
import webbrowser
import subprocess


# WHY: Handle all commands given by the user.
def process_command(command, speak):

    # WHY: Respond to greetings.
    if "hello" in command:
        speak("Hello! How can I help you?")

    # WHY: Respond to the user's question.
    elif "how are you" in command:
        speak("I am doing great! Thank you for asking.")

    # WHY: Tell the user NewMe's name.
    elif "what is your name" in command:
        speak("My name is NewMe, your personal voice assistant.")

    # WHY: Open YouTube.
    elif "open youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open_new_tab("https://www.youtube.com")

    # WHY: Open Google.
    elif "open google" in command:
        speak("Opening Google.")
        webbrowser.open_new_tab("https://www.google.com")

    # WHY: Open Notepad.
    elif "open notepad" in command:
        speak("Opening Notepad.")
        subprocess.Popen("notepad.exe")

    # WHY: Open Calculator.
    elif "open calculator" in command:
        speak("Opening Calculator.")
        subprocess.Popen("calc.exe")

    # WHY: Exit NewMe.
    elif "bye" in command:
        speak("Goodbye! NewMe is shutting down.")
        return False

    # WHY: Handle unsupported commands.
    else:
        speak("Sorry, I don't know that command yet.")

    return True
