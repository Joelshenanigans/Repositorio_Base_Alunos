import pyautogui
import webbrowser
import time 

# passo 1: abrir o Youtube com uma música específica
url = 'https://www.youtube.com/watch?v=M7sdAzMv83Q'
webbrowser.open(url)

# passo 2: aguardar o carregamento da página
time.sleep(5) # ajustar de acordo com a velocidade da internet utilizada

# passo 3: garantir que o video comece (aperte o espaço para 'play')
pyauogui.press('space') # toca ou pausa o video










