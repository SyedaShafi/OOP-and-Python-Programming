import pyautogui
from time import *
sleep(4)
for i in range(1, 5):
    pyautogui.write('Hello brother!', interval=0.25)
    pyautogui.press('enter')


