import pyautogui
import time
import random
import keyboard

from conversas8 import *

# =========================
# COORDENADAS DOS WPP
# =========================

wpps = [
    (1720, 323),    # WPP 1
    (1988, 223),    # WPP matucv 1
    (1726, 358),    # WPP 2
    (1978, 225),    # WPP matucv 1
    (1723, 393),   # WPP 3
    (1978, 225),    # WPP matucv 1
    (1729, 428),   # WPP 4
    (1978, 225),    # WPP matucv 1
    (1721, 469),   # WPP 5
    (1978, 225),    # WPP matucv 1


]

# =========================
# POSIÇÕES DOS BLOCOS
# =========================

blocos = [

    (1701, 121), # bloco 4
    (1702, 80), # bloco 3
    (1696, 56), # bloco 2
    (1703, 19), # bloco 1
]

# =========================
# LISTA COM TODAS AS CONVERSAS
# =========================

conversas = [
    conversa1,
    conversa2,
    conversa3,
    conversa4,
    conversa5,
    conversa6,
    conversa7,
    conversa8,
    conversa9,
    conversa10,

]

# =========================
# DIGITAÇÃO HUMANA
# =========================

def digitar(msg):

    keyboard.write(
        msg,
        delay=random.uniform(0.035, 0.142)
    )

# =========================
# INÍCIO
# =========================

print("Iniciando em 5 segundos...")
time.sleep(5)

# =========================
# LOOP PRINCIPAL
# =========================

quantidade_msgs = min(len(c) for c in conversas)

for i in range(quantidade_msgs):

    # =========================
    # ENVIA MENSAGENS NOS WPP
    # =========================

    for j in range(len(wpps)):

        x, y = wpps[j]

        pyautogui.moveTo(x, y, duration=1)

        time.sleep(random.uniform(0.2, 0.6))

        pyautogui.click()

        digitar(conversas[j][i])

        pyautogui.press("enter")

        time.sleep(random.uniform(0.5, 1))

    # =========================
    # CLICA NOS BLOCOS
    # =========================

    for bx, by in blocos:

        pyautogui.moveTo(bx, by, duration=0.2)

        time.sleep(random.uniform(0.5, 0.9))

        pyautogui.click()

    print(f"Mensagem {i} enviada")

print("Conversa finalizada.")