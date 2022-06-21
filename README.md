https://qiita.com/kenmaro/items/8517c78d5207252c229a

## grpc + python + (ssl or token ) auth

This repository is about quick tutorial for

- `grpc + python + ssl`
- `grpc + python + header token`

authentication.

## Step

#### create ssh keys
$ sh keygen.sh

**make sure Common Name: localhost**


#### cp server.crt, server.key

#### build protos
and sed.sh is for path
$ cd proto && mkdir grpc_service && python gen.py && cd grpc_service && sh sed.sh && cd .. && cp -r grpc_service ../


