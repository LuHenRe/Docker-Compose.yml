FROM alpine:latest

# Instala todas as ferramentas necessárias
RUN apk add --no-cache \
    python3 \
    py3-pip \
    iproute2 \
    iputils \
    tcpdump \
    curl \
    bash \
    nmap

# Instala scapy (para ARP Spoofing)
RUN pip3 install scapy

WORKDIR /app

# Copia o script de ataque
COPY spoofing.py .

# Mantém o container rodando
CMD ["tail", "-f", "/dev/null"]
