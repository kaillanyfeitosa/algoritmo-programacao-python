import math


def calcular_delta(a, b, c):
    return b ** 2 - 4 * a * c


def calcular_raizes(a, b, c):
    """Retorna a lista de raízes reais distintas."""
    delta = calcular_delta(a, b, c)

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return [x1, x2]
    elif delta == 0:
        return [-b / (2 * a)]
    else:
        return []


def ler_coeficiente(nome):
    while True:
        try:
            return float(input(f"Digite o coeficiente {nome}: ").replace(",", "."))
        except ValueError:
            print("Valor inválido. Digite um número.")


def main():
    print("=== Equação do 2º grau: ax² + bx + c = 0 ===")

    while True:
        a = ler_coeficiente("a")
        if a != 0:
            break
        print("Em uma equação do 2º grau, 'a' não pode ser zero.")
    b = ler_coeficiente("b")
    c = ler_coeficiente("c")

    delta = calcular_delta(a, b, c)
    raizes = calcular_raizes(a, b, c)

    print(f"\nΔ = {delta:.2f}")
    print(f"Número de raízes reais distintas: {len(raizes)}")

    if len(raizes) == 2:
        print(f"x1 = {raizes[0]:.2f} e x2 = {raizes[1]:.2f}")
    elif len(raizes) == 1:
        print(f"x = {raizes[0]:.2f}")
    else:
        print("A equação não possui raízes reais (raízes complexas).")


main()
