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



if __name__ == "__main__":
    print("hello, world")
    with open('server.crt', 'rb') as f:
        trusted_certs = f.read()

    credentials = grpc.ssl_channel_credentials(root_certificates=trusted_certs)
    channel = grpc.secure_channel('localhost:5555', credentials)

    # channel = grpc.insecure_channel('localhost:5555', options=[])
    stub = myserver_pb2_grpc.MyServerStub(channel)

    res = stub.test1(message_pb2.PB_Message())

    print(f"res: {res.message}")


