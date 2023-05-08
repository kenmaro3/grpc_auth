import time
import pickle
import sys

sys.path.append("../")

import grpc
from grpc_service import myserver_pb2_grpc

from grpc_service.model import message_pb2



if __name__ == "__main__":
    print("hello, world")
    host = "13.230.132.241"
    #host = "localhost"
    if False:
        with open('server.crt', 'rb') as f:
            trusted_certs = f.read()

        credentials = grpc.ssl_channel_credentials(root_certificates=trusted_certs)
        channel = grpc.secure_channel('localhost:5555', credentials)

    channel = grpc.insecure_channel(f'{host}:5555', options=[])
    stub = myserver_pb2_grpc.MyServerStub(channel)

    res = stub.test1(message_pb2.PB_Message())

    print(f"res: {res.message}")


