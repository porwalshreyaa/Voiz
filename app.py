"module imported to know time, create engine, set username and botname"
import os
from datetime import datetime
from decouple import config
import speech_recognition as sr
import webbrowser

USERNAME = config('USER')
BOTNAME = config('BOTNAME')
SECRETKEY = config('SECRETKEY')


# Initialize the recognizer
recognizer = sr.Recognizer()



def say(text):
    """Says text you pass through it"""
    os.system(f"espeak -s 150 -p 50 '{text}'")

def take_command():
    """Takes command in the form of audio"""
    with sr.Microphone() as source:
        # Use the microphone as the source
        print("Listening... Say something.")
        recognizer.adjust_for_ambient_noise(source)   # Adjust for noise
        audio = recognizer.listen(source) 
        query = recognizer.recognize_google(audio, language="hi-in")
        print(f"{USERNAME} said: {query}")
        if "stop listening" in query.lower():

            print("Stopping listening.")
            say("Ab mai Jata hu!")
            exit()
        try:
            # Recognize the speech
            text = recognizer.recognize_google(audio)
            # print("You said:", text)
            print(f"{USERNAME} said: {query}")
            say(f"Aapne kaha, {query}")
            return text
        except sr.UnknownValueError as e:
            error = "Mujhe samjh nahi aayaa"
            say(error, e)
        except sr.RequestError as e:
            print(f"Sorry, there was an error connecting to the Google API: {e}")
            say(f"Sorry, there was an error connecting to the Google API: {e}")
        finally:
            say("Ab mai Jata hu!")
            exit()
            
        # except sr.UnknownValueError:
        #     print("Sorry, I couldn't understand what you said.")
        # except sr.RequestError as e:
        #     print(f"Sorry, there was an error connecting to the Google API: {e}")


if __name__ == '__main__':
    print("Vscode")
    say("Namasthey, I am Dooba-Dooba.")
    while True:
        command = take_command()
        sites = [["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],["google", "https://www.google.com"]]
        # add more sites :)
        # add search functionallity
    
        for site in sites:
            if f"Search".lower() in command.lower():
                command = command.lower().replace("dooba", "")
                command = command.lower().replace("search", "")
                command = command.lower().replace("-", "")
                lcommand = command.split()
                sear_q = ""
                for i in lcommand:
                    sear_q += i+"+"
                say("Searching Shreya...")
                webbrowser.open(f"https://www.google.com/search?q={sear_q}")
            elif f"Open {site[0]}".lower() in command.lower():
                say(f"Opening {site[0]} Shreya...")
                webbrowser.open(site[1])
            else:
                say("Your welcome, Shreya!")
                say("Ab mai Jata hu!")
                exit()


# def greet_user():
#     """Greets the user according to the time"""
#     hour = datetime.now().hour
#     if (hour >= 6) and (hour < 12):
#         speak(f"Good Morning {USERNAME}")
#     elif (hour >= 12) and (hour < 16):
#         speak(f"Good afternoon {USERNAME}")
#     elif (hour >= 16) and (hour < 19):
#         speak(f"Good Evening {USERNAME}")
#     else:
#         speak(f"Namaste! {USERNAME}")
#     speak(f"I am {BOTNAME}. How may I assist you?")


