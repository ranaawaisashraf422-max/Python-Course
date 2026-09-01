import speech_recognition as sr  # libarary for reecognizing my speech
import webbrowser
import pyttsx3   #for text to speech
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os
recognizer = sr.Recognizer()  # Recognize our speech
engine = pyttsx3.init()
newsapi = "Your Api Key"


def speak_old(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def speak(text):
      tts = gTTS(text)
      tts.save('temp.mp3')



      # Initialize pygame mixer
      pygame.mixer.init()

      # Load the MP3 file
      pygame.mixer.music.load('temp.mp3')

      # Play the MP3 file
      pygame.mixer.music.play()

      # Keep the program running until the music stops playing
      while pygame.mixer.music.get_busy():
          pygame.time.Clock().tick(10)
      pygame.mixer.music.unload()
      os.remove("temp.mp3")



def aiprocess(command):
    client = OpenAI(api_key="Link of api_key",
    )
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}
    ]
)

    return completion.choices[0].message.content
#pip install openai
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
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")

        if r.status_code == 200:
              # Parse the JSON response
              data = r.json()

              # Extract the articles
              articles = data.get('articles', [])

              # Print the headlines
              for article in articles:
                    speak(article['title'])
    else:
          #Let open AI Handle the request
          output = aiprocess(c)
          speak(output)
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

