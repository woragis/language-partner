# client.py
import grpc

from generated import greeter_pb2
from generated import greeter_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = greeter_pb2_grpc.GreeterStub(channel)
        request = greeter_pb2.HelloRequest(name='Jezreel')
        response = stub.SayHello(request)
        print("🧍 Client received:", response.message)


if __name__ == '__main__':
    run()
