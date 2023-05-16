from concurrent import futures
import pickle
import grpc
import json
import os
import sys

sys.path.append("../")

from grpc_service import myserver_pb2
from grpc_service import myserver_pb2_grpc

from service import MyServerService


def run():
    options = [
       ("grpc.max_message_length", 20000000),
       ("grpc.max_receive_message_length", 20000000),
    ]


    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=1)
        ,options=options
    )
    myserver_pb2_grpc.add_MyServerServicer_to_server(MyServerService(), server)
    server.add_insecure_port(f"[::]:{5001}")
    server.start()

    print(f"[MyServerControllergRPC] Init okay at: 5001")

    server.wait_for_termination()


if __name__ == "__main__":
    run()
