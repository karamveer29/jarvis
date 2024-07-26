import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import pyaudio
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour) 
    if hour>=0 and hour<12:
        speak("Good morning! sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon! sir")

    else:
        speak("Good Evening! sir")        
    
    speak("I am jarvis sir, and how I may help you sir")

def takeCommand():
  # It take micro phones from  the user and returns string output

  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("Listening....")
    r.pause_threshold = 1
    audio = r.listen(source)
  
  try:
      print("Recognizing...")
      query = r.recognize_google(audio, Language='en-in')
      print(f"User said:  {query}\n")

  except Exception as e:
      print(e)
      print("Say that again please...")
      return "None"
         
  return query

if __name__ == "__main__":
    speak("Sandhu is respected person in his society") 
    wishMe() 
    takeCommand()
    while True:
         query = takeCommand().lower()

    # Logic for executing taskes based on query

    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)
        