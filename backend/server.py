import grpc
from concurrent import futures
import time

import llm_pb2
import llm_pb2_grpc


class LLMServicer(llm_pb2_grpc.LLMServiceServicer):
    def GenerateText(self, request, context):
        prompt = request.prompt
        response_text = f"Echo: {prompt}"  # Replace with LangChain logic
        return llm_pb2.GenerateResponse(response=response_text)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    llm_pb2_grpc.add_LLMServiceServicer_to_server(LLMServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC server is running on port 50051")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
