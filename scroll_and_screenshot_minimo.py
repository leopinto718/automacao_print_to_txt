import pyautogui
import time
import os
import winsound
import cv2
import numpy as np

# CONFIGURAÇÕES
OUTPUT_DIR = "screenshots"
SCROLL_AMOUNT = 800 # pixels por scroll
WAIT_AFTER_SCROLL = 2.0 # segundos
REGION = (476, 88, 883, 626) #melhor: poderia ser lido a partir de um arquivo gerado anteriormente
# (x, y, width, height)
DIFF_TRESHOLD = 2.0 #ajuste empírico (?)
STABLE_LIMIT = 3 # número de repetições consecutivas

os.makedirs(OUTPUT_DIR, exist_ok= True)

# DEFINIÇÃO DAS FUNÇÕES 
def image_difference(img1, img2):
    """
    Retorna a diferença média normalizada entre duas imagens
    """

    diff = cv2.absdiff(img1, img2)
    return np.mean(diff)

def preprocess(pil_image):
    img = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2GRAY)
    img = cv2.resize(img, (300,300))
    return img


print("Você tem cinco segundos para clicar na janela do WhatsApp Web...")
winsound.Beep(800,700)
time.sleep(5)

prev_img = None
stable_count = 0
i = 1

while True:
    screenshot = pyautogui.screenshot(region = REGION)
    screenshot.save(f'{OUTPUT_DIR}/chat_{i:05d}.png')

    curr_img = preprocess(screenshot)

    if prev_img is not None:
        diff = image_difference(prev_img, curr_img)
        print(f"Imagem {i} - diferença: {diff:.2f}")

        if diff < DIFF_TRESHOLD:
            stable_count += 1
            print(f"Conteúdo estável ({stable_count}/{STABLE_LIMIT})")

            if stable_count >= STABLE_LIMIT:
                print("Fim do histórico detectado automaticamente.")
                break
        else:
            stable_count = 0 # reset se houve mudança real

    prev_img = curr_img

    pyautogui.scroll(SCROLL_AMOUNT)
    time.sleep(WAIT_AFTER_SCROLL)
    i += 1


# alerta sonoro
winsound.Beep(1200, 700)
