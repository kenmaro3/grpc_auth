rm -r grpc_service
mkdir grpc_service
python3 gen.py
cp sed.sh grpc_service/
cd grpc_service
sh sed.sh
cd ..
cp -r grpc_service ../

