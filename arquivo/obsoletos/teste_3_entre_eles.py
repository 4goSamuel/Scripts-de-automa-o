import pyautogui
import time
import random
import keyboard

from conversas9 import *

# =========================
# COORDENADAS DOS WPP
# =========================

wpps = [
    (1505, 223),   # WPP 1
    (1505, 223),   # WPP 1
    (1995, 225),   # WPP 2
    (1995, 225),   # WPP 2
    (2027, 605),   # WPP 3
    (2027, 605),   # WPP 3

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



print("Conversa finalizada.")