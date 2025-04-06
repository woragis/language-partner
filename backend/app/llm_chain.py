from langchain.llms import OpenAI

# You can switch out this class to route to different LLMs (Grok, Gemini, etc.)


class LLMWrapper:
    def __init__(self):
        self.llm = OpenAI(temperature=0.7)

    def generate(self, prompt: str) -> str:
        return self.llm(prompt)
