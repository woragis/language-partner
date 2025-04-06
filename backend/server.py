from concurrent import futures
import grpc

from generated import greeter_pb2_grpc, ai_pb2_grpc
from app.greeter_service import GreeterService
from app.ai_service import AIService


def serve():
    # Initialize Server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Add services to server
    greeter_pb2_grpc.add_GreeterServicer_to_server(GreeterService(), server)
    ai_pb2_grpc.add_AIServicer_to_server(AIService(), server)

    # Configure Server Port
    server.add_insecure_port('[::]:50051')

    # Start Server
    server.start()
    print('GRPC server is running on Port 50051')
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
