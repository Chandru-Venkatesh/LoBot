# LoBot - A Multi-functional Voice Assistant

LoBot is a voice-activated assistant created by Jayachandran to assist with information retrieval, web searches, voice-based tasks, and more. The bot utilizes various technologies such as speech recognition, text-to-speech, Wikipedia querying, Hugging Face chatbot, and YouTube video playback.

## Features

- **Speech Recognition**: LoBot listens to your voice commands and converts them into text for further processing.
- **Text-to-Speech**: LoBot responds with speech, making it an interactive assistant.
- **Wikipedia Information**: LoBot can fetch summaries from Wikipedia based on user queries.
- **Hugging Face Chatbot**: Chat with LoBot to get answers and engage in conversations.
- **YouTube Video Playback**: LoBot can play videos from YouTube based on user input.
- **Shutdown Command**: LoBot can shut down your system when requested.

## Requirements

- Python 3.x
- `pyttsx3` library for text-to-speech.
- `speech_recognition` library for speech-to-text functionality.
- `pywhatkit` library for YouTube search and video playback.
- `hugchat` for interacting with the Hugging Face chatbot API.
- `wikipedia` for fetching Wikipedia summaries.
- Operating system should support `os.system('shutdown')`.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/lobot.git
    cd lobot
    ```

2. Install the required Python libraries:

    ```bash
    pip install pyttsx3 speechrecognition pywhatkit hugchat wikipedia
    ```

3. Set up Hugging Face API credentials (if required) and provide them in the script.

4. Run the script:

    ```bash
    python lobot.py
    ```

## Usage

Once the script is running, you can interact with LoBot using your voice. Here are some example commands:

- "Tell me about [Topic]" – Fetches a summary from Wikipedia.
- "Play [Song] on YouTube" – Plays a video on YouTube.
- "Tell me about yourself" – LoBot will introduce itself.
- "Thanks for helping" – Ends the conversation.



