from aliot.aliot_obj import AliotObj
import piano_utils
import time
import sys

piano = AliotObj("piano")


def button_do(data):
    print("do")
    piano_utils.set_button_state(1)

def button_re(data):
    print("re")
    piano_utils.set_button_state(2)

def button_mi(data):
    print("mi")
    piano_utils.set_button_state(3)

def button_fa(data):
    print("fa")
    piano_utils.set_button_state(4)

def button_sol(data):
    print("sol")
    piano_utils.set_button_state(5)

def button_la(data):
    print("la")
    piano_utils.set_button_state(6)

def button_si(data):
    print("si")
    piano_utils.set_button_state(7)

def button_do2(data):
    print("do2")
    piano_utils.set_button_state(8)

def music(data):
    for i in data.split(";"):
        piano_utils.set_button_state(int(i))
        time.sleep(2)


piano.on_action_recv(action_id="do", callback=button_do)
piano.on_action_recv(action_id="re", callback=button_re)
piano.on_action_recv(action_id="mi", callback=button_mi)
piano.on_action_recv(action_id="fa", callback=button_fa)
piano.on_action_recv(action_id="sol", callback=button_sol)
piano.on_action_recv(action_id="la", callback=button_la)
piano.on_action_recv(action_id="si", callback=button_si)
piano.on_action_recv(action_id="do2", callback=button_do2)
piano.on_action_recv(action_id="music", callback=music)

piano.run()