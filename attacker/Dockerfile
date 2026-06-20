FROM alpine:latest

# Instala Python e ferramentas de rede (sem pip)
RUN apk add --no-cache \
    python3 \
    iproute2 \
    iputils \
    tcpdump \
    curl \
    bash

# Instala Scapy diretamente pelo gerenciador de pacotes do Alpine
RUN apk add --no-cache py3-scapy

WORKDIR /app
COPY spoofing.py .

# Mantém o container rodando
CMD ["tail", "-f", "/dev/null"]
