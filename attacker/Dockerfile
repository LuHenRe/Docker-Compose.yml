FROM alpine:latest

# Instala Python, ferramentas de rede e Scapy via apk
RUN apk add --no-cache \
    python3 \
    py3-pip \
    py3-scapy \
    iproute2 \
    iputils \
    tcpdump \
    curl \
    bash

WORKDIR /app
COPY spoofing.py .

# Container fica ativo
CMD ["tail", "-f", "/dev/null"]
