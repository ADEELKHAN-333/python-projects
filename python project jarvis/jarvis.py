import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary

# pip install pocketsphinex

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        if song in musiclibrary.music:  
            link = musiclibrary.music[song]
            webbrowser.open(link)
        else:
            speak(f"Sorry, I couldn't find the song {song}.")
    elif "quit" in c.lower():
        speak("Goodbye!")
        return False 
    

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for the wake word 'Jarvis'...")
                audio = recognizer.listen(source, timeout=1, phrase_time_limit=1)
                word = recognizer.recognize_google(audio)
                
            if word.lower() == "jarvis":
                speak("Yes?")
                
                with sr.Microphone() as source:
                    print("Jarvis Active... Listening for command.")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    
                    
                    if not processCommand(command):
                        break

        except sr.UnknownValueError:
            print("Sorry, I did not understand that. Please try again.")
            speak("Sorry, I did not understand that. Please try again.")
         
        except sr.WaitTimeoutError:
            print("Listening timed out. Please try again.")

        except sr.RequestError as e:
            print(f"API error: {e}")

