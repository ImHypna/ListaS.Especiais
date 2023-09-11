import random

# Função para carregar as palavras do arquivo externo
def carregar_palavras(arquivo):
    with open(arquivo, 'r') as file:
        palavras = file.readlines()
    return [palavra.strip() for palavra in palavras]

# Função para escolher uma palavra aleatória da lista
def escolher_palavra(palavras):
    return random.choice(palavras)

# Função principal do jogo
def jogo_da_adivinhacao():
    palavras = carregar_palavras("termo/palavras.txt")
    palavra_secreta = escolher_palavra(palavras)
    letras_descobertas = ["_"] * len(palavra_secreta)
    tentativas = 6
    letras_usadas = []

    print("Bem-vindo ao Jogo da Adivinhação de Palavras!")
    
    while tentativas > 0:
        print("\nPalavra: " + " ".join(letras_descobertas))
        print("Letras usadas: " + ", ".join(letras_usadas))
        letra = input("Digite uma letra: ").lower()

        if letra in letras_usadas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if letra in palavra_secreta:
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == letra:
                    letras_descobertas[i] = letra
        else:
            tentativas -= 1
            print(f"Letra '{letra}' não está na palavra. Você tem {tentativas} tentativas restantes.")

        letras_usadas.append(letra)

        if "".join(letras_descobertas) == palavra_secreta:
            print("\nParabéns! Você adivinhou a palavra: " + palavra_secreta)
            break

    if "".join(letras_descobertas) != palavra_secreta:
        print("\nFim de jogo! A palavra era: " + palavra_secreta)

if __name__ == "__main__":
    jogo_da_adivinhacao()