import speech_recognition as sr  # libarary for reecognizing my speech
import webbrowser
import pyttsx3   #for text to speech
import musicLibrary
recognizer = sr.Recognizer()  # Recognize our speech
engine = pyttsx3.init()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
            webbrowser.open("https://youtube.com")

    elif "open facebook" in c.lower():
            webbrowser.open("https://facebook.com")

    elif "open instagram" in c.lower():
            webbrowser.open("https://instagram.com")

    elif "open whatsapp" in c.lower():
            webbrowser.open("https://web.whatsapp.com")

    elif "open github" in c.lower():
            webbrowser.open("https://github.com")

    elif "open gmail" in c.lower():
            webbrowser.open("https://gmail.com")

    elif "open chatgpt" in c.lower():
            webbrowser.open("https://chatgpt.com")

    elif "open spotify" in c.lower():
            webbrowser.open("https://open.spotify.com")

    elif "open linkedin" in c.lower():
            webbrowser.open("https://linkedin.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)


if __name__== "__main__":
    speak("Initializing Jarvis...........?")

    while True:
        #Listen for the wake word Jarvis
        # obtain audio from the microphone
        r = sr.Recognizer()

        print("recognizing....")
   
        try:
            with sr.Microphone() as source:
                print("Listening.....")           
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word = r.recognize_google(audio)
            if (word.lower()== "jarvis"): 
                speak("Ya")
                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active.......")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)




        except Exception as e:
            print("Error; {0}".format(e))

