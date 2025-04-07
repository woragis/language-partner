import openai
from gtts import gTTS
from os import getenv, _exit, system
from dotenv import load_dotenv
from datetime import datetime
import pyaudio

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


def record_audio():
    import pyaudio
    import wave
    import time

    CHUNK = 1024
    FORMAT = pyaudio.paInt16  # Change to 16-bit integer for WAV compatibility
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 15  # Record for 5 seconds

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Recording...")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Finished recording.")

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save to WAV file
    wf = wave.open("output.mp3", 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    print("Audio saved as output.mp3")


def playback_audio():
    p = pyaudio.PyAudio()
    FORMAT = pyaudio.paFloat32
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    input_stream = p.open(format=FORMAT, channels=CHANNELS,
                          input=True, rate=RATE, frames_per_buffer=CHUNK)
    output_stream = p.open(format=FORMAT, channels=CHANNELS,
                           output=True, rate=RATE, frames_per_buffer=CHUNK)
    print('listening to your microfone and playing back... press ctrl+c to stop')
    try:
        while True:
            data = input_stream.read(CHUNK)
            output_stream.write(data)
    except KeyboardInterrupt:
        print('stopping...')
    finally:
        input_stream.stop_stream()
        input_stream.close()
        output_stream.stop_stream()
        output_stream.close()
        p.terminate()


def whisper_audio_transcribe():
    import whisper

    model = whisper.load_model('small')  # or 'base', 'medium', 'large', etc.

    result = model.transcribe('output.mp3')

    print('Detected language:', result['language'])
    print('Transcription:', result['text'])

    return


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
    # listen()
    # playback_audio()
    # record_audio()
    whisper_audio_transcribe()
