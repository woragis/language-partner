from langchain_google_genai import ChatGoogleGenerativeAI
from config.settings import GEMINI_API_KEY


def get_gemini_summarizer():
    return ChatGoogleGenerativeAI(api_key=GEMINI_API_KEY, model="gemini-1.5-flash-8b")


def get_gemini_audio_transcriber():
    return ChatGoogleGenerativeAI(api_key=GEMINI_API_KEY, model="gemini-1.5-flash")


def get_gemini_router():
    return ChatGoogleGenerativeAI(api_key=GEMINI_API_KEY, model="gemini-1.5-flash")
