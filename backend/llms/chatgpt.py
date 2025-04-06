from langchain.llms.openai import OpenAI
from config.settings import OPENAI_API_KEY


def get_chatgpt():
    return OpenAI(api_key=OPENAI_API_KEY, temperature=0.7)
