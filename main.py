import pyautogui
import PIL
from PIL import Image
import numpy
from pynput import keyboard, mouse
import time
import requests
import json
import random
import tkinter

root = tkinter.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()


def checkNotif1080():
    screen = pyautogui.screenshot()
    screen.save(r"screen.png")
    white = [255, 255, 255]
    image = Image.open("screen.png")
    image = numpy.array(image, dtype=numpy.uint8)
    pixels = [list(i[:3]) for i in image[997]]

    checks = []

    #Check C
    if pixels[1706] == white and pixels[1705] != white and pixels[1707] != white:
        #Valid
        checks.append(0)

    # Check L
    if pixels[1715] == white and pixels[1714] != white and pixels[1716] != white:
        # Valid
        checks.append(0)

    # Check O
    if pixels[1718] == white and pixels[1717] != white and pixels[1719] != white:
        # Valid
        checks.append(0)

    # Check S
    if pixels[1728] == white and pixels[1727] != white and pixels[1729] != white:
        # Valid
        checks.append(0)

    # Check E
    if pixels[1733] == white and pixels[1734] == white and pixels[1735] == white and pixels[1736] == white and pixels[1737] == white and pixels[1732] != white and pixels[1738] != white:
        # Valid
        checks.append(0)

    return len(checks) == 5


def checkNotif768():
    screen = pyautogui.screenshot()
    screen.save(r"screen.png")
    white = [255, 255, 255]
    image = Image.open("screen.png")
    image = numpy.array(image, dtype=numpy.uint8)
    pixels = [list(i[:3]) for i in image[685]]

    checks = []

    # Check C
    if pixels[1152] == white and pixels[1151] != white and pixels[1153] != white:
        # Valid
        checks.append(0)

    # Check L
    if pixels[1161] == white and pixels[1160] != white and pixels[1162] != white:
        # Valid
        checks.append(0)

    # Check O
    if pixels[1164] == white and pixels[1163] != white and pixels[1165] != white:
        # Valid
        checks.append(0)

    # Check S
    if pixels[1174] == white and pixels[1173] != white and pixels[1175] != white:
        # Valid
        checks.append(0)

    # Check E
    if pixels[1179] == white and pixels[1180] == white and pixels[1181] == white and pixels[1182] == white and pixels[
        1183] == white and pixels[1178] != white and pixels[1184] != white:
        # Valid
        checks.append(0)

    return len(checks) == 5

lel = requests.get("https://www.themoviescoop.com/articles/articles.js").text
lel2 = requests.get("https://www.themoviescoop.com/articles/archived_articles.js").text

lel = r'{}'.format(lel[7:-1])
lel = json.loads(lel)
lel2 = r'{}'.format(lel2[16:-1])
lel2 = json.loads(lel2)

links = []

for i in lel["newArticles"].keys():
    links.append("https://www.themoviescoop.com/articles/" + lel["newArticles"][i]["file"])

for i in lel["oldArticles"].keys():
    links.append("https://www.themoviescoop.com/articles/" + lel["oldArticles"][i]["file"])

for i in lel2.keys():
    links.append("https://www.themoviescoop.com/articles/" + lel2[i]["file"])

kb = keyboard.Controller()
ky = keyboard.Key
ms = mouse.Controller()


def prs(key):
    kb.press(key)
    kb.release(key)

def command(key):
    kb.press(ky.ctrl)
    kb.press(key)
    kb.release(ky.ctrl)
    kb.release(key)

time.sleep(5)

while True:
    command("t")
    time.sleep(1)
    kb.type(links[random.randint(0,len(links)-1)])
    time.sleep(0.5)
    prs(ky.enter)
    time.sleep(5)
    for i in range(20):
        ms.scroll(0, -1)
        time.sleep(random.randint(0, 1))
        for j in range(random.randint(0, 3)):
            pyautogui.moveTo(random.randint(round(width/4), round(width*(3/4))), random.randint(round(height/4), round(height*(3/4))), random.random())
            time.sleep(random.randint(1, 3))

    command("w")
    for i in range(5):
        prs(ky.f5)
        time.sleep(1)

    if checkNotif1080():
        ms.position = (1735, 996)
        ms.press(mouse.Button.left)
        ms.release(mouse.Button.left)

        ms.position = (round(width/2), round(height/2))
        ms.press(mouse.Button.left)
        ms.release(mouse.Button.left)
    time.sleep(30)

#1705 87 86 86
#1706 255 255 255
#1707 127 127 127


#1714 84 84 84
#1715 255 255 255
#1716 126 126 126


#1717 85 85 85
#1718 255 255 255
#1719 125 125 125


#1727 229 229 229
#1728 255 255 255
#1729 242 242 242


#1733 255 255 255
#1734 255 255 255
#1735 255 255 255
#1736 255 255 255
#1737 255 255 255