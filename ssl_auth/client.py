import time
import numpy as np
import pandas as pd
import pickle
import sys
from sklearn.model_selection import train_test_split

sys.path.append("../")

import grpc
from grpc_service import myserver_pb2_grpc

from grpc_service.model import message_pb2


def client_stream():
    for i in range(5):
        yield message_pb2.PB_Message(message=f"message from client: {i}")


if __name__ == "__main__":
    print("hello, world")
    with open('server.crt', 'rb') as f:
        trusted_certs = f.read()

    credentials = grpc.ssl_channel_credentials(root_certificates=trusted_certs)
    channel = grpc.secure_channel('localhost:5555', credentials)

    # channel = grpc.insecure_channel('localhost:5555', options=[])
    stub = myserver_pb2_grpc.MyServerStub(channel)

    # res = stub.test1(message_pb2.PB_Message())
    res = stub.test2(client_stream())
    print(f"res: {res.message}")

    res = stub.test3(message_pb2.PB_Message(message="client message"))
    for el in res:
        print(el.message)



