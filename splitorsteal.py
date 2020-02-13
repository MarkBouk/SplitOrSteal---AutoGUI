import pyautogui
import os
import asyncio

dirname = os.path.dirname(__file__)

joinQ = os.path.join(dirname, 'img\Join Queue.png')
accept = os.path.join(dirname, 'img\Accept.png')
split = os.path.join(dirname, 'img\Split.png')
lockIn = os.path.join(dirname, 'img\Lock In.png')
returnToMain = os.path.join(dirname, 'img\Return to Main Menu.png')
returnCancel = os.path.join(dirname, 'img\Return.png')
returnToTier = os.path.join(dirname, 'img\Return to Tier 1.png')

go = True

def splitOrSteal():
    for imgPath in [joinQ, accept, split, lockIn, returnToMain]:
        print("Looking for ", imgPath)
        location = pyautogui.locateCenterOnScreen(imgPath)
        while location == None:
            location = pyautogui.locateCenterOnScreen(imgPath)
            if location == None:
                location = pyautogui.locateCenterOnScreen(returnCancel)
                if location == None:
                    location = pyautogui.locateCenterOnScreen(returnToTier)
                if location != None:
                    pyautogui.click(location)
                    return
        pyautogui.click(location)

while go:
    splitOrSteal()