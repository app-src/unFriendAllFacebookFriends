from pyautogui import locateOnScreen, center, click, hotkey, moveTo, scroll
import time
from pynput import keyboard

threeDots = "threeDots.png"
unFriend = "unFriend.png"
confirm = "confirm.png"


time.sleep(5)

unfrnds=0

while True:
    
    if unfrnds==2:
        scroll(-150)
        print("number of frnds")
        unfrnds=0
    location=None
    while location==None:
        location = locateOnScreen(threeDots, confidence = 0.8)
        print("Finding ThreeDot Button")
        
    point = center(location)
    x,y=point
    click(x,y)
    time.sleep(0.5)

    

#"""

    location=None
    while location==None:
        location = locateOnScreen(unFriend,confidence=0.8)
        print("Finding UnFriend Button")
        
    point = center(location)
    x,y=point
    click(x,y)

    location=None
    while location==None:
        location = locateOnScreen(confirm)
        print("Finding confirm Button")
        if location != None:
            unfrnds+=1
        
        
    point = center(location)
    x,y=point
    click(x,y)
    


#"""





