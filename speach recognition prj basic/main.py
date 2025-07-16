import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary


# from openai import OpenAI
# import os



# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# def ask_chatgpt(prompt):
#     try:
#         response = client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "user", "content": prompt}
#             ]
#         )
#         return response.choices[0].message.content.strip()
#     except Exception as e:
#         return f"ChatGPT Error: {e}"




recogniser = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print("Speaking:", text)
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open" in c.lower():
        c = c.replace("open", "")
        c = c.strip()
        speak("Opening " + c)
        webbrowser.open("https://" + c + ".com")
    
    elif "play" in c.lower():
        song = c.lower().replace("play", "").strip()
        print(f"Requested song: {song}")

        if song in musiclibrary.music:
            link = musiclibrary.music[song]
            speak(f"Playing {song}")
            webbrowser.open(link)
        else:
            speak("Sorry, I couldn't find that song.")


        #open ai handel
  

if __name__ == "__main__":
    speak("Initializing Jarvis")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recogniser.listen(source, timeout=4)
                word = recogniser.recognize_google(audio)
                print(f"Heard: {word}")

                if word.strip().lower() == "jarvis":
                    speak("Yes")

                    with sr.Microphone() as source:
                        print("Jarvis activated, listening for command...")
                        audio = recogniser.listen(source, timeout=4)
                        command = recogniser.recognize_google(audio)
                        print(f"Heard command: {command}")
                        processCommand(command)

        except Exception as e:
            print(f"Error: {e}")

    