import pyautogui
import time
import winsound

print("Posicione o mouse no canto SUPERIOR ESQUERDO da conversa")
time.sleep(5)
x1,y1 = pyautogui.position()

# alerta sonoro
winsound.Beep(800, 700)

print("Agora no canto INFERIOR DIREITO da conversa")
time.sleep(5)
x2, y2 = pyautogui.position()

# alerta sonoro
winsound.Beep(1200, 700)

print(f'Região: x = {x1}, y = {y1}, width = {x2 - x1}, height= {y2 - y1}')