import pyautogui
import time
import random
import keyboard

from conversas8 import *

# =========================
# COORDENADAS DOS WPP
# =========================

wpps = [
    (765, 686),    # WPP 1


]


# =========================
# CONVERSAS
# =========================

# Lista com todas as conversas
conversas = [
    conversa1,
    conversa2,

]


# =========================
# DIGITAÇÃO 80 A 120 PALAVRAS POR MINUTO
# =========================

def digitar(msg):

    keyboard.write(
        msg,
        delay=random.uniform(0.035, 0.059)
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

        time.sleep(random.uniform(0.1, 0.32))

        pyautogui.click()

        digitar(conversas[j][i])

        pyautogui.press("enter")

        time.sleep(random.uniform(0.15, 0.35))

        print(f"Mensagem {i} enviada")


print("Conversa finalizada.")