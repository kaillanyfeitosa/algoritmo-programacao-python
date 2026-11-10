import math


def area_triangulo(base, altura):
    return (base * altura) / 2


def area_retangulo(base, altura):
    return base * altura


def area_quadrado(lado):
    return lado ** 2


def area_trapezio(base_maior, base_menor, altura):
    return ((base_maior + base_menor) * altura) / 2


def area_losango(diagonal_maior, diagonal_menor):
    return (diagonal_maior * diagonal_menor) / 2


def area_circulo(raio):
    return math.pi * raio ** 2


def ler_numero(mensagem):
    """Lê um número positivo."""
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Valor inválido. Digite um número.")
            continue
        if valor > 0:
            return valor
        print("O valor deve ser maior que zero.")


def menu():
    print("\n=== Áreas de Figuras Planas ===")
    print("1 - Triângulo")
    print("2 - Retângulo")
    print("3 - Quadrado")
    print("4 - Trapézio")
    print("5 - Losango")
    print("6 - Círculo")
    print("0 - Sair")


def main():
    while True:
        menu()
        opcao = input("Escolha a figura: ").strip()

        if opcao == "0":
            print("Encerrando o programa.")
            break
        elif opcao == "1":
            b = ler_numero("Base: ")
            h = ler_numero("Altura: ")
            area = area_triangulo(b, h)
        elif opcao == "2":
            b = ler_numero("Base: ")
            h = ler_numero("Altura: ")
            area = area_retangulo(b, h)
        elif opcao == "3":
            lado = ler_numero("Lado: ")
            area = area_quadrado(lado)
        elif opcao == "4":
            B = ler_numero("Base maior: ")
            b = ler_numero("Base menor: ")
            h = ler_numero("Altura: ")
            area = area_trapezio(B, b, h)
        elif opcao == "5":
            D = ler_numero("Diagonal maior: ")
            d = ler_numero("Diagonal menor: ")
            area = area_losango(D, d)
        elif opcao == "6":
            r = ler_numero("Raio: ")
            area = area_circulo(r)
        else:
            print("Opção inválida.")
            continue

        print(f"Área = {area:.2f}")


main()
