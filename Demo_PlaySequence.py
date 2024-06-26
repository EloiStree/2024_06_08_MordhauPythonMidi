
# Want to play in loop the sequence of notes 1 to 60

import random
import socket

import time
import struct

# Frequence to test the notes 0-60
bool_use_0to60_at_start=True
# Time between note on the test
int_frequence=0.1

time_between_loop_end=5


ipv4_target= "127.0.0.1"
port_target= [5648,3614]
#5648 defaut for Mordhau Midi Github
#3614 defaut for Python IID Websocket Sync


sockets={}
sockets_address={}
for i in range(len(port_target)):
    sockets[i]=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sockets_address[i]=(ipv4_target, port_target[i])
   
def send_note(value_int_0_60):
    print("Sending note: "+str(value_int_0_60))
    for i in range(len(port_target)):        
        sockets[i].sendto(struct.pack("<i", value_int_0_60), sockets_address[i])

    # Close the socket
exit_condition=False

# Wait you to be in the game
time.sleep(3)

# Quick test that all notes are working
if bool_use_0to60_at_start:
    for i in range(1,60):
        send_note(i)
        time.sleep(int_frequence)


while not exit_condition:
    
    # Adn your sequence here
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
    time.sleep(time_between_loop_end)


sock.close()