import socket

udp_uip_addr = "127.0.0.1"
udp_port = 14550
# declare our serverSocket upon which
# we will be listening for UDP messages
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# One difference is that we will have to bind our declared IP address
# and port number to our newly declared serverSock
serverSock.bind((udp_uip_addr, udp_port))

udp_uip_client = "127.0.0.1"
udp_port_client = 14555
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
# serverSock.bind((udp_uip_client, udp_port_client)) 


while True:
    data, addr = serverSock.recvfrom(1024)
    print  data
    clientSock.sendto(data, (udp_uip_client, udp_port_client))
    dataclient, addrclient = clientSock.recvfrom(1024)
    serverSock.sento(dataclient, (udp_uip_addr, udp_port))
