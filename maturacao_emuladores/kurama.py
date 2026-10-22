import  pygetwindow     as  gw
import  pyautogui       as  ag
import  keyboard        as  kb
import  random
import  time
import  os
import  sys

from    conversas   import  *
from    Assuntos    import  *

for l in range(5):

    # =========================
    # variaveis mutáveis
    # =========================

    TOTAL_MENSAGENS = 5
    local_digitacao = (857, 1262)
    temporizador = 12 #Cada unidade vale por 5 minutos 

    # lista de assuntos
    blocos = [
        assuntos_empresa,
        assuntos_universo,
        assuntos_livros,
        assuntos_comida,
        assuntos_social,
        assuntos_aleatorios,
    ]

    # =========================
    # conta as janelas do chrome
    # =========================

    janelas = [w for w in gw.getAllWindows() if "Chrome" in w.title]

    num_jam = len(janelas)

    print(f"encontradas {num_jam} janelas")


    # ========================================================
    # VELOCIDADE DE DIGITAÇÃO
    # ========================================================


    def digitar(msg):

        kb.write(
            msg,
            delay = random.uniform(0.090, 0.158) #pc lento do carai
        )


    # ========================
    # abre as janelas, maximiza, arruma tamanho e minimiza
    # ========================

    print("organizar janelas e abrir grupo em 5 segundos")
    time.sleep(5)


    for janela in   janelas:
        janela.activate()
        time.sleep(1)

        if  not janela.isMaximized:
            janela.maximize()
            time.sleep(2)

        ag.hotkey('ctrl', '0')
        time.sleep(2)

        ag.moveTo (167, 174)
        time.sleep(1)
        ag.click()
        time.sleep(1)
        
        ag.moveTo (165, 175)
        time.sleep(1)
        ag.click()
        time.sleep(1)
        
        digitar(f"Projeto e25 {l}")
        time.sleep(2)
        ag.press("enter")
        time.sleep(1)

        digitar(
            random.choice([
                "oii",
                "bom diaaa",
                "fala meu povo",
                "cheguei carai kkkkk",
                "começa logo isso ksksksks",
                "e aí pessoal",
                "todo mundo online?",
            ])
        )
        time.sleep (1)
        ag.press("enter")
        time.sleep(1)
        
        janela.restore()
        time.sleep(1) # zzzzzz "a mimir"

        janela.minimize()

        
    print("janelas organizadas")


    # =========================================================
    # GERADOR



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

    # gerar pares com total

    pares = [(i, i+1) for i in range(1, num_jam+1, 2)]

    resultado = {}

    # Luup para gerar as conversas

    for a, b in pares:
        c1, c2 = gerar_conversa(TOTAL_MENSAGENS)

        resultado[f"conversa{a}"] = c1
        resultado[f"conversa{b}"] = c2


    # =========================================================
    # MOSTRAR EXEMPLO


    with open("conversas.py", "w", encoding="utf-8") as arquivo:

        for nome, conversa in resultado.items():

            arquivo.write(f"\n{nome} = [\n")

            for msg in conversa:
                arquivo.write(f'    "{msg}",\n')

            arquivo.write("]\n")

    time.sleep(10)

    # =======================================================
    # coordenadas do wpp
    # =======================================================



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




    # =======================================================
    # LOOP PRINCIPAL
    # =======================================================

    quantidade_msgs = min(len(c) for c in conversas)


    for i in range(quantidade_msgs):

        for j, janela in enumerate(reversed(janelas)):

            janela.restore()
            time.sleep(1)

            janela.activate()
            time.sleep(1) # zzzzzz "a mimir"

            if  not janela.isMaximized:
                janela.maximize()
                time.sleep(2)

            ag.moveTo(943 , 1268)
            ag.click()
            time.sleep(1)

            ag.moveTo(1321, 1266)
            ag.click()
            time.sleep(2)

            digitar(conversas[j][i])
            time.sleep(1) # zzzzzz "a mimir"

            ag.press("enter")
            time.sleep(1) # zzzzzz "a mimir"

            janela.restore()
            time.sleep(2)

            janela.minimize()

            time.sleep(1) # zzzzzz "a mimir"
        
        print(f"msg {i} enviada")

        


    for k, janela in enumerate(janelas):
        janela.activate()
        time.sleep(1)

        if  not janela.isMaximized:
            janela.maximize()
            time.sleep(2)
        
        ag.hotkey('ctrl'+ 'f5')

        janela.restore()
        

        '''
        x = k * 15
        y = k * 20

        janela.moveTo(x, y)
        time.sleep(1)
        '''
        

    print("finalizado, iniciando temporizador de 1 hora")



    for l in range(temporizador):
        x = l*5
        y = (temporizador*5) - x

        print(f"{x} minutos passados.")
        print(f"O tempo será reiniciado em {y} minutos")

        time.sleep(5*60)
    
os.execv(sys.executable, [sys.executable] + sys.argv)