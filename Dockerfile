FROM public.ecr.aws/amazonlinux/amazonlinux:2

# Install python for running the server and net-tools for modifying network config
RUN yum install python3 iproute git   -y
RUN pip3 install --upgrade pip && pip3 install grpcio grpcio-tools

WORKDIR /app

RUN git clone https://github.com/kenmaro3/grpc_auth.git

COPY run.sh ./

RUN cd grpc_auth && cd proto && sh run.sh && cp -r grpc_service /app/

RUN chmod +x /app/run.sh

#CMD ["/app/run.sh"]
CMD ["tail", "-f", "/app/run.sh"]