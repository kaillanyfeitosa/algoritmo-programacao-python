import modulo_senhas


def main():
    print("=== Verificador de Senhas ===")
    senha = input("Digite a senha a ser testada: ")

    valida, erros = modulo_senhas.verificar_senha(senha)

    if valida:
        print("Senha dentro do padrão da empresa!")
    else:
        print("Senha fora do padrão. Problemas encontrados:")
        for erro in erros:
            print(f"- {erro}")


main()
