import random
import socket

import time
import struct

int_frequence=1

while True:
        
    # Generate a random integer value
    random_value = random.randint(-2, 120)
    random_value = random.randint(1, 60)

    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Set the destination address and port
    server_address = ('localhost', 5648)

    # Send the random value to the server
    sock.sendto(struct.pack("<i", random_value), server_address)

    # Close the socket
    sock.close()
    time.sleep(int_frequence)
