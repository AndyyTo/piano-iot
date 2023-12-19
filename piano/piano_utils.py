import serial
import time
import threading
import gpt

ser = serial.Serial('COM6', 9600)

_button_state = False


def listen():
    return ser.readline().decode().strip()

state_to_frequency = {
    1: gpt.frequencies["c4"],
    2: gpt.frequencies["d4"],
    3: gpt.frequencies["e4"],
    4: gpt.frequencies["f4"],
    5: gpt.frequencies["g4"],
    6: gpt.frequencies["a4"],
    7: gpt.frequencies["b4"],
    8: gpt.frequencies["c5"],   
}

def set_button_state(state):
    if state in state_to_frequency:
        frequency = state_to_frequency[state]
        ser.write(str(frequency).encode())


def get_button_state():
    return _button_state

def frequencies_array(chords):
    for i in chords:
        ser.write((str(i) + "x").encode())




def read_from_serial():
    global _button_state
    try:
        ser.flush()
        while True:
            if ser.in_waiting > 0:
                _button_state = ser.readline().decode().strip()
            time.sleep(1)

    except KeyboardInterrupt:
        print("Exiting...")


