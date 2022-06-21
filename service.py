from concurrent import futures
import pickle
import grpc
import json
import os
import sys
import numpy as np
import pprint

from grpc_service import myserver_pb2
from grpc_service import myserver_pb2_grpc

from grpc_service.model import message_pb2


from log import logging
logger = logging.getLogger(__name__)

class MyServerService(myserver_pb2_grpc.MyServerServicer):
    def __init__(self) -> None:
        super().__init__()

    def test0(self, request, context):
        print(request.message)

        return  message_pb2.PB_Message(message="result from 0!")

    def test1(self, request, context):
        print(request.message)

        return  message_pb2.PB_Message(message="result from 1!")
