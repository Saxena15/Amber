import os

import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os

# import chrome
import pyaudio

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)


def wishme():
    hr = int(datetime.datetime.now().hour)
    if hr >= 0 and hr < 12:
        speakAudio("Good Morning!")

    elif hr >= 12 and hr < 18:
        speakAudio("Good Afternoon!")

    else:
        speakAudio("Good Evening!")

    speakAudio("I am Amber Sir. Please tell me how may I help you")


def speakAudio(audio):
    engine.say(audio);
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-au')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")  # Say that again will be printed in case of improper voice
        return "None"  # None string will be returned
    return query


if __name__ == "__main__":
    wishme()

    # query = takeCommand().lower()
    # if "amber" in query:

    while True:
        query = takeCommand().lower()

        if 'time' in query:
            speakAudio('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speakAudio("According to Wikipedia")
            print(results)
            speakAudio(results)

        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        elif 'google' in query:
            webbrowser.open("google.com")

        elif 'wikipedia' in query:
            webbrowser.open("wikipedia.com")


        elif 'time' in query:

            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speakAudio(f"Sir, the time is {strTime}")

        elif 'Android studio' in query:
            path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Android Studio\\bin\\studio64.exe"
            os.startfile(path)
        # elif 'Spotify' in query:
        #     session = spotify.Session()

        elif 'python development ide' in query:
            path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1\\bin\\pycharm64.exe"
            os.startfile(path)
        elif 'telegram' in query:
            path = "E:\\Telegram Desktop\\Telegram"
            os.startfile(path)

        elif 'see ya' in query:
            speakAudio(" bye sir")

            break

        else:
            speakAudio("mehhhh")

    else:

        pass
