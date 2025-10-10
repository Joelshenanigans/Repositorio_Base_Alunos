import pyautogui
import time

pyautogui.press('win')
time.sleep(1)
pyautogui.write('desenhado com pyautogui')
pyautogui.press('enter')
time.sleep(2)

arvore = [
    " |\  "
    " | | "
    " | | "
    " | | "
    " ___ "
    " | | "
    " | | "
    
]

for linha in arvore:
    pyautogui.write(linha, interval=0.1)
    pyautogui.press('enter')
print('desenho da árvore concluido!')










