

    # =======================================================
    # coordenadas do wpp
    # =======================================================







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