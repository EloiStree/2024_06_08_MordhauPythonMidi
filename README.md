# 2024_06_08_MordhauPythonMidi
Python script to play music with Midi keyboard on Mordhau


![image](https://github.com/EloiStree/2024_06_08_MordhauPythonMidi/assets/20149493/21b7a774-ac24-4005-9c68-d73009d7f00f)



## If on same PC:

Use Mordhau Console Music By UDP IID : file to affect the game
Use MIDI To Mordhau : to send your midi keyboard to the script that affect the game
Use UDP sample : if you need to create your own python script.


## if on remote PC:

- Gate: https://github.com/EloiStree/2024_05_11_GateIID_WS_Python
- Server: https://github.com/EloiStree/2024_04_04_IndexIntegerDateTunnelingRSA




## Local

> MIDI > UDP > Injector > USER32 > Mordhau

Vidéo Français: https://youtu.be/Q0Nym_dJZQE
English video: https://youtu.be/_1cG4yv8woQ

Code to parse your Midi keyboard to the keyboard injector: 
https://github.com/EloiStree/2024_06_08_MordhauPythonMidi/blob/main/MidiToMordhau.py

Code to inject Keyboard or SendMessage key to the Mordhau Game:
https://github.com/EloiStree/2024_06_08_MordhauPythonMidi/blob/main/MordhauConsoleMusicByUDPIID.py



## Sync Online

> MIDI > UDP > IID Client > IID RSA SERVER > IID Client > UDP > Injector > USER32 >Mordhau

Demo video: https://youtu.be/GuHUTRreQYU

## Client
Client code in Python : https://github.com/EloiStree/2024_05_11_GateIID_WS_Python

### Server
Fetch IP of home shared server: https://github.com/EloiStree/IP/blob/main/IIDWS/SERVER.txt
Have your own Server IID: https://github.com/EloiStree/2024_04_04_IndexIntegerDateTunnelingRSA/releases/tag/V0
Code of the server IID: https://github.com/EloiStree/2024_04_04_IndexIntegerDateTunnelingRSA/tree/main/CloudTunnelingRSA
