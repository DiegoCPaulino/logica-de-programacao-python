import random

roleta = list(range(1, 37))
jogadores = []

def girarRoleta():
    return random.choice(roleta)

def cadastrarJogador():
    nome = input("\nDigite o nome do jogador: ")
    banca = float(input(f"Digite o valor inicial da banca de {nome}: R$ "))
    jogador = {
        "nome": nome,
        "banca": banca,
        "valorApostado": 0,
        "tipoAposta": "",
        "dadosAposta": {},
        "ganhoRodada": 0
    }
    jogadores.append(jogador)
    print(f"✅ Jogador {nome} foi cadastrado com sucesso!\n")

def apostar(jogador):
    print(f"\nJogador: {jogador['nome']} — Banca atual: R$ {jogador['banca']:.2f}")
    valor = float(input("Digite o valor a ser apostado: R$ "))

    while valor <= 0 or valor > jogador["banca"]:
        print("Valor inválido! Deve ser maior que 0 e menor ou igual à banca.")
        valor = float(input("Digite o valor a ser apostado: R$ "))

    jogador["valorApostado"] = valor
    jogador["banca"] -= valor

    print("\nTipos de aposta disponíveis:")
    print("1 - Única (paga 35x)")
    print("2 - Dupla (paga 17x)")
    print("3 - Rua (paga 11x)")
    print("4 - Six (paga 5x)")
    print("5 - Coluna (paga 2x)")
    print("6 - Dúzia (paga 2x)")
    print("7 - Par/Ímpar (paga 1x)")

    tipo = input("Escolha o tipo de aposta (1 a 7): ")

    if tipo == "1":
        numero = int(input("Digite o número da aposta única (1-36): "))
        jogador["tipoAposta"] = "unica"
        jogador["dadosAposta"] = {"numero": numero}

    elif tipo == "2":
        primeiro = int(input("Digite o primeiro número da aposta dupla: "))
        tipoVizinho = input("Horizontal ou Vertical (H/V): ").upper()
        jogador["tipoAposta"] = "dupla"
        jogador["dadosAposta"] = {"primeiro": primeiro, "tipoVizinho": tipoVizinho}

    elif tipo == "3":
        primeira = int(input("Digite o primeiro número da rua (linha de 3 números): "))
        jogador["tipoAposta"] = "rua"
        jogador["dadosAposta"] = {"primeiraCasa": primeira}

    elif tipo == "4":
        primeira = int(input("Digite o primeiro número da aposta six (linha de 6 números): "))
        jogador["tipoAposta"] = "six"
        jogador["dadosAposta"] = {"primeiraCasa": primeira}

    elif tipo == "5":
        coluna = input("Digite a coluna da aposta (1, 2 ou 3): ")
        jogador["tipoAposta"] = "coluna"
        jogador["dadosAposta"] = {"coluna": coluna}

    elif tipo == "6":
        duzia = input("Digite a dúzia da aposta (1 (1-12), 2 (13-24), 3 (25-36)): ")
        jogador["tipoAposta"] = "duzia"
        jogador["dadosAposta"] = {"duzia": duzia}

    elif tipo == "7":
        escolha = input("Digite sua escolha (P para Par, I para Ímpar): ").upper()
        jogador["tipoAposta"] = "parimpar"
        jogador["dadosAposta"] = {"escolha": escolha}

    else:
        print("Tipo de aposta inválido. Nenhuma aposta registrada.")
        jogador["tipoAposta"] = ""
        jogador["dadosAposta"] = {}

def analisarGanhos(numeroSorteado):
    print(f"\n🎰 Número sorteado: {numeroSorteado}\n")
    for jogador in jogadores:
        tipo = jogador["tipoAposta"]
        valor = jogador["valorApostado"]
        ganho = 0

        if tipo == "unica":
            if numeroSorteado == jogador["dadosAposta"]["numero"]:
                ganho = valor * 35

        elif tipo == "dupla":
            primeiro = jogador["dadosAposta"]["primeiro"]
            vizinho = jogador["dadosAposta"]["tipoVizinho"]
            if vizinho == "H":
                segundo = primeiro + 1 if primeiro % 3 != 0 else primeiro - 1
            else:
                segundo = primeiro + 3 if primeiro <= 33 else primeiro - 3
            if numeroSorteado in [primeiro, segundo]:
                ganho = valor * 17

        elif tipo == "rua":
            primeira = jogador["dadosAposta"]["primeiraCasa"]
            rua = [primeira, primeira + 1, primeira + 2]
            if numeroSorteado in rua:
                ganho = valor * 11

        elif tipo == "six":
            primeira = jogador["dadosAposta"]["primeiraCasa"]
            six = [primeira + i for i in range(6) if primeira + i <= 36]
            if numeroSorteado in six:
                ganho = valor * 5

        elif tipo == "coluna":
            coluna = jogador["dadosAposta"]["coluna"]
            if coluna == "1":
                numeros = list(range(1, 37, 3))
            elif coluna == "2":
                numeros = list(range(2, 37, 3))
            else:
                numeros = list(range(3, 37, 3))
            if numeroSorteado in numeros:
                ganho = valor * 2

        elif tipo == "duzia":
            duzia = jogador["dadosAposta"]["duzia"]
            if duzia == "1":
                numeros = range(1, 13)
            elif duzia == "2":
                numeros = range(13, 25)
            else:
                numeros = range(25, 37)
            if numeroSorteado in numeros:
                ganho = valor * 2

        elif tipo == "parimpar":
            escolha = jogador["dadosAposta"]["escolha"]
            if (escolha == "P" and numeroSorteado % 2 == 0) or (escolha == "I" and numeroSorteado % 2 != 0):
                ganho = valor

        if ganho > 0:
            jogador["banca"] += valor + ganho
            jogador["ganhoRodada"] = ganho
            print(f"💰 {jogador['nome']} ganhou R$ {ganho:.2f}! Nova banca: R$ {jogador['banca']:.2f}")
        else:
            jogador["ganhoRodada"] = 0
            print(f"❌ {jogador['nome']} perdeu! Nova banca: R$ {jogador['banca']:.2f}")

    print("\n=== Fim da rodada ===")
    for jogador in jogadores:
        print(f"{jogador['nome']} — Banca atual: R$ {jogador['banca']:.2f}")

    for jogador in jogadores:
        jogador["tipoAposta"] = ""
        jogador["dadosAposta"] = {}
        jogador["valorApostado"] = 0

def iniciarJogo():
    print("=== 🎡 JOGO DA ROLETA ===")
    qtdJogadores = int(input("Quantos jogadores irão participar? "))

    for i in range(qtdJogadores):
        cadastrarJogador()

    continuar = True
    while continuar:
        numeroSorteado = girarRoleta()
        for jogador in jogadores:
            if jogador["banca"] > 0:
                apostar(jogador)
            else:
                print(f"⚠️ O jogador(a) <{jogador['nome']}> zerou a banca e não pode mais jogar.")
        analisarGanhos(numeroSorteado)

        escolha = input("\nDeseja jogar novamente (J), adicionar novo jogador (A) ou sair (S)? ").upper()
        if escolha == "A":
            cadastrarJogador()
        elif escolha == "S":
            continuar = False
            print("\nEncerrando o jogo! Até a próxima...")

iniciarJogo()