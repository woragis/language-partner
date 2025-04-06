from langchain_google_genai import ChatGoogleGenerativeAI
from config.settings import GEMINI_API_KEY


def get_gemini():
    return ChatGoogleGenerativeAI(api_key=GEMINI_API_KEY, model="gemini-pro")
