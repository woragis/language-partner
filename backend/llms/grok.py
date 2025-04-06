from langchain.llms.base import LLM
from typing import Optional


class GrokSearchLLM(LLM):
    def _call(self, prompt: str, stop: Optional[list[str]] = None) -> str:
        return f"[Grok Search] Simulated search for: {prompt}"

    @property
    def _llm_type(self):
        return "grok"
