import time
from colorama import Fore, Back, init
init(autoreset=True)
personagens = {"Mago": {"cura": 10, "dano": 15, "vida": 50, "escudo": 7}, 
"Guerreiro":{"dano": 17, "cura": 15, "vida": 50, "escudo": 15}, 
"Arqueiro": {"dano": 20, "escudo": 5, "cura": 6, "vida": 50}}
def ver_cartas():
    print(Fore.WHITE + Back.GREEN + "---- Observatorio ----")
    for linha in personagens.keys():
        print(f"- {linha}")
def ver_atributos():
  
    for linha in personagens.keys():
        print(f"- {linha}")
    jogador = input("Digite o nome do personagem e veja os atributos: ").title().strip()
    if jogador in personagens:
        print(Fore.BLACK + Back.YELLOW + "---- Atributos ----")
        print(f"Vida de {jogador}: {personagens[jogador]['vida']}")
        print(f"Dano de {jogador}: {personagens[jogador]['dano']}")
        print(f"Escudo de {jogador}: {personagens[jogador]['escudo']}")
        print(f"Cura de {jogador}: {personagens[jogador]['cura']}\n")
    else:
        print("Esse personagem não existe!")
def escolher():
    print(Fore.WHITE + Back.BLUE + "==== Deck de batalha ====")
    for linha in personagens.keys():
        print(f"- {linha}")
    jgd1 = input("Escolha seu Heroi: ").title().strip()
    jgd2 = input("Escolha seu Heroi: ").title().strip()
    if jgd1 in personagens and jgd2 in personagens:
        print(Fore.BLACK + Back.YELLOW + f"-------- {jgd1} --------")
        print(f"Cura: {personagens[jgd1]['cura']}")
        print(f"Dano: {personagens[jgd1]['dano']}")
        print(f"Escudo: {personagens[jgd1]['escudo']}")
        print(f"vida: {personagens[jgd1]['vida']}")
        print(Fore.BLACK + Back.YELLOW + f"======== {jgd2} ========")
        print(f"Cura: {personagens[jgd2]['cura']}")
        print(f"Dano: {personagens[jgd2]['dano']}")
        print(f"Escudo: {personagens[jgd2]['escudo']}")
        print(f"vida: {personagens[jgd2]['vida']}\n")
        if jgd1 in personagens and jgd2 in personagens:
            try:            
                batalha(jgd1, jgd2)
            except KeyboardInterrupt:
                print(Fore.BLACK + Back.YELLOW + "Jogo encerrado pelo usuario... ")
                exit()
def batalha(cm1, cm2):
    
    vida1 = personagens[cm1]['vida']
    vida2 = personagens[cm2]['vida']            
    print(Fore.WHITE + Back.BLUE +"><><><><><> Batalha nas masmorras <><><><><>\n")
    while vida1 > 0 and vida2 > 0:
        print(Fore.BLACK + Back.YELLOW + "Ataques e Defesas monte sua estrategia: (dano, escudo, cura, vida)")
        print(Fore.BLACK + Back.BLUE + f"{cm1} x {cm2}")   
        escolha1 = input("JOGADOR 1 - Escolha o tipo de ataque que deseja usar: \n")
        if escolha1 == "dano":
            vida2 -= personagens[cm1]['dano']
            print(f"{cm2} perdeu {vida2} de vida para {cm1}\n")
            time.sleep(0.5)
        elif escolha1 == "escudo":
            vida1 += personagens[cm1]['escudo']
            print(f"{cm1} defendeu o ataque e ficou com {vida1} de vida\n")
            time.sleep(0.5)
        elif escolha1 == "cura":
            vida1 += personagens[cm1]['cura']
            print(f"Jogador 1 curou {vida1} de vida de seu {cm1}\n")
            time.sleep(0.5)
        if vida1 <= 0:
            print(f"Você perdeu para o jogador2 com seu {cm2}!\n")
            print(f"=====Fim de jogo=====")
            print(f"vencedor: jogador 1 com seu heroi {cm1} chupa! jogador 2")
            break
    
        escolha2 = input("JOGADOR 2 - Digite sua escolha: \n")
        if escolha2 == "dano":
            vida1 -= personagens[cm2]['dano']
            print(f"Jgador 1 perdeu {vida1} de vida para jogador 2\n")
            time.sleep(0.5)
        elif escolha2 == "escudo":
            vida2 += personagens[cm2]['escudo']
            print(f"{cm2} defendeu o ataque e ficou com {vida2} de vida\n")
            time.sleep(0.5)
        elif escolha2 == "cura":
            vida2 += personagens[cm2]['cura']
            print(f"Jogador 2 usou cura vida atual {vida2}\n")
            time.sleep(0.5)
        if vida2 <= 0:
            print(Fore.RED + Back.BLACK + f"Você perdeu para o jogador1 com seu {cm1}!\n")
            print(f"=====Fim de jogo=====")
            print(f"vencedor: jogador 2 com seu heroi {cm2}")
            break
while True:
    print(Fore.YELLOW + Back.BLACK + "1 - ver cartas")
    print(Fore.YELLOW + Back.BLACK + "2 - ver atributos")
    print(Fore.YELLOW + Back.BLACK + "3 - escolher e batalhar\n")
    try:
        acao = int(input("Digite oque deseja: "))
        if acao == 1:
            ver_cartas()
        elif acao == 2:
            ver_atributos()
        elif acao == 3:
            escolher()
    except ValueError:
        print("Digite apenas numeros")
    except KeyboardInterrupt:
        print(Fore.BLACK + Back.YELLOW + "Jogo encerrado pelo usuario... ")
        exit()
