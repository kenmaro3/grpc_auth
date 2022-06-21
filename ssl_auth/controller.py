from concurrent import futures
import pickle
import grpc
import json
import os
import sys
import numpy as np

sys.path.append("../")

from grpc_service import myserver_pb2
from grpc_service import myserver_pb2_grpc

from service import MyServerService
import constants

from log import logging
logger = logging.getLogger(__name__)


def run():
    options = [
       ("grpc.max_message_length", constants.GRPC_MAX_MESSAGE_LENGTH),
       ("grpc.max_receive_message_length", constants.GRPC_MAX_MESSAGE_LENGTH),
    ]

    with open('server.key', 'rb') as f:
        private_key = f.read()
    with open('server.crt', 'rb') as f:
        certificate_chain = f.read()

    server_credentials = grpc.ssl_server_credentials(
      ((private_key, certificate_chain,),))

    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=constants.SERVER_MAX_WORKER)
        ,options=options
    )
    myserver_pb2_grpc.add_MyServerServicer_to_server(MyServerService(), server)
    #server.add_insecure_port(f"[::]:{constants.SERVER_PORT}")
    server.add_secure_port(f"[::]:{constants.SERVER_PORT}", server_credentials)
    server.start()

    logger.info(f"[MyServerControllergRPC] Init okay at: {constants.SERVER_PORT}")
    logger.info(
        f"[MyServerControllergRPC] max_message_length: {constants.GRPC_MAX_MESSAGE_LENGTH}"
        + f", max_worker: {constants.SERVER_MAX_WORKER}"
    )

    server.wait_for_termination()


if __name__ == "__main__":
    run()
