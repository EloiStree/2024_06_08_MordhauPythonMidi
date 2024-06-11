# pip install keyboard pyperclip pygetwindow mido python-rtmidi

import mido
import socket
import struct
import time
import random 


# Change with your MIDI keyboard name
# You can find it by running the script once and looking at the available devices
keyboard_to_listen="MPK mini play 1"

# Some keyboard need some additional configuration to push note on computer
# (Not the case most of the time, if it happens try an other keyboard or read the doc of the keyboard)

# Change with your IP and port if you know what you do
UDP_IP_TARGET=["127.0.0.1"]
UDP_PORT =[3614, 7000, 5648]




def send_udp_message(int_command):
                global UDP_IP_TARGET ,  UDP_PORT
                for ipv4 in UDP_IP_TARGET:
                    for port in UDP_PORT:
                        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        sock.sendto(struct.pack("<i",int_command), (ipv4, port))
                        sock.close()
               

def on_message(message):
    if message.type == 'note_on':
        print(f"Note {message.note} on")
        if(str(message.note) not in midi_to_mordhau):
            print(f"Note {message.note} not mapped to any command")
            return
        else:
            cmd_mordhau_as_int=int(midi_to_mordhau[str(message.note)])
            print(f"Mordhay command: {cmd_mordhau_as_int}")
            send_udp_message(cmd_mordhau_as_int)

    elif message.type == 'note_off':
        print(f"Note {message.note} off")

def launch_listener():
    global keyboard_to_listen
    # List all available MIDI devices
    print("Available MIDI devices:")
    for device in mido.get_input_names():
        print(device)

    bool_keyboard_found=False
    try:
        # Select the desired MIDI device
        input_device = mido.open_input(keyboard_to_listen)
        bool_keyboard_found=True
    except:
        print(f"Device {keyboard_to_listen} not found")
        print(" ")
        print(" ")
        print(" ")
    
    if not bool_keyboard_found:
        
        print("Available MIDI devices:")
        devices = mido.get_input_names()
        for device in devices:
            print(device)
        for i in range(len(devices)-1, 0, -1):
            try:
                print(i)
                # Select the desired MIDI device
                input_device = mido.open_input(devices[i])
                bool_keyboard_found=True
                keyboard_to_listen=devices[i]
                break
            except:
                print(f"Device {devices[i]} not connectable")
                print(" ")

 

    # Start listening for MIDI messages
    print("Listening to MIDI notes...")
    for message in input_device:
        on_message(message)


midi_to_mordhau= {}
midi_to_mordhau["36"]="-2"
midi_to_mordhau["41"]="-1"
midi_to_mordhau["48"]="1"
midi_to_mordhau[""]="2"
midi_to_mordhau["49"]="3"
midi_to_mordhau[""]="4"
midi_to_mordhau["50"]="5"
midi_to_mordhau[""]="6"
midi_to_mordhau["51"]="7"
midi_to_mordhau[""]="8"
midi_to_mordhau["52"]="9"
midi_to_mordhau[""]="10"
midi_to_mordhau["53"]="11"
midi_to_mordhau[""]="12"
midi_to_mordhau["54"]="13"
midi_to_mordhau[""]="14"
midi_to_mordhau["55"]="15"
midi_to_mordhau[""]="16"
midi_to_mordhau["56"]="17"
midi_to_mordhau[""]="18"
midi_to_mordhau["57"]="19"
midi_to_mordhau[""]="20"
midi_to_mordhau["58"]="21"
midi_to_mordhau[""]="22"
midi_to_mordhau["59"]="23"
midi_to_mordhau[""]="24"
midi_to_mordhau["60"]="25"
midi_to_mordhau[""]="26"
midi_to_mordhau["61"]="27"
midi_to_mordhau[""]="28"
midi_to_mordhau["62"]="29"
midi_to_mordhau[""]="30"
midi_to_mordhau["63"]="31"
midi_to_mordhau[""]="32"
midi_to_mordhau["64"]="33"
midi_to_mordhau[""]="34"
midi_to_mordhau["65"]="35"
midi_to_mordhau[""]="36"
midi_to_mordhau["66"]="37"
midi_to_mordhau[""]="38"
midi_to_mordhau["67"]="39"
midi_to_mordhau[""]="40"
midi_to_mordhau["68"]="41"
midi_to_mordhau[""]="42"
midi_to_mordhau["69"]="43"
midi_to_mordhau[""]="44"
midi_to_mordhau["70"]="45"
midi_to_mordhau[""]="46"
midi_to_mordhau["71"]="47"
midi_to_mordhau[""]="48"
midi_to_mordhau[""]="49"
midi_to_mordhau[""]="50"
midi_to_mordhau[""]="51"
midi_to_mordhau[""]="52"
midi_to_mordhau[""]="53"
midi_to_mordhau[""]="54"
midi_to_mordhau[""]="55"
midi_to_mordhau[""]="56"
midi_to_mordhau[""]="57"
midi_to_mordhau[""]="58"
midi_to_mordhau[""]="59"
midi_to_mordhau["72"]="60"

midi_to_mordhau[""]="61"
midi_to_mordhau["21"]="62"
midi_to_mordhau[""]="63"
midi_to_mordhau[""]="64"
midi_to_mordhau[""]="65"
midi_to_mordhau[""]="66"
midi_to_mordhau[""]="67"
midi_to_mordhau[""]="68"
midi_to_mordhau[""]="69"
midi_to_mordhau[""]="70"
midi_to_mordhau[""]="71"
midi_to_mordhau[""]="72"
midi_to_mordhau[""]="73"
midi_to_mordhau[""]="74"
midi_to_mordhau[""]="75"
midi_to_mordhau["17"]="76"
midi_to_mordhau[""]="77"
midi_to_mordhau[""]="78"
midi_to_mordhau[""]="79"
midi_to_mordhau[""]="80"
midi_to_mordhau[""]="81"
midi_to_mordhau[""]="82"
midi_to_mordhau[""]="83"
midi_to_mordhau["22"]="84"
midi_to_mordhau[""]="85"
midi_to_mordhau[""]="86"
midi_to_mordhau[""]="87"
midi_to_mordhau[""]="88"
midi_to_mordhau["18"]="89"
midi_to_mordhau[""]="90"
midi_to_mordhau[""]="91"
midi_to_mordhau[""]="92"
midi_to_mordhau[""]="93"
midi_to_mordhau[""]="94"
midi_to_mordhau[""]="95"
midi_to_mordhau[""]="96"
midi_to_mordhau[""]="97"
midi_to_mordhau["23"]="98"
midi_to_mordhau[""]="99"
midi_to_mordhau[""]="100"
midi_to_mordhau[""]="101"
midi_to_mordhau[""]="102"
midi_to_mordhau[""]="103"
midi_to_mordhau["19"]="104"
midi_to_mordhau[""]="105"
midi_to_mordhau[""]="106"
midi_to_mordhau[""]="107"
midi_to_mordhau[""]="108"
midi_to_mordhau[""]="109"
midi_to_mordhau[""]="110"
midi_to_mordhau[""]="111"
midi_to_mordhau[""]="112"
midi_to_mordhau[""]="113"
midi_to_mordhau[""]="114"
midi_to_mordhau[""]="115"
midi_to_mordhau[""]="116"
midi_to_mordhau[""]="117"
midi_to_mordhau[""]="118"
midi_to_mordhau[""]="119"
midi_to_mordhau[""]="120"


launch_listener()