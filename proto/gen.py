from grpc.tools import protoc
import glob

protos = glob.glob("./*.proto")
protos.extend(glob.glob("model/*.proto"))

for path in protos:
    protoc.main(
        (
            '',
            '-I.',
            '--python_out=./grpc_service',
            '--grpc_python_out=./grpc_service',
            f'./{path}',
        )
    )


