import random


def ler_palpite():
    """Lê um palpite válido (inteiro de 1 a 100)."""
    while True:
        try:
            palpite = int(input("Seu palpite (1 a 100): "))
        except ValueError:
            print("Digite apenas números inteiros.")
            continue
        if 1 <= palpite <= 100:
            return palpite
        print("O número deve estar entre 1 e 100.")


def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    palpites = []

    print("=== Jogo de Adivinhação ===")
    print("Pensei em um número de 1 a 100. Tente adivinhar!")

    while True:
        palpite = ler_palpite()
        palpites.append(palpite)

        if palpite == numero_secreto:
            print("\nParabéns, você acertou!")
            print(f"Palpites digitados: {palpites}")
            print(f"Quantidade de tentativas: {len(palpites)}")
            break
        elif palpite < numero_secreto:
            print("Você errou! Dica: o número secreto é MAIOR.")
        else:
            print("Você errou! Dica: o número secreto é MENOR.")


jogo_adivinhacao()
