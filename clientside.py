# import socket programming library 
import socket 
  
# import thread module 
from _thread import *
import threading 
import time



relay_IP = input("relay IP: ")
relay_port = input("relay port: ")
real_IP = input("real IP: ")
real_port = input("real port: ")
otherside_IP = input("otherside IP:")
otherside_port = input("otherside port:")

relay = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# outconnection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
real = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
real.bind((real_IP,real_port))
relay.bind((relay_IP,relay_port))
# outconnecrelay
# outconnection.bind((otherside_IP,otherside_port))

def outgoing():
    global relay, real ,relay_IP, relay_port
    global otherside_IP, otherside_port, real_IP, relay_port
    while True:
        out_data, out_addr = real.recvfrom(4048)
        relay.sendto(out_data, (otherside_IP,otherside_port ))
        # print("out: ", len(out_data))

def incoming():
    global relay, real ,relay_IP, relay_port
    global otherside_IP, otherside_port, real_IP, relay_port
    while True:
        in_data, in_addr = relay.recvfrom(4048)
        relay.sendto(in_data, (real_IP, real_port))
        # print("in :", len(in_data))


def Main():

    start_new_thread(outgoing, ()) 
    start_new_thread(incoming, ()) 
    while True:
        i=0


if __name__ == '__main__':
    Main()
