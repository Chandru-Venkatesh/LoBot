import wikipedia
import pyttsx3
from hugchat import hugchat
from hugchat.login import Login
import speech_recognition as sr
import pywhatkit

def initialize_text_to_speech():
    engine = pyttsx3.init()
    engine.setProperty('rate', '150')
    return engine

def say(text, engine):
    engine.say(text)
    engine.runAndWait()

def say_and_print(text, engine):
    print("LoBot:", text)
    say(text, engine)

def get_user_input(recognizer):
    while True:
        with sr.Microphone() as source:
            print("Say something:")
            audio = recognizer.listen(source)

        try:
            user_input = recognizer.recognize_google(audio)
            print("You said:", user_input)
            return user_input
        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio. Please try again.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}. Please try again.")

def chat_wikipedia(query, num_sentences=2):
    try:
        result = wikipedia.summary(query, sentences=num_sentences)
        if result:
            say_and_print(result, text_to_speech_engine)
    except wikipedia.exceptions.DisambiguationError as e:
        error_message = "I'm sorry, there was a disambiguation error. Please provide more details."
        print("Disambiguation Error:", e)
        say_and_print(error_message, text_to_speech_engine)
    except wikipedia.exceptions.HTTPTimeoutError as e:
        error_message = "I'm sorry, there was an HTTP timeout error. Please try again later."
        print("HTTP Timeout Error:", e)
        say_and_print(error_message, text_to_speech_engine)
    except wikipedia.exceptions.PageError as e:
        error_message = "I couldn't find any information on that topic."
        print("Page Error:", e)
        say_and_print(error_message, text_to_speech_engine)

def chat_huggingface(query, chatbot):
    # Send user input to the chatbot and get the response
    response = chatbot.chat(query)

    # Print and speak the response
    print(f"LoBot: {response}")
    say(response, text_to_speech_engine)

def play_on_youtube(query):
    pywhatkit.playonyt(query)
    
import os

def shutdown_computer():
    if os.name == 'posix': # for Linux and macOS
        os.system('sudo shutdown -h now')
    elif os.name == 'nt': # for Windows
        os.system('shutdown /s /t 1')
    else:
        print("Unsupported operating system")

    
    

shutdown_computer()


if __name__ == "__main__":
    # Initialize Hugging Face chatbot
    sign = Login("Jayachandran", "Kausi@2007")
    cookies = sign.login()
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

    # Initialize text-to-speech engine
    text_to_speech_engine = initialize_text_to_speech()

    # Initialize speech recognition
    recognizer = sr.Recognizer()

    while True:
        user_input = get_user_input(recognizer)

        if user_input.lower() == 'thanks for helping':
            response = "You're welcome! If you have more questions or need assistance, feel free to ask. I'm here to help."
            say_and_print(response, text_to_speech_engine)
            break

        if user_input.lower() == 'tell me about yourself':
            response = "I am LoBot, designed by Jayachandran. I'm here to help with information, answer questions, and assist you in various tasks. Feel free to ask anything!"
            say_and_print(response, text_to_speech_engine)
        elif user_input.lower().startswith('tell me about'):
            # Perform Wikipedia search
            query = user_input.lower().replace("tell me about", "").strip()
            chat_wikipedia(query)
        elif "play" in user_input.lower() and ("on youtube" in user_input.lower() or "video on youtube" in user_input.lower()):
            # Extracting the query from the user input
            query_start_index = user_input.lower().find("play") + len("play")
            query_end_index = user_input.lower().find("on youtube") if "on youtube" in user_input.lower() else user_input.lower().find("video on youtube")
            query = user_input[query_start_index:query_end_index].strip()
            play_on_youtube(query)
        else:
            chat_huggingface(user_input, chatbot)
