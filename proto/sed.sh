for filename in *.py; do
  sed -i -e "s/^from model/from grpc_service.model/" $filename
done

for filename in model/*.py; do
  sed -i -e "s/^from model/from grpc_service.model/" $filename
done

