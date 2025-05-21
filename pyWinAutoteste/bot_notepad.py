from pywinauto.application import Application
from pywinauto import timings
import time

# Inicia o Notepad
app = Application(backend="uia").start("notepad.exe")

# Aguarda a janela aparecer (usando regex no título)
app.window(title_re=".*Bloco de Notas").wait('visible', timeout=10)
janela = app.window(title_re=".*Bloco de Notas")

# Digita algo
janela.type_keys("Meu nome é Mamam!", with_spaces=True)
