FROM alpine:latest

# Instala ferramentas
RUN apk add --no-cache \
    python3 \
    py3-pip \
    iproute2 \
    iputils \
    tcpdump \
    curl \
    bash

# Instala scapy com a flag para bypass
RUN pip3 install scapy --break-system-packages

WORKDIR /app
COPY spoofing.py .

CMD ["tail", "-f", "/dev/null"]
