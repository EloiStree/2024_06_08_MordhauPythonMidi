
import keyboard
import time
import struct
import socket
import keyboard
import time
import struct
import socket
import pyperclip
import random


bool_use_keyboard_input=False


pyperclip.copy("Hello")
time_for_clipboard_to_be_effective=0.01
time_for_past_to_be_effective=0.01
time_between_notes=0.1

key_for_shawm= "o"
key_for_lute= "p"

def change_to_shawm():
    if(bool_use_keyboard_input):
        keyboard.press_and_release(key_for_shawm)
def change_to_flute():
    if(bool_use_keyboard_input):
        keyboard.press_and_release(key_for_shawm)

def change_to_lute():
    if(bool_use_keyboard_input):
        keyboard.press_and_release(key_for_lute)


def play_on_notes(int_note_0_60:int):
    pyperclip.copy(f"equipmentcommand {int_note_0_60}")    
    keyboard.press_and_release('enter')
    keyboard.press_and_release('enter')
    keyboard.press_and_release('u')
    time.sleep(time_for_clipboard_to_be_effective)
    keyboard.press_and_release('ctrl+v')
    time.sleep(time_for_past_to_be_effective)
    keyboard.press_and_release('enter')

def play_all_notes():
    for i in range(0,60):
        play_on_notes(i)
        time.sleep(time_between_notes)

def play_lute_note(int_note_0_60:int):
    change_to_lute()
    play_all_notes(int_note_0_60)

def play_flute_note(int_note_0_60:int):
    change_to_flute()
    play_all_notes(int_note_0_60)



time.sleep(3)
change_to_lute()
play_all_notes()
change_to_shawm()
play_all_notes()


change_to_lute()
time.sleep(2)
for i in range(0,20):
    play_on_notes(random.randint(0,60))
    time.sleep(time_between_notes)

change_to_shawm()
time.sleep(2)
for i in range(0,20):
    play_on_notes(random.randint(0,60))
    time.sleep(time_between_notes)
                  

                  