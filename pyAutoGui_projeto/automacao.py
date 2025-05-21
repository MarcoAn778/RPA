import pyautogui
import time

pyautogui.PAUSE = 0.3 # Espera 0.3 segundos a cada linha de codigo

#Pegar informações do mouse e da tela
print(pyautogui.position())
print(pyautogui.size())

#funções do mouse
time.sleep(5)
pyautogui.moveTo(x=625, y=171, duration = 1) #Move para o mouse para a coordenada
pyautogui.click(x=500, y=277) #Da um click no mouse na coordenada
time.sleep(2) #Espera 2 segundos
pyautogui.scroll(-100) # Numero negativo = scroll para baixo

#funções do teclado
pyautogui.write('Bom dia')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('Enter')