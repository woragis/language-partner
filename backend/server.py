import grpc
from concurrent import futures
import time
from app import llm_pb2_grpc
from app.service import LLMServicer


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    llm_pb2_grpc.add_LLMServiceServicer_to_server(LLMServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("✅ gRPC server running on port 50051")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        print("🛑 Shutting down...")
        server.stop(0)


if __name__ == "__main__":
    serve()
