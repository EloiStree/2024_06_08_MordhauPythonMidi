
# This script send random note to check that the Mordhau injector work as planned.

import random
import socket

import time
import struct

int_frequence=0.1

ipv4_target= "127.0.0.1"
port_target= 5648
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send_note(value_int_0_60):
    # Create a UDP socket
    server_address = (ipv4_target, port_target)
    sock.sendto(struct.pack("<i", value_int_0_60), server_address)

    # Close the socket
exit_condition=False
while not exit_condition:
        
    
    for i in range(1,60):
        send_note(i)
        time.sleep(int_frequence)
    
    
    send_note(1)
    time.sleep(0.1)
    send_note(10)
    time.sleep(1)
    send_note(60)
    time.sleep(2)
    send_note(50)
    time.sleep(1)
    send_note(40)
    time.sleep(0.5)
    send_note(30)
    time.sleep(0.25)
    send_note(20)
    time.sleep(0.1)
    send_note(10)
    time.sleep(0.05)



sock.close()