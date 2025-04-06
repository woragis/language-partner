from grpc import Channel, insecure_channel

from generated import greeter_pb2, greeter_pb2_grpc
from generated import ai_pb2, ai_pb2_grpc


def test_greeter(channel: Channel) -> str:
    stub = greeter_pb2_grpc.GreeterStub(channel)
    request = greeter_pb2.HelloRequest(name='Jezreel')
    response = stub.SayHello(request)
    return response


def test_ai_search(channel: Channel) -> str:
    return


def test_ai_talk(channel: Channel) -> str:
    stub = ai_pb2_grpc.AIStub(channel)
    prompt = 'Hello, my name is jezreel'
    chat_request = ai_pb2.ChatRequest(prompt=prompt)
    response = stub.Chat(chat_request)
    return response


def test_ai_audio_input(channel: Channel) -> str:
    return


def run():
    with insecure_channel('localhost:50051') as channel:
        # Greeting route testing
        greeter_response = test_greeter(channel)
        print("🧍 Client received:", greeter_response.message)

        # Ai route testing
        ai_talk_response = test_ai_talk(channel)
        print("🧍 Ai Response:", ai_talk_response.response)


if __name__ == '__main__':
    run()
