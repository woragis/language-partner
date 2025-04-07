from langchain.agents import Tool
from llms.gemini import get_gemini_summarizer

gemini_llm = get_gemini_summarizer()

gemini_search_tool = Tool(
    name="gemini_search",
    func=lambda q: gemini_llm.predict(q),
    description="Use this tool to search for information on the internet or answer factual queries."
)
