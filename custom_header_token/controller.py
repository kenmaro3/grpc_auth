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

class AuthInterceptor(grpc.ServerInterceptor):
    def __init__(self, key):
        self._valid_metadata = ('rpc-auth-header', key)

        def deny(_, context):
            context.abort(grpc.StatusCode.UNAUTHENTICATED, 'Invalid key')

        self._deny = grpc.unary_unary_rpc_method_handler(deny)


    def validate_party(self, party_index, meta, continuation, handler_call_details):
        if meta and meta[0].value == self._valid_metadata[1][party_index]:
            return continuation(handler_call_details)
            #return self._deny
        else:
            logging.info(f"denied: {meta[0].value} vs {self._valid_metadata[party_index]}, {self._valid_metadata}")
            return self._deny


    def intercept_service(self, continuation, handler_call_details):
        meta = handler_call_details.invocation_metadata

        method = handler_call_details.method.split("/")[2]

        if method == "test0":
            return self.validate_party(0, meta, continuation, handler_call_details)
        elif method == "test1":
            return self.validate_party(1, meta, continuation, handler_call_details)
        else:
            raise Exception(f"got method: {handler_call_details.method}, {method}")




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
        futures.ThreadPoolExecutor(max_workers=constants.SERVER_MAX_WORKER),
        options=options,
        interceptors=(AuthInterceptor(['mytoken0', 'mytoken1']),)
        # interceptors=(AuthInterceptor('mytoken'),)
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
