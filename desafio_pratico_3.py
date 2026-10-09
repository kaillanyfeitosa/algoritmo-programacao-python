# Desafio Prático 3 - Lógica, Algoritmos e Programação
# Curso Superior de Tecnologia em Banco de Dados - 1º Período

from math import gcd


# ---------------------------------------------------------------
# QUESTÃO 1
# ---------------------------------------------------------------
'''
1. Faça um programa em Python que receba 10 idades, calcule e exiba:
a) a média das idades;
b) a mediana;
c) a moda.
'''


def calcular_media(idades):
    return sum(idades) / len(idades)


def calcular_mediana(idades):
    ordenadas = sorted(idades)  # a mediana precisa da lista em ordem
    n = len(ordenadas)
    meio = n // 2

    if n % 2 == 0:
        # quantidade par: média dos dois do meio
        return (ordenadas[meio - 1] + ordenadas[meio]) / 2
    else:
        return ordenadas[meio]


def calcular_moda(idades):
    maior_repeticao = 0
    modas = []

    for idade in idades:
        repeticoes = idades.count(idade)
        if repeticoes > maior_repeticao:
            maior_repeticao = repeticoes
            modas = [idade]
        elif repeticoes == maior_repeticao and idade not in modas:
            modas.append(idade)

    # se ninguém repete, não tem moda
    if maior_repeticao == 1:
        return []
    return modas


def questao_1():
    idades = []
    for i in range(10):
        idade = int(input(f"Digite a idade {i + 1}: "))
        idades.append(idade)

    print(f"\na) Média das idades: {calcular_media(idades):.2f}")
    print(f"b) Mediana: {calcular_mediana(idades)}")

    modas = calcular_moda(idades)
    if len(modas) == 0:
        print("c) Moda: não existe moda (nenhuma idade se repete)")
    else:
        print(f"c) Moda: {modas}")


# ---------------------------------------------------------------
# QUESTÃO 2
# ---------------------------------------------------------------
'''
2. Uma caixa contém:

bolas = ["vermelha", "azul", "verde", "vermelha", "amarela", "azul", "vermelha",
"verde", "azul", "vermelha"]

Considerando que uma bola será escolhida ao acaso, crie um programa que:
a) conte quantas bolas existem na caixa;
b) conte quantas são vermelhas;
c) calcule a probabilidade de escolher uma bola vermelha;
d) apresente a probabilidade em forma de fração e porcentagem.
'''


def contar_bolas(bolas):
    return len(bolas)


def contar_vermelhas(bolas):
    return bolas.count("vermelha")


def calcular_probabilidade(vermelhas, total):
    return vermelhas / total


def simplificar_fracao(numerador, denominador):
    divisor = gcd(numerador, denominador)
    return numerador // divisor, denominador // divisor


def questao_2():
    bolas = ["vermelha", "azul", "verde", "vermelha", "amarela", "azul",
             "vermelha", "verde", "azul", "vermelha"]

    total = contar_bolas(bolas)
    vermelhas = contar_vermelhas(bolas)
    probabilidade = calcular_probabilidade(vermelhas, total)
    num, den = simplificar_fracao(vermelhas, total)

    print(f"a) Quantidade de bolas na caixa: {total}")
    print(f"b) Quantidade de bolas vermelhas: {vermelhas}")
    print(f"c) Probabilidade de sortear uma vermelha: {probabilidade}")
    print(f"d) Em fração: {vermelhas}/{total} (simplificando: {num}/{den})")
    print(f"   Em porcentagem: {probabilidade * 100:.0f}%")


# ---------------------------------------------------------------
# QUESTÃO 3
# ---------------------------------------------------------------
'''
3. Uma escola deseja armazenar as notas de seus alunos utilizando uma lista dentro
de outra lista. Cada lista interna representa um aluno e contém suas três notas
obtidas durante o semestre.
Considere a seguinte estrutura:

alunos = [
   ["Ana", 7.5, 8.0, 9.0],
   ["Bruno", 6.0, 5.5, 7.0],
   ["Carlos", 9.0, 8.5, 10.0],
   ["Daniela", 5.0, 6.0, 4.5],
   ["Eduardo", 8.0, 7.5, 6.5]
]

Cada elemento da lista alunos possui a seguinte estrutura:

[nome, nota1, nota2, nota3]

Sua tarefa é criar um programa em Python que percorra essa lista e apresente um
relatório contendo:
a) O nome de cada aluno;
b) A média das três notas de cada aluno;
c) Se o aluno está aprovado ou reprovado, considerando que a média mínima
para aprovação é 7,0;
d) a média geral da turma;
e) o nome do aluno com a maior média;
f) o nome do aluno com a menor média;
g) quantos alunos foram aprovados;
h) quantos alunos foram reprovados.
'''


def media_do_aluno(aluno):
    # aluno = [nome, nota1, nota2, nota3]
    return (aluno[1] + aluno[2] + aluno[3]) / 3


def situacao_do_aluno(media):
    if media >= 7.0:
        return "Aprovado"
    else:
        return "Reprovado"


def questao_3():
    alunos = [
        ["Ana", 7.5, 8.0, 9.0],
        ["Bruno", 6.0, 5.5, 7.0],
        ["Carlos", 9.0, 8.5, 10.0],
        ["Daniela", 5.0, 6.0, 4.5],
        ["Eduardo", 8.0, 7.5, 6.5]
    ]

    soma_medias = 0
    aprovados = 0
    reprovados = 0

    # começo com o primeiro aluno para comparar com os outros
    maior_media = media_do_aluno(alunos[0])
    nome_maior = alunos[0][0]
    menor_media = media_do_aluno(alunos[0])
    nome_menor = alunos[0][0]

    print("===== RELATÓRIO DA TURMA =====")
    for aluno in alunos:
        nome = aluno[0]
        media = media_do_aluno(aluno)
        situacao = situacao_do_aluno(media)

        print(f"Aluno: {nome} | Média: {media:.2f} | Situação: {situacao}")

        soma_medias += media

        if situacao == "Aprovado":
            aprovados += 1
        else:
            reprovados += 1

        if media > maior_media:
            maior_media = media
            nome_maior = nome
        if media < menor_media:
            menor_media = media
            nome_menor = nome

    media_geral = soma_medias / len(alunos)

    print("------------------------------")
    print(f"Média geral da turma: {media_geral:.2f}")
    print(f"Aluno com a maior média: {nome_maior} ({maior_media:.2f})")
    print(f"Aluno com a menor média: {nome_menor} ({menor_media:.2f})")
    print(f"Alunos aprovados: {aprovados}")
    print(f"Alunos reprovados: {reprovados}")


# ---------------------------------------------------------------
# QUESTÃO 4
# ---------------------------------------------------------------
'''
4. Uma empresa possui uma lista com os preços de alguns produtos. Antes de
apresentar os valores ao cliente, todos os preços precisam receber um acréscimo de
10%.

O programador inicialmente escreveu o código da seguinte maneira:

precos = [50, 80, 120, 35, 200, 75]
novos_precos = []
for preco in precos:
   novo_preco = preco * 1.10
   novos_precos.append(novo_preco)
print(novos_precos)

O código funciona corretamente, mas a equipe deseja torná-lo mais compacto e
utilizar List Comprehension. Sua tarefa é reescrever o programa utilizando List
Comprehension
'''


def aplicar_acrescimo(precos):
    # round para não aparecer coisas tipo 55.00000000000001
    return [round(preco * 1.10, 2) for preco in precos]


def questao_4():
    precos = [50, 80, 120, 35, 200, 75]
    novos_precos = aplicar_acrescimo(precos)
    print("Preços originais:", precos)
    print("Preços com 10% de acréscimo:", novos_precos)


# ---------------------------------------------------------------
# QUESTÃO 5
# ---------------------------------------------------------------
'''
5. Um estacionamento cobra seus clientes de acordo com o tempo que o veículo
permaneceu no local:
Tempo de permanência      Valor
Até 1 hora                R$ 5,00
De 1 a 3 horas            R$ 10,00
De 3 a 5 horas            R$ 15,00
Mais de 5 horas           R$ 20,00

Crie um código (principal) que receba as informações relevantes para a situação.
Crie uma função para o cálculo do valor final do estacioamento.
'''


def calcular_valor_estacionamento(horas):
    if horas <= 1:
        return 5.00
    elif horas <= 3:
        return 10.00
    elif horas <= 5:
        return 15.00
    else:
        return 20.00


def questao_5():
    horas = float(input("Quantas horas o veículo ficou no estacionamento? ").replace(",", "."))

    if horas < 0:
        print("Tempo inválido!")
        return

    valor = calcular_valor_estacionamento(horas)
    print(f"Valor a pagar: R$ {valor:.2f}")


# ---------------------------------------------------------------
# QUESTÃO 6
# ---------------------------------------------------------------
'''
6. Um sistema de cadastro precisa calcular a idade de uma pessoa a partir do seu
ano de nascimento e do ano atual. Para isso você deve criar uma função. A função
deve receber os dois anos e retornar a idade da pessoa.
Desafio: faça o programa informar se a pessoa é:
 • menor de idade;
 • maior de idade.
'''


def calcular_idade(ano_nascimento, ano_atual):
    return ano_atual - ano_nascimento


def questao_6():
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    ano_atual = int(input("Digite o ano atual: "))

    idade = calcular_idade(ano_nascimento, ano_atual)

    if idade < 0:
        print("O ano de nascimento não pode ser maior que o ano atual!")
        return

    print(f"A pessoa tem {idade} anos.")

    # desafio
    if idade >= 18:
        print("Maior de idade.")
    else:
        print("Menor de idade.")


# ---------------------------------------------------------------
# QUESTÃO 7
# ---------------------------------------------------------------
'''
7. Uma empresa de construção precisa calcular rapidamente a área de diferentes
figuras geométricas. Crie três funções para a área do triângulo, área do trapézio e
área do losango.
'''


def area_triangulo(base, altura):
    return (base * altura) / 2


def area_trapezio(base_maior, base_menor, altura):
    return ((base_maior + base_menor) * altura) / 2


def area_losango(diagonal_maior, diagonal_menor):
    return (diagonal_maior * diagonal_menor) / 2


def questao_7():
    print("1 - Triângulo")
    print("2 - Trapézio")
    print("3 - Losango")
    figura = input("Escolha a figura: ")

    if figura == "1":
        base = float(input("Base: "))
        altura = float(input("Altura: "))
        print(f"Área do triângulo: {area_triangulo(base, altura):.2f}")
    elif figura == "2":
        base_maior = float(input("Base maior: "))
        base_menor = float(input("Base menor: "))
        altura = float(input("Altura: "))
        print(f"Área do trapézio: {area_trapezio(base_maior, base_menor, altura):.2f}")
    elif figura == "3":
        d_maior = float(input("Diagonal maior: "))
        d_menor = float(input("Diagonal menor: "))
        print(f"Área do losango: {area_losango(d_maior, d_menor):.2f}")
    else:
        print("Opção inválida!")


# ---------------------------------------------------------------
# QUESTÃO 8
# ---------------------------------------------------------------
'''
8. Um sistema precisa verificar se uma senha atende a uma regra básica de
segurança. Crie uma função que receba uma senha e retorne:
 • True se a senha possuir pelo menos 8 caracteres;
 • False caso contrário.

Desafio: modifique a função para exigir também que a senha contenha pelo menos
um número.
'''


def verificar_senha(senha):
    if len(senha) >= 8:
        return True
    else:
        return False


# versão do desafio: 8 caracteres + pelo menos um número
def verificar_senha_desafio(senha):
    tem_numero = False
    for caractere in senha:
        if caractere.isdigit():
            tem_numero = True

    if len(senha) >= 8 and tem_numero:
        return True
    else:
        return False


def questao_8():
    senha = input("Digite uma senha: ")

    print("Regra básica (mínimo 8 caracteres):", verificar_senha(senha))
    print("Desafio (8 caracteres + um número):", verificar_senha_desafio(senha))


# ---------------------------------------------------------------
# PROGRAMA PRINCIPAL (menu para escolher a questão)
# ---------------------------------------------------------------
def main():
    questoes = {
        "1": questao_1,
        "2": questao_2,
        "3": questao_3,
        "4": questao_4,
        "5": questao_5,
        "6": questao_6,
        "7": questao_7,
        "8": questao_8,
    }

    while True:
        print("\n=== DESAFIO PRÁTICO 3 ===")
        escolha = input("Escolha a questão (1 a 8) ou 0 para sair: ")

        if escolha == "0":
            print("Encerrando o programa...")
            break
        elif escolha in questoes:
            print()
            questoes[escolha]()
        else:
            print("Opção inválida, tente de novo.")


main()
