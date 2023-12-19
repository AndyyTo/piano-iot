from aliot.aliot_obj import AliotObj
import piano_utils
import time
import sys
import cv2
import mediapipe as mp
import threading
import gpt

piano = AliotObj("piano")

mp_draw = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands

cap = cv2.VideoCapture(0)
tipIds = [4, 8, 12, 16, 20]


def start():
    while True:
        try:
            line = piano_utils.listen().split(";")
            if line:
                print(line)
                piano.update_component("MyLog", line[1])
                piano.update_component("Buzzer", line[0])
        except KeyboardInterrupt:
            break

def startMediapipe():
    t = time.time()
    while True:
        with mp_hand.Hands(min_detection_confidence=0.5,
                           min_tracking_confidence=0.5) as hands:
            ret, image = cap.read()
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = hands.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            lmList = []
            if results.multi_hand_landmarks:
                for hand_landmark in results.multi_hand_landmarks:
                    myHands = results.multi_hand_landmarks[0]
                    for id, lm in enumerate(myHands.landmark):
                        h, w, c = image.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        lmList.append([id, cx, cy])
                    mp_draw.draw_landmarks(image, hand_landmark, mp_hand.HAND_CONNECTIONS)
            fingers = 0
            if len(lmList) != 0:
                if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                    fingers += 1
                for i in tipIds[1:]:
                    if lmList[i][2] < lmList[i - 1][2]:
                        fingers += 2 ** (i // 4 - 1)
                if time.time() - t > 1:
                    t = time.time()
                    print(fingers)
                    piano_utils.set_button_state(fingers)
            cv2.imshow("result", image)
            k = cv2.waitKey(1)
            if k == ord('q'):
                break
#create threads for functions
thread1 = threading.Thread(target=start)
thread2 = threading.Thread(target=startMediapipe)

#start the threads
thread1.start()
thread2.start()

def button_do(data):
    piano.update_component("MyLog", "Do")
    piano_utils.set_button_state(1)


def button_re(data):
    piano.update_component("MyLog", "Re")
    piano_utils.set_button_state(2)


def button_mi(data):
    piano.update_component("MyLog", "Mi")
    piano_utils.set_button_state(3)


def button_fa(data):
    piano.update_component("MyLog", "Fa")
    piano_utils.set_button_state(4)


def button_sol(data):
    piano.update_component("MyLog", "Sol")
    piano_utils.set_button_state(5)


def button_la(data):
    piano.update_component("MyLog", "La")
    piano_utils.set_button_state(6)


def button_si(data):
    piano.update_component("MyLog", "Si")
    piano_utils.set_button_state(7)


def button_do2(data):
    piano.update_component("MyLog", "Do2")
    piano_utils.set_button_state(8)

def gptPrompt(data):
    chords = gpt.generate_music(data)
    piano_utils.frequencies_array(chords)


piano.on_action_recv(action_id="do", callback=button_do)
piano.on_action_recv(action_id="re", callback=button_re)
piano.on_action_recv(action_id="mi", callback=button_mi)
piano.on_action_recv(action_id="fa", callback=button_fa)
piano.on_action_recv(action_id="sol", callback=button_sol)
piano.on_action_recv(action_id="la", callback=button_la)
piano.on_action_recv(action_id="si", callback=button_si)
piano.on_action_recv(action_id="do2", callback=button_do2)

piano.on_action_recv(action_id="prompt", callback=gptPrompt)

piano.on_start(callback=start)
piano.run()
cap.release()
cv2.destroyAllWindows()