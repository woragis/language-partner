# client.py
import grpc

from generated import greeter_pb2, greeter_pb2_grpc
from generated import ai_pb2, ai_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        # Greeting route testing
        stub = greeter_pb2_grpc.GreeterStub(channel)
        request = greeter_pb2.HelloRequest(name='Jezreel')
        response = stub.SayHello(request)
        print("🧍 Client received:", response.message)

        # Ai route testing
        stub = ai_pb2_grpc.AIStub(channel)
        prompt = 'Hello, my name is jezreel'
        chat_request = ai_pb2.ChatRequest(prompt=prompt)
        response = stub.Chat(chat_request)
        print("🧍 Ai Response:", response.response)


if __name__ == '__main__':
    run()
