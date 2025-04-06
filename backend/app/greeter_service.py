from generated import greeter_pb2, greeter_pb2_grpc


class GreeterService(greeter_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        print(f'Received request from: {request.name}')
        return greeter_pb2.HelloReply(message=f'Hello {request.name}')
