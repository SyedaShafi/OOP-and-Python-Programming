import pyautogui
from time import *
n = int(input())


sleep(3)
for i in range(n):
    pyautogui.press('home')
    for j in range(i+1):
        pyautogui.write('#', interval=0.25)
    pyautogui.press('enter')
    pyautogui.press('home')

              

                 