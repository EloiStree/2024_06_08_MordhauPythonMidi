import mido
import os

import random
import socket

import time
import struct


file_name_list= ["Battlefield.mid","Pirates.mid","Mortal.mid",]

file_name= "Pirates.mid"
file_name= "Mortal.mid"
file_name= "Battlefield.mid"

absolut_path_folder='C:/Users/elois/Desktop/2024_06_08_MordhauPythonMidi/Note/'


ipv4_target= "127.0.0.1"
port_target= [5648,3614]
#5648 defaut for Mordhau Midi Github
#3614 defaut for Python IID Websocket Sync

use_percentage= False
use_offset= True
offset=-20


sockets={}
sockets_address={}
for i in range(len(port_target)):
    sockets[i]=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sockets_address[i]=(ipv4_target, port_target[i])
   
def send_note(value_int_0_60):
    if(value_int_0_60<0):
        return
    if(value_int_0_60>60):
        return
        
    print("Sending note: "+str(value_int_0_60))
    for i in range(len(port_target)):        
        sockets[i].sendto(struct.pack("<i", value_int_0_60), sockets_address[i])



def display_notes(midi_file):
    mid = mido.MidiFile(midi_file)
    
    for msg in mid.play():
        if msg.type == 'note_on':
            if use_percentage:
                percent = msg.note/127
                i60 = int(percent*60)
                send_note(i60)
                print(f"Note: {msg.note} | Time: {msg.time}")
            elif use_offset:
                send_note(msg.note+offset)
                print(f"Note: {msg.note} | Time: {msg.time}")
            
        
def try_to_play(name_file):
    global absolut_path_folder
    
    print("Trying to play: "+name_file)
    if os.path.exists(name_file):
        display_notes(name_file)
    elif os.path.exists(absolut_path_folder+name_file):
        p = absolut_path_folder+name_file
        print("Trying to play: "+p)
        display_notes(p)
    

for file_name in file_name_list:
        try_to_play(file_name)
