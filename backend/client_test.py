import grpc
from app import llm_pb2, llm_pb2_grpc

channel = grpc.insecure_channel("localhost:50051")
stub = llm_pb2_grpc.LLMServiceStub(channel)

response = stub.GenerateText(llm_pb2.GenerateRequest(prompt="Tell me a joke"))
print("🤖 LLM says:", response.response)
