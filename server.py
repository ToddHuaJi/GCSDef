# import socket programming library 
import socket 
  
# import thread module 
from _thread import *
import threading 
import time
import string
from random import *

my_IP = input("target IP: ")
listen_Port_low = input("target port start: ")
listen_Port_high = input("target port end: ")
seed = input("seed: ")
message = "fake message, but real enough 12341254135 123"

rand  = Random(seed)
valid_port = rand.randint(listen_Port_low, listen_Port_high)


def outgoing(target_IP, target_port):
    global rand, valid_port
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    if(valid_port == target_port):
        my_socket.sendto((message, (target_IP, target_port))
    else:
        my_socket.sendto(''.join(rand.choice(string.ascii_uppercase + string.digits) for _ in range(rand.randint(0, 100))), (target_IP, target_port))
    


def Main():
    global my_IP, listen_Port_high, listen_Port_low
    global message
   
    print("valid port: ", valid_port)
    while True:
        for i in range(listen_Port_low-1, listen_Port_high+1):
            start_new_thread(outgoing, (my_IP, i)) 

        message = input("message: ")
        



if __name__ == "__main__":
    Main()

