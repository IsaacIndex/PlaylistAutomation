#/Users/nokhimwong/opt/anaconda3/envs/allPython/bin/python /Users/nokhimwong/Programming/Python/PlaylistAutomation/BTTPlaylist.py
import pyautogui
import pygetwindow as gw
import time
import os
# import multiprocessing

filelink = "/Users/nokhimwong/Programming/Python/PlaylistAutomation/img"
os.chdir(filelink)
x, y = pyautogui.size()

z1 = list(gw.getWindowGeometry("YouTube"))
pyautogui.click(z1[0], z1[1])

for i in range(0, len(z1)):
    z1[i] = int(z1[i])
print(z1)


z1[2] += z1[0]
z1[3] += z1[1]
print(z1)

print("start search...")
#all ==========================================================================
try:
    all = pyautogui.center(pyautogui.locateOnScreen("all.png"))
    print(all)
    pyautogui.click(x=all[0], y=all[1]-10)
    time.sleep(0.5)
except:
    try:
        all2 = pyautogui.center(pyautogui.locateOnScreen("all2.png"))
        print(all2)
        pyautogui.click(x=all2[0], y=all2[1]-10)
        time.sleep(0.5)
    except:
        pass

#more
try:
    more = pyautogui.locateOnScreen('more.png')
    print(more)
    pyautogui.click(x=more[0], y=more[1])
    pyautogui.moveTo(x=z1[0], y=z1[1])
except:
    print("skip show more")
    pass

#playlist
playlist = pyautogui.locateOnScreen("Motivation.png")
playlist_trials = 0
while playlist == None and playlist_trials < 5:
    playlist_trials += 1
    playlist = pyautogui.locateOnScreen("Motivation.png")
print(playlist)
pyautogui.click(x=playlist[0], y=playlist[1])
#time.sleep(0.8)

#mix
mix = pyautogui.locateCenterOnScreen("mix.png")
mix_trials = 0
while mix == None and mix_trials < 5:
    mix_trials += 1
    mix = pyautogui.locateCenterOnScreen("mix.png")
print(mix)
pyautogui.click(x=mix[0], y=mix[1])

#loop
loop = pyautogui.locateCenterOnScreen("loop.png")
loop_trials = 0
while loop == None and loop_trials < 5:
    loop_trials += 1
    loop = pyautogui.locateCenterOnScreen("loop.png")
print(loop)
pyautogui.click(x=loop[0], y=loop[1])


# # Start foo as a process
# p = multiprocessing.Process(target=foo, name="Foo", args=(10,))
# p.start()

# # Wait 10 seconds for foo
# time.sleep(10)

# # Wait a maximum of 10 seconds for foo
# # Usage: join([timeout in seconds])
# p.join(10)

# # If thread is active
# if p.is_alive():
#     print("foo is running... let's kill it...")

#     # Terminate foo
#     p.terminate()
#     p.join()