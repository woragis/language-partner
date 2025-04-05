import openai
from gtts import gTTS
from os import getenv, _exit, system
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()


open_ai_key = getenv('OPEN_AI_KEY')


def print_key():
    print(f'Open AI KEY: {open_ai_key}')


def get_time() -> str:
    now = datetime.now()
    formated = now.strftime('%Y_%m_%d__%H_%M_%S__%f')
    return formated


def say():
    text = "こんにちは、元気ですか？"
    tts = gTTS(text=text, lang='ja')
    file = 'jpa.mp3'
    tts.save(file)
    system(f'mpg123 {file}')

    return


def main():

    if not open_ai_key:
        print('No api key')
        _exit(1)

    openai.api_key = open_ai_key

    response = openai.chat.completions.create(
        model='gpt-4o',
        messages=[
            {'role': 'system', 'content': 'You are a partner that helps a english speaker to learn english by talking to him in japanese'},
            {'role': 'system', 'content': 'The user can ask you to translate something, when he asks this, you respond in english explaining what you said, why you said, the context its used generally'},
            {'role': 'system',
                'content': 'You sometimes explain the grammar behind some phrases'},
            {'role': 'user', 'content': 'The user speaks english and is trying to learn japanese'},
            {'role': 'system', 'content': 'You don\'t know the user japanese level, so you need to find out based on his level of comprehension of what you say'},
        ]
    )

    print(response.choices[0].message)


def listen():
    import speech_recognition as sr

    # Create recognizer
    r = sr.Recognizer()

    # Use the microphone
    with sr.Microphone() as source:
        print("🎤 Say something...")
        # optional: calibrate to background noise
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 5
        audio = r.listen(source, timeout=10, phrase_time_limit=20)

    print("⏳ Transcribing...")

    try:
        # Use Google's speech recognition
        # "en-US" for English, "ja-JP" for Japanese
        # text = r.recognize_google(audio, language="ja-JP")
        text = r.recognize_google(audio, language="en-US")
        print("📝 You said:", text)
    except sr.UnknownValueError:
        print("❌ Could not understand audio")
    except sr.RequestError as e:
        print(f"🔌 Could not request results; {e}")


def get_files():
    file_history = []
    for i in range(5):
        file = f'{get_time()}.mp3'
        file_history.append(file)
    for i in file_history:
        print(i)
    return file_history


if __name__ == '__main__':
    # main()
    # print_key()
    # say()
    listen()
