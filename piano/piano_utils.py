import serial
import time
import threading
import handWatcher

ser = serial.Serial('COM5', 9600)

_button_state = False


def listen():
    return ser.readline().decode().strip()


def set_button_state(state):
    global _button_state
    if state in (1, 2, 3, 4, 5, 6, 7, 8):
        ser.write(str(state).encode())


def get_button_state():
    return _button_state


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


