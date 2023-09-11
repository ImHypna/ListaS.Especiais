def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 15)

def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas e colunas
    for i in range(4):
        if all([tabuleiro[i][j] == jogador for j in range(4)]) or all([tabuleiro[j][i] == jogador for j in range(4)]):
            return True
    # Verificar diagonais
    if all([tabuleiro[i][i] == jogador for i in range(4)]) or all([tabuleiro[i][3 - i] == jogador for i in range(4)]):
        return True
    return False

def jogar_jogo_da_velha():
    tabuleiro = [[" " for _ in range(4)] for _ in range(4)]
    jogador_atual = "X"
    jogadas = 0

    while True:
        imprimir_tabuleiro(tabuleiro)
        print(f"Vez do jogador {jogador_atual}")
        linha = int(input("Digite o número da linha (0 até 3): "))
        coluna = int(input("Digite o número da coluna (0 até 3): "))

        if linha < 0 or linha > 3 or coluna < 0 or coluna > 3 or tabuleiro[linha][coluna] != " ":
            print("Jogada inválida. Tente novamente.")
            continue

        tabuleiro[linha][coluna] = jogador_atual
        jogadas += 1

        if verificar_vitoria(tabuleiro, jogador_atual):
            imprimir_tabuleiro(tabuleiro)
            print(f"Jogador {jogador_atual} venceu!")
            break
        elif jogadas == 16:
            imprimir_tabuleiro(tabuleiro)
            print("O jogo terminou em empate!")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"

if __name__ == "__main__":
    jogar_jogo_da_velha()
