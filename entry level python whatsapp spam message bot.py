import pyautogui
import time

#here we download the pyautogui library from cmd via the internet and add it to our windows library and run the code in our internal library


time.sleep(0)

def message():

    pyautogui.write("gardas") #we write the message we are going to send here
    pyautogui.press("enter")  #which is our message sending key in whatsapp, we assign it here.

    

while True:
    message()
    time.sleep(0)

#In addition, here we enter the number of messages we want to send and in addition we write how many messages we want to send and how long the intervals will be.