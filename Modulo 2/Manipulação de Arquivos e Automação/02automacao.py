# automção que faça o mouse se mover na forma de um quadrado

import pyautogui

for i in range(10):
    # .moveTo é uma função de movimento de mouse
    # pyautogui.moveto(x,y,duration=em segundos)
    pyautogui.moveTo(100 + 10 * i, 100 + 10 * i, duration=0.25)
    pyautogui.moveTo(200 + 10 * i, 100 + 10 * i, duration=0.25)
    pyautogui.moveTo(200 + 10 * i, 200 + 10 * i, duration=0.25)
    pyautogui.moveTo(100 + 10 * i, 200 + 10 * i, duration=0.25)













