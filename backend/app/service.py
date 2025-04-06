import grpc
from app import llm_pb2, llm_pb2_grpc
from app.llm_chain import LLMWrapper


class LLMServicer(llm_pb2_grpc.LLMServiceServicer):
    def __init__(self):
        self.chain = LLMWrapper()

    def GenerateText(self, request, context):
        prompt = request.prompt
        response_text = self.chain.generate(prompt)
        return llm_pb2.GenerateResponse(response=response_text)
