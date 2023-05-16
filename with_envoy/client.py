import time
import pickle
import sys

sys.path.append("../")

import grpc
from grpc_service import myserver_pb2_grpc

from grpc_service.model import message_pb2



if __name__ == "__main__":
    print("hello, world")
    #host = "35.78.69.89"
    host = "localhost"

    channel = grpc.insecure_channel(f'{host}:5001', options=[])
    stub = myserver_pb2_grpc.MyServerStub(channel)

    res = stub.test1(message_pb2.PB_Message(message="data"))

    print(f"res: {res.message}")


