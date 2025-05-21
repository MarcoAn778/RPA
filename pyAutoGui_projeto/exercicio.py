import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press('win')
time.sleep(1)
pyautogui.write('chome')
time.sleep(1)
pyautogui.press('enter')
pyautogui.click(x=1041, y=598)
pyautogui.write('hashtagtreinamentos.com')
pyautogui.press('enter')
time.sleep(1)
pyautogui.moveTo(x=619, y=166, duration= 1)
#pyautogui.click(x=501, y=275)
time.sleep(1)
posicao_cursoexel = pyautogui.locateCenterOnScreen('Img.excel.png')
pyautogui.click(posicao_cursoexel)
time.sleep(1)
pyautogui.click(x=493, y=575)
pyautogui.write('Josias')
pyautogui.press('tab')
pyautogui.write('teste@gmail.com')
pyautogui.press('tab')
pyautogui.write('7799238456')
pyautogui.press('tab')
pyautogui.press('enter')