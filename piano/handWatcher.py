import time
from typing import NamedTuple

import cv2
from matplotlib.transforms import Bbox
import mediapipe as mp
import math


class HandWatcher:
    def __init__(self, cap, mode=False, maxHands=2, detectionCon=0.5, minTrackCon=0.5):
        """
        :param mode: In static mode, detection is done on each image: slower
        :param maxHands: Maximum number of hands to detect
        :param detectionCon: Minimum Detection Confidence Threshold
        :param minTrackCon: Minimum Tracking Confidence Threshold
        """

        self.cap = cap
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.minTrackCon = minTrackCon
        self.mpDraw = mp.solutions.drawing_utils

        self.tipIds = [4, 8, 12, 16, 20]
        self.cap = None

    def capture(self):
        ret, image = self.cap.read()

    def track(self):
        ret, image = self.cap.read()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = self.hands.process(image)
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
                self.mpDraw.draw_landmarks(image, hand_landmark, self.mpHands.HAND_CONNECTIONS)
        fingers = 0
        if len(lmList) != 0:
            if lmList[self.tipIds[0]][1] > lmList[self.tipIds[0] - 1][1]:
                fingers += 1
            for i in self.tipIds[1:]:
                if lmList[i][2] < lmList[i - 1][2]:
                    fingers += 2 ** (i // 4 - 1)
        # cv2.destroy

            # print(finger_counter)
            # publish.single(MQTT_PATH, finger_counter, hostname=MQTT_SERVER)
            # cv2.putText(image, 'Forward', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_4)
            # cv2.putText(image, str(fingers), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2,
            #             cv2.LINE_4)

        return fingers
            # elif finger_counter == 4:
            #    cv2.putText(image, 'Backward', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_4)

        # cv2.imshow("result", image)

