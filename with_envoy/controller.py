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
import constants

from log import logging
logger = logging.getLogger(__name__)


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

    logger.info(f"[MyServerControllergRPC] Init okay at: {constants.SERVER_PORT}")
    logger.info(
        f"[MyServerControllergRPC] max_message_length: {constants.GRPC_MAX_MESSAGE_LENGTH}"
        + f", max_worker: {constants.SERVER_MAX_WORKER}"
    )

    server.wait_for_termination()


if __name__ == "__main__":
    run()
