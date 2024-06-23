import speech_recognition as sr
import pyttsx3
import wikipediaapi

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
tts_engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen():
    """Listen for a voice command and convert it to text."""
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"Recognized: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return ""

def fetch_wikipedia_summary(query):
    """Fetch the summary from Wikipedia."""
    wiki = wikipediaapi.Wikipedia('en')
    page = wiki.page(query)
    if page.exists():
        return page.summary[:1000]  # Fetch the summary, limited to 1000 characters
    else:
        return "Sorry, I couldn't find any information on that topic."

def process_command(command):
    """Process the voice command and respond accordingly."""
    if 'wikipedia' in command:
        speak("Searching Wikipedia...")
        command = command.replace("wikipedia", "")
        result = fetch_wikipedia_summary(command.strip())
        speak(f"According to Wikipedia, {result}")
    elif 'hello' in command:
        speak("Hello! How can I help you today?")
    elif 'goodbye' in command:
        speak("Goodbye! Have a nice day.")
        exit()
    else:
        speak("I'm sorry, I can't help with that yet.")

def main():
    """Main function to run the voice assistant."""
    speak("How can I assist you today?")
    while True:
        command = listen()
        if command:
            process_command(command)

if __name__ == "__main__":
    main()
