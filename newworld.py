from datetime import datetime
import pyautogui
import time
running = True
afkBot = False
inQueue = False
userTime = input("please enter the time you want the game launched. H/M/S in 24 hour time. Ex: 13:04:59\n Note: Only works on 1080p moniters. \n")
while running:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current time is:", current_time)
    if (current_time == userTime) and inQueue == False:
        pyautogui.click(419, 435)
        time.sleep(250)
        pyautogui.click(1446, 942)
        time.sleep(15)
        pyautogui.click(1680, 968)
        time.sleep(10)
        pyautogui.click(1680, 968)
        time.sleep(10)
        pyautogui.click(1680, 968)
        time.sleep(500)
        while True:
            pyautogui.press("w")
            time.sleep(10)
