from aliot.aliot_obj import AliotObj
import piano_utils
import time
import sys

piano = AliotObj("piano")


def start():
    while True:
        try:
            line = piano_utils.listen().split(";")
            print("test" + " " + str(line))
            if line:
                if line[2] == "button":
                    piano.update_component("MyLog", line[3])
                if line[0] == "frequency":
                    print(line)
                    piano.update_doc({
                        "/doc/frequency": line[1]
                    })
                    time.sleep(1)
                    piano.update_component("Buzzer", line[1])
            time.sleep(1)
        except KeyboardInterrupt:
            break


def button_do(data):
    print("do")
    piano.update_component("MyLog", "Do")
    piano_utils.set_button_state(1)


def button_re(data):
    print("re")
    piano.update_component("MyLog", "Re")
    piano_utils.set_button_state(2)


def button_mi(data):
    print("mi")
    piano.update_component("MyLog", "Mi")
    piano_utils.set_button_state(3)


def button_fa(data):
    print("fa")
    piano.update_component("MyLog", "Fa")
    piano_utils.set_button_state(4)


def button_sol(data):
    print("sol")
    piano.update_component("MyLog", "Sol")
    piano_utils.set_button_state(5)


def button_la(data):
    print("la")
    piano.update_component("MyLog", "La")
    piano_utils.set_button_state(6)


def button_si(data):
    print("si")
    piano.update_component("MyLog", "Si")
    piano_utils.set_button_state(7)


def button_do2(data):
    print("do2")
    piano.update_component("MyLog", "Do2")
    piano_utils.set_button_state(8)


def music(data):
    for i in data.split(";"):
        piano.update_component("MyLog", "Music")
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

piano.on_start(callback=start)
piano.run()
