FROM ubuntu
RUN apt-get update && apt-get install -y --force-yes python3-pip build-essential libssl-dev libffi-dev python3-dev
RUN pip3 install cryptography redis
WORKDIR /workspace
