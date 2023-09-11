def imprimir_tabuleiro(tabuleiro):
    n = len(tabuleiro)
    for i in range(n):
        for j in range(n):
            print(tabuleiro[i][j], end=" ")
            if j < n - 1:
                print("|", end=" ")
        print()
        if i < n - 1:
            print("-" * (4 * n - 1))

def verificar_vitoria(tabuleiro, jogador):
    n = len(tabuleiro)

    # Verificar linhas e colunas
    for i in range(n):
        if all([tabuleiro[i][j] == jogador for j in range(n)]) or all([tabuleiro[j][i] == jogador for j in range(n)]):
            return True

    # Verificar diagonais
    if all([tabuleiro[i][i] == jogador for i in range(n)]) or all([tabuleiro[i][n - 1 - i] == jogador for i in range(n)]):
        return True

    return False

def jogar_jogo_da_velha():
    tamanho_tabuleiro = int(input("Digite o tamanho do tabuleiro (quadrado): "))
    tabuleiro = [[" " for _ in range(tamanho_tabuleiro)] for _ in range(tamanho_tabuleiro)]
    jogador_atual = "X"
    jogadas = 0
    max_jogadas = tamanho_tabuleiro * tamanho_tabuleiro

    while True:
        imprimir_tabuleiro(tabuleiro)
        print(f"Vez do jogador {jogador_atual}")
        linha = int(input(f"Digite o número da linha (0 a {tamanho_tabuleiro - 1}): "))
        coluna = int(input(f"Digite o número da coluna (0 a {tamanho_tabuleiro - 1}): "))

        if (
            linha < 0
            or linha >= tamanho_tabuleiro
            or coluna < 0
            or coluna >= tamanho_tabuleiro
            or tabuleiro[linha][coluna] != " "
        ):
            print("Jogada inválida. Tente novamente.")
            continue

        tabuleiro[linha][coluna] = jogador_atual
        jogadas += 1

        if verificar_vitoria(tabuleiro, jogador_atual):
            imprimir_tabuleiro(tabuleiro)
            print(f"Jogador {jogador_atual} venceu!")
            break
        elif jogadas == max_jogadas:
            imprimir_tabuleiro(tabuleiro)
            print("O jogo terminou em empate!")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"

if __name__ == "__main__":
    jogar_jogo_da_velha()