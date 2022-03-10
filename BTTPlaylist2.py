#/Users/nokhimwong/opt/anaconda3/envs/allPython/bin/python /Users/nokhimwong/Programming/Learning/python/PlaylistAutomation/BTTPlaylist.py
#tried locate but original file worked after chdir
import pyautogui
import pygetwindow as gw
import time
from PIL import ImageGrab

filelink = "/Users/isaac/Documents/Programming/Python/PlaylistAutomation/img/"
x, y = pyautogui.size()

z1 = list(gw.getWindowGeometry("YouTube"))
pyautogui.click(z1[0], z1[1])
im = ImageGrab.grab(bbox = z1)

for i in range(0, len(z1)):
    z1[i] = int(z1[i])
print(z1)


z1[2] += z1[0]
z1[3] += z1[1]
print(z1)

print("start search...")
#all
try:
    all = pyautogui.center(pyautogui.locate(filelink+"all.png",im))
except Exception as e:
    print(e)
    print(filelink+"all.png")
print(all)

#pyautogui.moveTo(x=all[0], y=all[1],duration=0.25)
#pyautogui.click(x=all[0], y=all[1])

time.sleep(2)

print("more")
#more
im = ImageGrab.grab(bbox = z1)

more = pyautogui.locate(filelink+"more.png",im)
print(more)
#pyautogui.click(x=more[0], y=more[1])
pyautogui.moveTo(x=z1[0], y=z1[1])
time.sleep(2)

#playlist
im = ImageGrab.grab(bbox = z1)
playlist = pyautogui.locate(filelink+"Motivation.png",im)
print(playlist)
pyautogui.click(x=playlist[0], y=playlist[1])
time.sleep(2)

#mix
im = ImageGrab.grab(bbox = z1)
mix = pyautogui.center(pyautogui.locate(filelink+"mix.png",im))
print(mix)
pyautogui.click(x=mix[0], y=mix[1])