import pyautogui
import time
import random

# =========================
# COORDENADAS DOS WPP
# =========================

wpps = [
    (766, 687),   # WPP 1
    (1867, 620),  # WPP 2
    (1200, 700),  # WPP 3
    (1500, 500),  # WPP 4
]

# =========================
# CONVERSAS
# =========================

conversas = [
    conversa1,
    conversa2,
    conversa3,
    conversa4,
]

# =========================
# DIGITAÇÃO
# =========================

def digitar(msg):
    pyautogui.write(
        msg,
        interval=random.uniform(0.04, 0.10)
    )

# =========================
# TEMPO
# =========================

print("Iniciando em 5 segundos...")
time.sleep(5)

# =========================
# LOOP PRINCIPAL
# =========================

quantidade_msgs = min(len(c) for c in conversas)

for i in range(quantidade_msgs):

    for j in range(len(wpps)):

        x, y = wpps[j]

        pyautogui.moveTo(x, y, duration=1)

        time.sleep(random.uniform(1, 2))

        pyautogui.click()

        digitar(conversas[j][i])

        pyautogui.press("enter")

        time.sleep(random.uniform(2, 5))

print("Conversa finalizada.")