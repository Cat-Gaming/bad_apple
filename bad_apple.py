#!/usr/bin/python3
import cv2
from playsound import playsound
import numpy as np
from notifypy import Notify
import time
import os
black_char = "⬛"
white_char = "⬜"
resolution = (64, 64)

notif = Notify("Bad Apple", "⬜⬛⬜")
notif.send()

def convert(li):
    con = []
    for y in range(resolution[0]):
        for x in range(resolution[1]):
            con.append(li[y][x][0])
    return con
def normalize(con):
    noms = []
    for c in con:
        if c == 0:
            noms.append(0)
        elif c == 255:
            noms.append(1)
        else:
            noms.append(0)
    return noms

def draw(pixels):
    os.system('clear')
    string = ""
    i = 0
    for pixel in pixels:
        if i == resolution[0]:
            string += "\n"
            i = 0
        if pixel == 0:
            string += black_char
        else:
            string += white_char
        i += 1
    print(string)

video = cv2.VideoCapture('bad_apple.mp4')

playsound('bad_apple.mp3', False)
while True:
    success, frame = video.read()
    arr = cv2.resize(frame, dsize=resolution, interpolation=cv2.INTER_LINEAR)
    li = arr.tolist()
    con = convert(li)
    nom = normalize(con)
    draw(nom)
    cv2.imshow("frame", arr)
    if cv2.waitKey(30) == ord('q'):
            video.release()
            cv2.destroyAllWindows()
            break