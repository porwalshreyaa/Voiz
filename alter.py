import os
import speech_recognition as sr

recognizer = sr.Recognizer()

def take_command():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language="en-in")
        return command.lower()
    except sr.UnknownValueError:
        return "unknown"
    except sr.RequestError as e:
        print(f"Error connecting to the Google API: {e}")
        return "error"

if __name__ == '__main__':
    print("Listening for your wake word...")
    while True:
        command = take_command()
        
        # Check if the wake word is detected
        if "dooba dooba" in command:
            print("Wake word detected. Listening for a command...")
            while True:
                command = take_command()
                if command == "unknown":
                    print("Sorry, I couldn't understand what you said.")
                elif command == "error":
                    print("Error connecting to the Google API.")
                elif "stop listening" in command:
                    print("Stopping listening.")
                    break
                else:
                    # Handle specific commands here
                    print(f"Command received: {command}")
