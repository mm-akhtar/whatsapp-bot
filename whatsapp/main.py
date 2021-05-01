import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep (3)

# position1 = pt.locateOnScreen("whatsapp/smily_paperclip.png", confidence=.6)
position1 = pt.locateOnScreen("whatsapp/wtp_icon.png", confidence=.6)
print("got this")

x = position1[0]
y = position1[1]

#Gets message

def get_message():
    global x, y

    position = pt.locateOnScreen("whatsapp/smily_paperclip.png", confidence=.6)
    x= position[0]
    y= position[1]
    pt.moveTo(x,y, duration=.5)
    pt.moveTo(x + 100, y - 60, duration=.5)
    pt.tripleClick()
    # experiment
    # pt.doubleClick()
    # pt.dragRel(50,-330, duration=1)
    pt.rightClick()
    pt.moveRel(12,15)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print("message received: " + whatsapp_message)
    return whatsapp_message

#posts
def post_response(message):
    global x,y

    position = pt.locateOnScreen("whatsapp/smily_paperclip.png", confidence=.6)
    x= position[0]
    y= position[1]

    pt.moveTo(x +200, y + 20, duration=.5)
    pt.click()
    pt.typewrite(message, interval=0.1)

    pt.typewrite("\n", interval=0.1)

#processes response
def process_response(message):
    random_no = random.randrange(3)

    if "?" in str(message).lower():
        return "Don't ask me anything"

    else:
        if random_no ==0:
            return"that's cool"
        elif random_no == 1:
            return "Remenber to subscribe "
        else:
            return "I want to eat something"

#check for new messages
def check_for_new_messages():
    pt.moveTo(x + 50, y -60, duration=.5)

    while True:
        # continously checks for green dot
        try:
            position = pt.locateOnScreen("whatsapp/green_circle.png", confidence=.7)

            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100,0)
                pt.click()
                sleep(.5)

        except(Exception):
            print("No new messages located")

        if pt.pixelMatchesColor(int(x+  50), int(y -55), (38,45,49), tolerance=20):
            print("black")
            processed_message =process_response(get_message())
            post_response(processed_message)

        else:
            print("no new messages yet")
            
        sleep(50)


#open whatsapp
def start_whatsapp():
    global x, y
    position = pt.locateOnScreen("whatsapp/wtp_icon.png", confidence=.6)
    x= position[0]
    y= position[1]
    pt.moveTo(x+10,y+10, duration=.5)
    # pt.moveRel(x+50, y -20, duration=.5)
    pt.click()




start_whatsapp()
check_for_new_messages()
            