from concurrent import futures
import grpc

from generated import greeter_pb2_grpc
from app.greeter_service import GreeterService


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greeter_pb2_grpc.add_GreeterServicer_to_server(GreeterService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('GRPC server is running on Port 50051')
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
