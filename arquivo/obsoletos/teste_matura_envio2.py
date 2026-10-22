import pyautogui
import time
import random
import keyboard

from conversas8 import *
from numeros_wpp import *
from mensagens_clientes import *

# =========================
#   COORDENADAS DA BARRA DE TEXTO DO WPP - passa para a próxima janela E já permite enviar mensagem
# =========================

wpps = [
    (1720, 323),    # WPP 1
    (1726, 358),   # WPP 2
    (1723, 393),   # WPP 3
    (1729, 428),   # WPP 4
    (1721, 469),   # WPP 5
    (1725, 504),   # WPP 6
]

# =========================
#   POSIÇÕES DE ORDENAÇÃO - reorganiza as janelas
# =========================

blocos = [
    (1699, 160), # bloco 5
    (1701, 121), # bloco 4
    (1702, 80), # bloco 3
    (1696, 56), # bloco 2
    (1703, 19), # bloco 1
]


# =========================
#   BARRAS DE PESQUISA - para pesquisar contatos específicos já salvos no wpp
# =========================

barras_pesquisa = [

    (1491, 131), # WPP 1
    (1535, 167), # WPP 2
    (1464, 199), # WPP 3
    (1445, 230), # WPP 4
    (1535, 261), # WPP 5
    (1494, 302), # WPP 6

]

# =========================
#   ACESSAR NUMEROS DOS CLIENTES - serve para clicar no ultimo número de cliente e 
# abrir a caixa de "iniciar conversa" 
# =========================

localizacao_numeros = [

    (1769, 294), # WPP 1
    (1769, 331), # WPP 2
    (1762, 362), # WPP 3
    (1762, 391), # WPP 1
    (1788, 428), # WPP 2
    (1765, 463), # WPP 3

]

# =========================
# BOTÕES INICIAR CONVERSA - clica na caixa de "iniciar conversa" aberta anteriormente
# =========================

botoes_iniciar = [

    (1670, 256), # WPP 1
    (1668, 295), # WPP 2
    (1655, 325), # WPP 3
    (1628, 354), # WPP 1
    (1724, 392), # WPP 2
    (1656, 422), # WPP 3

]

# =========================
# CONVERSAS - conversas pré setadas abertas em um arquivo.py
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
# DIGITAÇÃO HUMANA
# =========================

def digitar(msg):

    keyboard.write(
        msg,
        delay=random.uniform(0.042, 0.142)
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
    # ENVIA PARA AMIGOS NO WPP
    # =========================

    for j in range(len(wpps)):

        x, y = wpps[j]      #BARRA DE DIGITAÇÃO

        pyautogui.moveTo(x, y, duration=1)

        time.sleep(random.uniform(0.5, 0.6))

        pyautogui.click()

        digitar(conversas[j][i])    #COMEÇA A DIGITAR

        pyautogui.press("enter")

        time.sleep(random.uniform(0.4, 0.6))

        

    # =========================
    # ORDENA OS WPP
    # =========================

    for bx, by in blocos:

        pyautogui.moveTo(bx, by, duration=0.2)

        time.sleep(random.uniform(0.1, 0.3))

        pyautogui.click()

    # =========================
    # LOOP DOS NÚMEROS
    # =========================

    for j in range(len(wpps)):

        numero = numeros[(i + j) % len(numeros)]

        mensagem_numero = mensagens_numeros[(i + j) % len(mensagens_numeros)]

        # CLICA NO WPP

        x, y = wpps[j]

        pyautogui.moveTo(x, y, duration=0.5)

        time.sleep(random.uniform(0.3, 0.5))

        pyautogui.click()

        # ABRE PESQUISA

        px, py = barras_pesquisa[j]

        pyautogui.moveTo(px, py, duration=0.5)

        pyautogui.click()

        time.sleep(random.uniform(0.3, 0.5))

        # DIGITA O NÚMERO

        digitar(numero)

        time.sleep(random.uniform(0.5, 0.8))

        pyautogui.press("enter")

        time.sleep(random.uniform(0.5, 0.8))

        # CLICA EM INICIAR CONVERSA

        ix, iy = botoes_iniciar[j]

        pyautogui.moveTo(ix, iy, duration=0.5)

        pyautogui.click()

        time.sleep(random.uniform(0.5, 0.8))

        # ENVIA MENSAGEM

        digitar(mensagem_numero)

        pyautogui.press("enter")

        time.sleep(random.uniform(0.4, 0.7))
    
    # =========================
    # REORGANIZA NOVAMENTE
    # =========================

    for bx, by in blocos:

        pyautogui.moveTo(bx, by, duration=0.2)

        time.sleep(random.uniform(0.1, 0.3))

        pyautogui.click()

    print(f"Mensagem {i} enviada")

print("Conversa finalizada.")