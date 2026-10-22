import pyautogui
import time
import random

# =========================
# COORDENADAS DA BARRA DE TEXTO DO WPP
# =========================

wpps = [
    (1720, 323),    # WPP 1
    (1726, 358),   # WPP 2
    (1723, 393),   # WPP 3
    (1729, 428),   # WPP 4
    (1721, 469),   # WPP 5
    (2005, 369),    # WPP 6
    (2005, 369),   # WPP 7
    (2005, 369),   # WPP 8
    (2005, 369),   # WPP 9
    (2005, 369),   # WPP 10
]

# =========================
# POSIÇÕES DE ORDENAÇÃO
# =========================

blocos = [

    (1699, 160), # bloco 5
    (1701, 121), # bloco 4
    (1702, 80), # bloco 3
    (1696, 56), # bloco 2
    (1703, 19), # bloco 1
]

# =========================
# CONVERSAS
# =========================

conversa1 = [
    "mano hoje aconteceu uma parada muito aleatória no trabalho",
    " ",
    "a mulher simplesmente entrou na sala errada e começou reclamar pro setor errado",

]

conversa2 = [
    "cara eu dormi muito mal hoje",
    " ",
    "fiquei vendo vídeo até quase 4h sem perceber",

]

conversa3 = [
    "mano preciso te contar uma coisa",
    " ",
    " ",

]

conversa4 = [
    "cara hoje o sistema resolveu enlouquecer",
    " ",
    "simplesmente começou dar erro sem motivo aparente",

]

conversa5 = [
    "cara hoje eu percebi oficialmente que virei adulto cansado",
    " ",
    "fiquei feliz porque cancelaram um compromisso",

]

conversa6 = [
    "oi ",
    "o que aconteceu?",
    "KKKKKKKKKKKKKK cara impossível",

]

conversa7 = [
    "oi ",
    "fala aí",
    "KKKKKKKKKKKKKKK documentário de avião é clássico da madrugada",

]

conversa8 = [
    "oooi ",
    " ",
    "conte logo velho",

]

conversa9 = [
    "oie ",
    "cara isso é literalmente rotina da TI",
    "KKKKKKKKKKKKKK",
    "sistema sempre quebra no pior horário possível",

]

conversa10 = [
    "ooi ",
    "KKKKKKKKKKKKKK bem-vindo oficialmente à vida adulta cansada",
    "cara cancelamento de compromisso hoje parece presente",
    "SIMMMMM",

]



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
]

# =========================
# DIGITAÇÃO HUMANA
# =========================

def digitar(msg):
    pyautogui.write(
        msg,
        interval=random.uniform(0.035, 0.142)
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

        time.sleep(random.uniform(0.5, 0.6))

        pyautogui.click()

        digitar(conversas[j][i])

        pyautogui.press("enter")

        time.sleep(random.uniform(0.4, 0.6))

        print(f"Mensagem {i} enviada")

    # =========================
    # ORDENA OS WPP
    # =========================

    for bx, by in blocos:

        pyautogui.moveTo(bx, by, duration=0.2)

        time.sleep(random.uniform(0.1, 0.3))

        pyautogui.click()

print("Conversa finalizada.")