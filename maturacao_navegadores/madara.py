import  pygetwindow     as  gw
import  pyautogui       as  ag
import  keyboard        as  kb
import  random
import  time
import  os
import  sys

from    Assuntos   import  *
from    numeros_wpp         import  *

# =========================
# conta as janelas do chrome
# =========================

janelas_Chrome = [w for w in gw.getAllWindows() if "Chrome" in w.title]

num_jam_Chrome = len(janelas_Chrome)

print(f"encontradas {num_jam_Chrome} janelas")

janelas_Edge = [v for v in gw.getAllWindows() if "Edge" in v.title]

num_jam_Edge = len(janelas_Edge)

print(f"encontradas {num_jam_Edge} janelas")

num_jam_tot = num_jam_Chrome + num_jam_Edge

print(f"{num_jam_tot} janelas totais")



# =========================
# variaveis mutáveis
# =========================

TOTAL_MENSAGENS = 2
local_digitacao = (857, 1262)
temporizador = 12 #Cada unidade vale por 5 minutos 
Edge_1 = (15, 15)
Edge_2 = (15, 15)
Edge_3 = (15, 15)
wpp = numeros


# lista de assuntos
blocos = [
    assuntos_empresa,
    assuntos_universo,
    assuntos_livros,
    assuntos_comida,
    assuntos_social,
    assuntos_aleatorios,
]

# ========================================================
# PARAMETROS
# ========================================================


def digitar(msg):

    kb.write(
        msg,
        delay = random.uniform(0.090, 0.158) #pc lento do carai
    )


def apertar_tecla(tecla, vezes, intervalo=0.5):
    for _ in range(vezes):
        ag.press(tecla)
        time.sleep(intervalo)


def gerar_conversa(total_mensagens=None):
    if total_mensagens is None:
        total_mensagens = TOTAL_MENSAGENS

    conversa1 = []
    conversa2 = []

    while len(conversa1) < total_mensagens:
        bloco = random.choice(blocos)
        pergunta, resposta = random.choice(bloco)

        conversa1.append(pergunta)
        conversa2.append(resposta)

    return conversa1[:total_mensagens], conversa2[:total_mensagens]

# =========================================================
# GERADOR
# =========================================================

# gerar pares com total

pares = [(i, i+1) for i in range(1, num_jam_tot+1, 2)]

resultado = {}

# Luup para gerar as conversas

for a, b in pares:
    c1, c2 = gerar_conversa(TOTAL_MENSAGENS)

    resultado[f"conversa{a}"] = c1
    resultado[f"conversa{b}"] = c2


# =========================================================
# MOSTRAR EXEMPLO
# =========================================================

with open("conversas.py", "w", encoding="utf-8") as arquivo:

    for nome, conversa in resultado.items():

        arquivo.write(f"\n{nome} = [\n")

        for msg in conversa:
            arquivo.write(f'    "{msg}",\n')

        arquivo.write("]\n")

time.sleep(10)

# =======================================================
# lista de conversas
# =======================================================


conversas = [
    resultado[chave]
    for chave in sorted(resultado.keys(),
                        key=lambda x: int(x.replace("conversa", ""))
                        ) #lambidão kkkkkkkk
]


print("iniciando maturação em 5 segundos...")
time.sleep(5) # zzzzzzzzzzzzzzzzzzzzzzz "a mimir"


# ========================
# abre as janelas, maximiza, arruma tamanho e minimiza
# ========================

print("organizar janelas e abrir grupo em 5 segundos")
time.sleep(5)



for janela in   janelas_Edge:
    janela.activate()
    time.sleep(1)

    if  not janela.isMaximized:
        janela.maximize()
        time.sleep(2)

    ag.hotkey('ctrl', '0')
    time.sleep(2)

    janela.restore()
    time.sleep(1) # zzzzzz "a mimir"

    janela.minimize()

for janela in   janelas_Chrome:
    janela.activate()
    time.sleep(1)

    if  not janela.isMaximized:
        janela.maximize()
        time.sleep(2)

    ag.hotkey('ctrl', '0')
    time.sleep(2)

    janela.restore()
    time.sleep(1) # zzzzzz "a mimir"

    janela.minimize()


print("janelas organizadas")


# =======================================================
# LOOP PRINCIPAL
# =======================================================

quantidade_msgs = min(len(c) for c in conversas)


for i in range(quantidade_msgs):

    for j, janela in enumerate(reversed(janelas_Edge)):

        janela.restore()
        time.sleep(1)

        janela.activate()
        time.sleep(1) # zzzzzz "a mimir"

        if  not janela.isMaximized:
            janela.maximize()
            time.sleep(2)

        for envio   in  wpp:    #edge

            apertar_tecla('tab', 2, 0.5)
            time.sleep(2)

            ag.press('enter')
            time.sleep(2)

            apertar_tecla('tab', 4, 0.5)
            time.sleep(2)

            ag.press('enter')
            time.sleep(2)

            digitar(wpp[envio])
            time.sleep(2)

            ag.moveTo("_____________")
            time.sleep(2)

            ag.click()
            time.sleep(2)

            digitar(conversa[envio][janela])
            time.sleep(2)

            ag.press('enter')
            time.sleep(2)

            apertar_tecla('esc', 3, 0.5)
            
            ag.moveTo('_______________')
            ag.click()
            time.sleep(2)


        ag.hotkey('ctrl', 'f5')
        time.sleep(5)

        janela.restore()
        time.sleep(2)

        janela.minimize()

        time.sleep(1) # zzzzzz "a mimir"


        for j, janela in enumerate(reversed(janelas_Chrome)):

        janela.restore()    #tá com erro em 'janela', não sei pq
        time.sleep(1)

        janela.activate()
        time.sleep(1) # zzzzzz "a mimir"

        if  not janela.isMaximized:
            janela.maximize()
            time.sleep(2)

        for envio   in  wpp:    #edge

            apertar_tecla('tab', 2, 0.5)
            time.sleep(2)

            ag.press('enter')
            time.sleep(2)

            apertar_tecla('tab', 4, 0.5)
            time.sleep(2)

            ag.press('enter')
            time.sleep(2)

            digitar(wpp[envio])
            time.sleep(2)

            ag.moveTo("_____________")
            time.sleep(2)

            ag.click()
            time.sleep(2)

            digitar(conversa[envio][janela])
            time.sleep(2)

            ag.press('enter')
            time.sleep(2)

            apertar_tecla('esc', 3, 0.5)
            
            ag.moveTo('_______________')
            ag.click()
            time.sleep(2)


        ag.hotkey('ctrl', 'f5')
        time.sleep(5)

        janela.restore()
        time.sleep(2)

        janela.minimize()

        time.sleep(1) # zzzzzz "a mimir"
    




    
 