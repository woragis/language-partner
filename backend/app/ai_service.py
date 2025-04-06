from generated import ai_pb2, ai_pb2_grpc
from agents.multi_llm_agent import build_agent


class AIService(ai_pb2_grpc.AIServicer):

    def __init__(self):
        print("🚀 Initializing multi-LLM agent...")
        self.agent = build_agent()

    def Chat(self, request, context):
        print(f"📩 Received prompt: {request.prompt}")

        try:
            response_text = self.agent.run(request.prompt)
        except Exception as e:
            response_text = f"❌ Error processing request: {e}"

        return ai_pb2.ChatResponse(response=response_text)
