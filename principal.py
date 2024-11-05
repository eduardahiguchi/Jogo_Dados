import random

META_PONTOS = 100

def configurar_jogadores():
    num_jogadores = int(input("Quantos jogadores? (1 ou 2): "))
    jogadores = {}

    nome_jogador1 = input("Insira o nome do Jogador 1: ")
    jogadores["Jogador 1"] = {"nome": nome_jogador1, "pontuacao": 0, "rodadas": []}

    if num_jogadores == 2:
        nome_jogador2 = input("Insira o nome do Jogador 2: ")
        jogadores["Jogador 2"] = {"nome": nome_jogador2, "pontuacao": 0, "rodadas": []}
    else:
        jogadores["Computador"] = {"nome": "Computador", "pontuacao": 0, "rodadas": []}

    return jogadores

def lancar_dado(lados):
    return random.randint(1, lados)

def jogar_rodada(jogador):
    print(f"\nÉ a vez de {jogador['nome']}!")
    pontuacao_rodada = 0

    dado1 = lancar_dado(6)
    dado2 = lancar_dado(10)
    print(f"{jogador['nome']} lançou {dado1} e {dado2}.")

    if dado1 == 1 or dado2 == 1:
        print(f"{jogador['nome']} tirou um 1 e perdeu todos os pontos desta rodada.")
        return 0

    pontuacao_rodada += dado1 + dado2

    if pontuacao_rodada == 7:
        dado_bonus = lancar_dado(10)
        pontuacao_rodada += dado_bonus
        print(f"Soma foi 7! {jogador['nome']} lançou o dado de 10 lados novamente e tirou {dado_bonus}.")

    print(f"Pontos nesta rodada para {jogador['nome']}: {pontuacao_rodada}")
    return pontuacao_rodada

def jogar(jogadores):
    turno = 0

    while True:
        nome_jogador = list(jogadores.keys())[turno % len(jogadores)]
        jogador = jogadores[nome_jogador]

        pontos_rodada = jogar_rodada(jogador)
        jogador["rodadas"].append(pontos_rodada)
        jogador["pontuacao"] += pontos_rodada

        print(f"Pontuação total de {jogador['nome']}: {jogador['pontuacao']}")

        if jogador["pontuacao"] >= META_PONTOS:
            print(f"\n{jogador['nome']} venceu o jogo com {jogador['pontuacao']} pontos!")
            break

        turno += 1

def iniciar_jogo():
    print("Bem-vindo ao jogo de dados!")
    jogadores = configurar_jogadores()
    jogar(jogadores)

iniciar_jogo()