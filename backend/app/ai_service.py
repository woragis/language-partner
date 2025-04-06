from generated import ai_pb2, ai_pb2_grpc

# This would normally be replaced with a real AI backend call
def dummy_ai_response(prompt: str) -> str:
    return f"🤖 Echo: {prompt}"

class AIService(ai_pb2_grpc.AIServicer):
    def Chat(self, request, context):
        print(f"📩 Received prompt: {request.prompt}")
        response_text = dummy_ai_response(request.prompt)
        return ai_pb2.ChatResponse(response=response_text)
