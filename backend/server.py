from concurrent import futures
import grpc

from generated import greeter_pb2, greeter_pb2_grpc


class GreeterService(greeter_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        print(f'Received request from: {request.name}')
        return greeter_pb2.HelloReply(message=f'Hello {request.name}')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greeter_pb2_grpc.add_GreeterServicer_to_server(GreeterService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('GRPC server is running on Port 50051')
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
