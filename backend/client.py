import grpc
import llm_pb2
import llm_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = llm_pb2_grpc.LLMServiceStub(channel)
    response = stub.GenerateText(llm_pb2.GenerateRequest(prompt="Hello!"))
    print("LLM response:", response.response)


if __name__ == '__main__':
    run()
