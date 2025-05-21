from pywinauto import Application
from pywinauto import Desktop
import time

app = Application(backend="uia").start("calc.exe")
dlg = Desktop(backend= "uia").Calculator


dlg.type_keys('2')
time.sleep(2)
dlg.type_keys('{+}')
time.sleep(2)
dlg.type_keys('3')
time.sleep(2)
dlg.type_keys('=')

resultado = dlg.child_window(auto_id="CalculatorResults", control_type="Text").window_text()

print("Resultado:", resultado)  # Vai imprimir algo como: "Display is 6" ou "O resultado é 6"