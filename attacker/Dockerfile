FROM ubuntu:22.04

# Atualiza e instala tudo
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    tcpdump \
    curl \
    iproute2 \
    iputils-ping \
    net-tools \
    && pip3 install scapy \
    && apt-get clean

WORKDIR /app
COPY spoofing.py .

CMD ["tail", "-f", "/dev/null"]
