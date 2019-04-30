# import socket programming library 
import socket 
  
# import thread module 
from _thread import *
from threading import *
import time
from random import *

my_IP = input("target IP: ")
listen_Port_low = input("target port start: ")
listen_Port_high = input("target port end: ")
seed = input("seed: ")
message = "fake message, but real enough 12341254135 123"

rand  = Random(seed)
valid_port = rand.randint(listen_Port_low, listen_Port_high)
lock = Lock()

def incoming(my_IP, my_listen_port):
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    my_socket.bind((my_IP, my_listen_port))
    global lock
    
    data, addr = my_socket.recvfrom(4048)
    lock.acquire()
    print("incoming data form ", my_listen_port, " saying: ", data)
    if(valid_port == my_listen_port):
        print("I am the current port: ", my_listen_port)
    lock.release()


def Main():
    global my_IP, listen_Port_high, listen_Port_low

    
    while True:
        x = 0
        for i in range(listen_Port_low-1, listen_Port_high+1):
            start_new_thread(incoming, (my_IP, i)) 
        print("listeners ready")
        x = input("next")



if __name__ == "__main__":
    Main()

