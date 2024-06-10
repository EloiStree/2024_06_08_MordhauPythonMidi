# pip install keyboard pyperclip pygetwindow mido python-rtmidi
import keyboard
import pyperclip
import pygetwindow as gw
import mido
import time
import struct
import socket
import ctypes

#UDP_PORT=7000
UDP_PORT=5648


window_title = "MORDHAU  "
bool_use_keyboard_input=False

# Constants for SendMessage
WM_KEYDOWN = 0x0100
WM_KEYUP = 0x0101


wait_console_open_delay=0.03
wait_console_open_delay=0.03





# Find the window by its title
def find_window(title):
    return ctypes.windll.user32.FindWindowW(None, title)


def get_all_windows(title):
    list_window_found = [window for window in gw.getAllWindows() if title in window.title]
    return list_window_found



def find_in_all(title):
    global target_window_index
    list_window_found = [window for window in gw.getAllWindows() if title in window.title]
    if list_window_found:
        return list_window_found[0]
    else:
        return None
    
    
def find_in_all(title, index):
    global target_window_index
    list_window_found = [window for window in gw.getAllWindows() if title in window.title]
    if list_window_found and len(list_window_found) > index:
        return list_window_found[index]
    else:
        return None
def find_in_all_count(title):
    global target_window_index
    list_window_found = [window for window in gw.getAllWindows() if title in window.title]
    if list_window_found :
        return len(list_window_found)
    else:
        return 0





all_found_windows_at_start = get_all_windows(window_title)



mordhau_hwnd = find_window(window_title)
found_window_count= find_in_all_count(window_title)
use_print_log=False

print (f"Window found:{mordhau_hwnd} Count:{found_window_count}")

for windowt in all_found_windows_at_start:
    print("Window Title:", windowt.title)
    print("Window ID:", windowt._hWnd)


# Define the necessary structures
PUL = ctypes.POINTER(ctypes.c_ulong)

class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]


# Define the necessary functions
def press_key(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(hexKeyCode, 0x48, 0, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def release_key(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(hexKeyCode, 0x48, 0x0002, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


























timebetweenaction=0.1
timepress=0.1




def enum_child_windows(parent_hwnd):
    child_windows = []

    def enum_child_proc(hwnd, lParam):
        nonlocal child_windows
        child_windows.append(hwnd)
        return True  # Continue enumeration

    # Convert the callback function to a C function pointer
    EnumChildProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))

    # Call EnumChildWindows with the parent window handle and the callback function
    ctypes.windll.user32.EnumChildWindows(parent_hwnd, EnumChildProc(enum_child_proc), 0)

    return child_windows

def is_window_focused(hwnd):
    return user32.GetForegroundWindow() == hwnd

# def send_key(hwnd, key_code):
    
#         child_windows = enum_child_windows(hwnd)
#         # for child_hwnd in child_windows:
#         #     send_key_press(child_hwnd, key_code)
#         #     time.sleep(0.1)  # Optional delay between keydown and keyup
#         #     send_key_release(child_hwnd, key_code)

def send_key_press(hwnd, key_code):
   
        #print("A")
        ctypes.windll.user32.PostMessageW(hwnd, WM_KEYDOWN, key_code, 0)

        #print("B")
        # child_windows = enum_child_windows(hwnd)
        # for child_hwnd in child_windows:
        #     ctypes.windll.user32.SendMessageW(child_hwnd, WM_KEYDOWN, key_code, 0)

def send_key_release(hwnd, key_code):
   
        ctypes.windll.user32.PostMessageW(hwnd, WM_KEYUP, key_code, 0)
        # child_windows = enum_child_windows(hwnd)
        # for child_hwnd in child_windows:
        #     ctypes.windll.user32.SendMessageW(child_hwnd, WM_KEYUP, key_code, 0)
















#------------------------------------------------







pyperclip.copy("Hello")
time_for_clipboard_to_be_effective=0.01
time_for_past_to_be_effective=0.01
time_between_notes=0.1

key_for_shawm= "I"
key_for_lute= "O"
key_for_mute_switch= "p"


def past_key_post():
    global mordhau_hwnd
    send_key_press(mordhau_hwnd, keyboard_mappings["Ctrl"])
    #time.sleep(0.01)
    send_key_press(mordhau_hwnd, keyboard_mappings["V"])
    #time.sleep(0.05)
    send_key_release(mordhau_hwnd, keyboard_mappings["V"])
    #time.sleep(0.01)
    send_key_release(mordhau_hwnd, keyboard_mappings["Ctrl"])
    #time.sleep(0.01)

def pess_and_release_key_post(key):   
        global mordhau_hwnd
        send_key_press(mordhau_hwnd, keyboard_mappings[key])
        #time.sleep(timepress)
        send_key_release(mordhau_hwnd, keyboard_mappings[key])
        #time.sleep(timebetweenaction)

def pess_key_post(key):   
        global mordhau_hwnd
        send_key_press(mordhau_hwnd, keyboard_mappings[key])

def release_key_post(key):   
        global mordhau_hwnd
        send_key_release(mordhau_hwnd, keyboard_mappings[key])


def change_to_flute():
    if(bool_use_keyboard_input):
        keyboard.press_and_release(key_for_shawm)
    else :
        pess_and_release_key_post(key_for_shawm)

def change_to_lute():
    if(bool_use_keyboard_input):
        keyboard.press_and_release(key_for_lute)
    else :
        pess_and_release_key_post(key_for_lute)

def fake_type_past():
    WM_PASTE = 0x0302
    ctypes.windll.user32.SendMessageW(mordhau_hwnd, WM_PASTE, 0, 0)
    

def try_to_write(str_to_write):
    for char in str_to_write:
        char=char.upper()
        if(char=="0"):
            char="NP0"
        elif(char=="1"):
            char="NP1"
        elif(char=="2"):
            char="NP2"
        elif(char=="3"):
            char="NP3"
        elif(char=="4"):
            char="NP4"
        elif(char=="5"):
            char="NP5"
        elif(char=="6"):
            char="NP6"
        elif(char=="7"):
            char="NP7"
        elif(char=="8"):
            char="NP8"
        elif(char=="9"):
            char="NP9"
        pess_key_post(char)
        #time.sleep(0.01)

def play_on_notes(int_note_0_60:int):
    str_to_write=f"equipmentcommand {int_note_0_60}"
    pyperclip.copy(str_to_write)  
    
    if(bool_use_keyboard_input):  
        keyboard.press_and_release('enter')
        keyboard.press_and_release('enter')
        keyboard.press_and_release('u')
        time.sleep(time_for_clipboard_to_be_effective)
        keyboard.press_and_release('ctrl+v')
        time.sleep(time_for_past_to_be_effective)
        keyboard.press_and_release('enter')
    else:
        pess_and_release_key_post('Enter')
        pess_and_release_key_post('Enter')
        pess_and_release_key_post('U')
        time.sleep(0.02)
        try_to_write(str_to_write)
        
        # ##past_key_post()
        # time.sleep(0.01)
        # pess_and_release_key_post("Backspace")
        # time.sleep(0.01)
        # # pess_and_release_key_post("Backspace")
        # time.sleep(0.01)
        time.sleep(0.02)
        pess_and_release_key_post('Enter')
        pess_and_release_key_post('Enter')

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









bool_mute_mode=False
def switch_mute_mode():
        global bool_mute_mode
        bool_mute_mode=not bool_mute_mode
        if bool_mute_mode:
            print("Mute mode enabled")
        else:
            print("Mute mode disabled")


# Function to be called when left Alt key is released
def event_hook_keyboard(event):
    global bool_mute_mode
    #print ("R"+str(event.name)  
    if event.event_type == 'up':  # Check if the event is a key release
 
        if(event.name==key_for_mute_switch):
            switch_mute_mode()

keyboard.hook(event_hook_keyboard)


def listen_udp():
    global UDP_PORT
    global bool_mute_mode
    UDP_IP = "0.0.0.0"
    print("Start listening on UDP port", listen_udp)
    print("-1 for flute")
    print("-2 for lute")
    print("0 to 60 for notes on lute")
    print("61 to 120 for notes on flute")
    print("Maye the music be with you! ")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    last_int_command=0
    note_int_to_play=0
    iid_anti_double_previous=""
    iid_anti_double_current=""
    while True:
        
        data, addr = sock.recvfrom(1024)

        if(bool_mute_mode):
            print("Ignored due to mute mode")
            continue

        bool_is_int_command=False
        int_cmd_value=0
        

        if(len(data)==4):
            int_cmd_value = struct.unpack('<i', data)[0]
            bool_is_int_command=True
        if(len(data)==16):

            index, int_cmd_value, date = struct.unpack('<iiQ', data)[:3]
            iid_anti_double_previous=iid_anti_double_current
            iid_anti_double_current=f"{index}{int_cmd_value}{date}"
            if(iid_anti_double_current==iid_anti_double_previous):
                continue

            bool_is_int_command=True

        if(bool_is_int_command and int_cmd_value>-3 and int_cmd_value<121):
            if int_cmd_value<61 and last_int_command>60:
                
                change_to_lute()
                print("Change to lute")
                
            elif int_cmd_value>60 and last_int_command<61:
                
                change_to_flute()
                print("Change to flute")
                
                
            if(int_cmd_value>60):
                note_int_to_play= int_cmd_value-60
                play_on_notes(note_int_to_play)
            elif int_cmd_value>0:
                note_int_to_play= int_cmd_value
                play_on_notes(note_int_to_play)
            elif int_cmd_value==-1:
                change_to_flute()
            elif int_cmd_value==-2:
                change_to_lute()
            
            last_int_command= int_cmd_value
            print(f"Received {int_cmd_value}")
            # Process the received data here
            # Example: print the received data

# Call the listen_udp function




keyboard_mappings = {
    "Backspace": 0x08,
    "Tab": 0x09,
    "Clear": 0x0C,
    "Enter": 0x0D,
    "Shift": 0x10,
    "Ctrl": 0x11,
    "Alt": 0x12,
    "Pause": 0x13,
    "CapsLock": 0x14,
    "Esc": 0x1B,
    "Escape": 0x1B,
    "Space": 0x20,
    "PageUp": 0x21,
    "PageDown": 0x22,
    "End": 0x23,
    "Home": 0x24,
    "LeftArrow": 0x25,
    "Left": 0x25,
    "UpArrow": 0x26,
    "Up": 0x26,
    "RightArrow": 0x27,
    "Right": 0x27,
    "DownArrow": 0x28,
    "Down": 0x28,
    "Select": 0x29,
    "Print": 0x2A,
    "Execute": 0x2B,
    "PrintScreen": 0x2C,
    "Insert": 0x2D,
    "Delete": 0x2E,
    '0': 0x30,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    '5': 0x35,
    '6': 0x36,
    '7': 0x37,
    '8': 0x38,
    '9': 0x39,
    'A': 0x41,
    'B': 0x42,
    'C': 0x43,
    'D': 0x44,
    'E': 0x45,
    'F': 0x46,
    'G': 0x47,
    'H': 0x48,
    'I': 0x49,
    'J': 0x4A,
    'K': 0x4B,
    'L': 0x4C,
    'M': 0x4D,
    'N': 0x4E,
    'O': 0x4F,
    'P': 0x50,
    'Q': 0x51,
    'R': 0x52,
    'S': 0x53,
    'T': 0x54,
    'U': 0x55,
    'V': 0x56,
    'W': 0x57,
    'X': 0x58,
    'Y': 0x59,
    'Z': 0x5A,
    "LeftWindows": 0x5B,
    "RightWindows": 0x5C,
    "Applications": 0x5D,
    "Sleep": 0x5F,
    "Numpad0": 0x60,
    "Numpad1": 0x61,
    "Numpad2": 0x62,
    "Numpad3": 0x63,
    "Numpad4": 0x64,
    "Numpad5": 0x65,
    "Numpad6": 0x66,
    "Numpad7": 0x67,
    "Numpad8": 0x68,
    "Numpad9": 0x69,
    "Multiply": 0x6A,
    "NP0": 0x60,
    "NP1": 0x61,
    "NP2": 0x62,
    "NP3": 0x63,
    "NP4": 0x64,
    "NP5": 0x65,
    "NP6": 0x66,
    "NP7": 0x67,
    "NP8": 0x68,
    "NP9": 0x69,
    "Multiply": 0x6A,
    "Add": 0x6B,
    "Separator": 0x6C,
    "Subtract": 0x6D,
    "Decimal": 0x6E,
    "Divide": 0x6F,
    "F1": 0x70,
    "F2": 0x71,
    "F3": 0x72,
    "F4": 0x73,
    "F5": 0x74,
    "F6": 0x75,
    "F7": 0x76,
    "F8": 0x77,
    "F9": 0x78,
    "F10": 0x79,
    "F11": 0x7A,
    "F12": 0x7B,
    "F13": 0x7C,
    "F14": 0x7D,
    "F15": 0x7E,
    "F16": 0x7F,
    "F17": 0x80,
    "F18": 0x81,
    "F19": 0x82,
    "F20": 0x83,
    "F21": 0x84,
    "F22": 0x85,
    "F23": 0x86,
    "F24": 0x87,
    "NumLock": 0x90,
    "ScrollLock": 0x91,
    "LeftShift": 0xA0,
    "RightShift": 0xA1,
    "LeftControl": 0xA2,
    "RightControl": 0xA3,
    "LeftAlt": 0xA4,
    "RightAlt": 0xA5,
    "LeftMenu": 0xA4,
    "RightMenu": 0xA5,
    "BrowserBack": 0xA6,
    "BrowserForward": 0xA7,
    "BrowserRefresh": 0xA8,
    "BrowserStop": 0xA9,
    "BrowserSearch": 0xAA,
    "BrowserFavorites": 0xAB,
    "BrowserHome": 0xAC,
    "VolumeMute": 0xAD,
    "VolumeDown": 0xAE,
    "VolumeUp": 0xAF,
    "MediaNext Track": 0xB0,
    "MediaPrevious Track": 0xB1,
    "MediaStop": 0xB2,
    "MediaPlay": 0xB3,
    "LaunchMail": 0xB4,
    "LaunchMedia Select": 0xB5,
    "LaunchApp1": 0xB6,
    "LaunchApp2": 0xB7,
    "OEM1": 0xBA,
    "OEMPlus": 0xBB,
    "OEMComma": 0xBC,
    "OEMMinus": 0xBD,
    "OEMPeriod": 0xBE,
    "OEM2": 0xBF,
    "OEM3": 0xC0,
    "OEM4": 0xDB,
    "OEM5": 0xDC,
    "OEM6": 0xDD,
    "OEM7": 0xDE,
    "OEM8": 0xDF,
    "OEM102": 0xE2,
    "ProcessKey": 0xE5,
    "Packet": 0xE7,
    "Attn": 0xF6,
    "CrSel": 0xF7,
    "ExSel": 0xF8,
    "EraseEOF": 0xF9,
    "Play": 0xFA,
    "Zoom": 0xFB,
    "PA1": 0xFD,
    " ":  0x20,
    "0x08":"0x08",
    "0x09":"0x09",
    "0x0C":"0x0C",
    "0x0D":"0x0D",
    "0x10":"0x10",
    "0x11":"0x11",
    "0x12":"0x12",
    "0x13":"0x13",
    "0x14":"0x14",
    "0x1B":"0x1B",
    "0x20":"0x20",
    "0x21":"0x21",
    "0x22":"0x22",
    "0x23":"0x23",
    "0x24":"0x24",
    "0x25":"0x25",
    "0x26":"0x26",
    "0x27":"0x27",
    "0x28":"0x28",
    "0x29":"0x29",
    "0x2A":"0x2A",
    "0x2B":"0x2B",
    "0x2C":"0x2C",
    "0x2D":"0x2D",
    "0x2E":"0x2E",
    "0x30":"0x30",
    "0x31":"0x31",
    "0x32":"0x32",
    "0x33":"0x33",
    "0x34":"0x34",
    "0x35":"0x35",
    "0x36":"0x36",
    "0x37":"0x37",
    "0x38":"0x38",
    "0x39":"0x39",
    "0x41":"0x41",
    "0x42":"0x42",
    "0x43":"0x43",
    "0x44":"0x44",
    "0x45":"0x45",
    "0x46":"0x46",
    "0x47":"0x47",
    "0x48":"0x48",
    "0x49":"0x49",
    "0x4A":"0x4A",
    "0x4B":"0x4B",
    "0x4C":"0x4C",
    "0x4D":"0x4D",
    "0x4E":"0x4E",
    "0x4F":"0x4F",
    "0x50":"0x50",
    "0x51":"0x51",
    "0x52":"0x52",
    "0x53":"0x53",
    "0x54":"0x54",
    "0x55":"0x55",
    "0x56":"0x56",
    "0x57":"0x57",
    "0x58":"0x58",
    "0x59":"0x59",
    "0x5A":"0x5A",
    "0x5B":"0x5B",
    "0x5C":"0x5C",
    "0x5D":"0x5D",
    "0x5F":"0x5F",
    "0x60":"0x60",
    "0x61":"0x61",
    "0x62":"0x62",
    "0x63":"0x63",
    "0x64":"0x64",
    "0x65":"0x65",
    "0x66":"0x66",
    "0x67":"0x67",
    "0x68":"0x68",
    "0x69":"0x69",
    "0x6A":"0x6A",
    "0x6B":"0x6B",
    "0x6C":"0x6C",
    "0x6D":"0x6D",
    "0x6E":"0x6E",
    "0x6F":"0x6F",
    "0x70":"0x70",
    "0x71":"0x71",
    "0x72":"0x72",
    "0x73":"0x73",
    "0x74":"0x74",
    "0x75":"0x75",
    "0x76":"0x76",
    "0x77":"0x77",
    "0x78":"0x78",
    "0x79":"0x79",
    "0x7A":"0x7A",
    "0x7B":"0x7B",
    "0x7C":"0x7C",
    "0x7D":"0x7D",
    "0x7E":"0x7E",
    "0x7F":"0x7F",
    "0x80":"0x80",
    "0x81":"0x81",
    "0x82":"0x82",
    "0x83":"0x83",
    "0x84":"0x84",
    "0x85":"0x85",
    "0x86":"0x86",
    "0x87":"0x87",
    "0x90":"0x90",
    "0x91":"0x91",
    "0xA0":"0xA0",
    "0xA1":"0xA1",
    "0xA2":"0xA2",
    "0xA3":"0xA3",
    "0xA4":"0xA4",
    "0xA5":"0xA5",
    "0xA6":"0xA6",
    "0xA7":"0xA7",
    "0xA8":"0xA8",
    "0xA9":"0xA9",
    "0xAA":"0xAA",
    "0xAB":"0xAB",
    "0xAC":"0xAC",
    "0xAD":"0xAD",
    "0xAE":"0xAE",
    "0xAF":"0xAF",
    "0xB0":"0xB0",
    "0xB1":"0xB1",
    "0xB2":"0xB2",
    "0xB3":"0xB3",
    "0xB4":"0xB4",
    "0xB5":"0xB5",
    "0xB6":"0xB6",
    "0xB7":"0xB7",
    "0xBA":"0xBA",
    "0xBB":"0xBB",
    "0xBC":"0xBC",
    "0xBD":"0xBD",
    "0xBE":"0xBE",
    "0xBF":"0xBF",
    "0xC0":"0xC0",
    "0xDB":"0xDB",
    "0xDC":"0xDC",
    "0xDD":"0xDD",
    "0xDE":"0xDE",
    "0xDF":"0xDF",
    "0xE2":"0xE2",
    "0xE5":"0xE5",
    "0xE7":"0xE7",
    "0xF6":"0xF6",
    "0xF7":"0xF7",
    "0xF8":"0xF8",
    "0xF9":"0xF9",
    "0xFA":"0xFA",
    "0xFB":"0xFB",
    "0xFD":"0xFD"
}




listen_udp()



