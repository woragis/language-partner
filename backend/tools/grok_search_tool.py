from langchain.agents import Tool
from llms.grok import GrokSearchLLM

grok_llm = GrokSearchLLM()

grok_tool = Tool(
    name="grok_search",
    func=lambda q: grok_llm.predict(q),
    description="Useful for internet searches"
)
