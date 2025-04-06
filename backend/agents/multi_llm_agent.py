from langchain.agents import initialize_agent, AgentType
from tools.chatgpt_tool import chatgpt_tool
from tools.grok_search_tool import grok_tool
from llms.gemini import get_gemini


def build_agent():
    gemini_llm = get_gemini()

    tools = [chatgpt_tool, grok_tool]

    agent = initialize_agent(
        tools=tools,
        llm=gemini_llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    return agent
