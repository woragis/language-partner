from langchain.agents import Tool
from llms.chatgpt import get_chatgpt

chatgpt_llm = get_chatgpt()

chatgpt_tool = Tool(
    name="chatgpt_tool",
    func=lambda q: chatgpt_llm.predict(q),
    description="General conversation and reasoning"
)
