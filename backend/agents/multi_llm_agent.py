from langchain.agents import initialize_agent, AgentType
from tools.chatgpt_tool import chatgpt_tool
# from tools.grok_search_tool import grok_tool
from tools.gemini_search_tool import gemini_search_tool
from llms.gemini import get_gemini_router


def build_agent():
    gemini_llm = get_gemini_router()

    tools = [chatgpt_tool, gemini_search_tool]

    agent = initialize_agent(
        tools=tools,
        llm=gemini_llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    return agent
