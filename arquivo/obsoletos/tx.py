import pyautogui
import time
import random
import keyboard

from conversas9 import *

# =========================
# COORDENADAS DOS WPP
# =========================

wpps = [

    (1721, 469),   # WPP 5
    (1727, 575),   # WPP 8
    (1723, 618),   # WPP 9
    (1727, 683),   # WPP 11
    (1728, 715),   # WPP 12
    (2017, 411),   # WPP EXTRA
    (1964, 410),   # WPP EXTRA
    (2017, 408),   # WPP EXTRA
    (1964, 411),   # WPP EXTRA
    (2017, 412),   # WPP EXTRA
]

# =========================
# POSIÇÕES DOS BLOCOS
# =========================

blocos = [

    (1703, 376), # bloco 11
    (1701, 335), # bloco 10
    (1696, 305), # bloco 9
    (1699, 271), # bloco 8

    (1699, 160), # bloco 5

]

# =========================
# CONVERSAS
# =========================

# Lista com todas as conversas
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
    conversa11,
    conversa12,

]


# =========================
# DIGITAÇÃO 80 A 120 PALAVRAS POR MINUTO
# =========================

def digitar(msg):

    keyboard.write(
        msg,
        delay=random.uniform(0.035, 0.122)
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

        time.sleep(random.uniform(0.2, 0.5))

        pyautogui.click()

        digitar(conversas[j][i])

        pyautogui.press("enter")

        time.sleep(random.uniform(0.34, 0.5))

        print(f"Mensagem {i} enviada")

    # =========================
    # CLICA NOS BLOCOS
    # =========================

    for bx, by in blocos:

        pyautogui.moveTo(bx, by, duration=0.2)

        time.sleep(random.uniform(0.05, 0.093        ))

        pyautogui.click()

print("Conversa finalizada.")