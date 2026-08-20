# EXERCICIO 1
'''
1. Verificador de Par ou Ímpar. Peça ao usuário um número inteiro e diga se ele
é par ou ímpar.
'''
print('VERIFICADOR DE PAR OU ÍMPAR')
print('===========================')
numero = int(input('Digite um número: '))
if numero >= 0:
    if numero % 2 == 0:
        print(f'O número {numero} é PAR!')
    else:
        print(f'O número {numero} é ÍMPAR!')
else: 
    print('Você digitou incorretamente. Digite um número inteiro.')
    print('Tente novamente.')
print('===========================')
print('PROGRAMA FINALIZADO')


# EXRCICIO 2
'''
2. Classificador de Idade. Solicite a idade de uma pessoa. Classifique-a como
"Criança" (0-12 anos), "Adolescente" (13-17 anos), "Adulto" (18-64 anos) ou "Idoso"
(65 anos ou mais). 
'''
print('CLASSIFICADOR DE IDADE')
print('======================')
idade = int(input('Digite uma idade: '))
if idade >= 0:
    if idade >= 0 and idade <= 12:
        print(f'Idade: {idade}')
        print('Classificação: CRIANÇA')
    elif idade >= 13 and idade <= 17:
        print(f'Idade: {idade}')
        print('Classificação: ADOLESCENTE')  
    elif idade >= 18 and idade <= 64:
        print(f'Idade: {idade}')
        print('Classificação: ADULTO')
    elif idade >= 65:
        print(f'Idade: {idade}')
        print('Classificação: IDOSO')
    else:
        print('Erro detectado.')
else:
    print('Você digitou incorretamente. Tente novamente.')
print('======================')
print('PROGRAMA FINALIZADO')


# EXERCICIO 3
'''
3. Mini Calculadora. Crie uma mini calculadora que permita ao usuário escolher
entre as operações de soma, subtração, multiplicação e divisão. Peça dois
números e a operação desejada. Imprima o resultado. 
'''
print('MINI CALCULADORA')
print('================')
numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
print('1 - SOMA\n2 - SUBTRAÇÃO\n3 - MULTIPLICAÇÃO\n4 - DIVISÃO')
resposta = int(input('Digite a operação desejada: '))
print('================')
if resposta >=1 and resposta <=4:
    if resposta == 1:
        print('Operação escolhida: SOMA')
        print(f'Resultado: {numero1 + numero2}')
    elif resposta == 2:
        print('Operação escolhida: SUBTRAÇÃO')
        print(f'Resultado: {numero1 - numero2}')
    elif resposta == 3:
        print('Operação escolhida: MULTIPLICAÇÃO')
        print(f'Resultado: {numero1 * numero2}')
    elif resposta == 4:
        if numero2 == 0 or numero1 == 0:
            print('OPA! ERRO! Não existe divisão por ZERO.')
            numero2 = float(input('Digite outro número DIFERENTE DE ZERO: '))
            print(f'Resultado: {numero1 / numero2}')
        else:
            print('Operação escolhida: DIVISÃO')
            print(f'Resultado: {numero1 / numero2}')
    else: 
        print('Erro detectado.')
else:
    print('Você digitou incorretamente.\nTente novamente.')
print('================')
print('PROGRAMA FINALIZADO')


# EXERCICIO 4
'''
4. Classificador de Triângulos. Peça ao usuário para digitar o comprimento de
três lados de um triângulo. Determine se os lados formam um triângulo válido
e, em caso afirmativo, classifique-o como Equilátero, Isósceles ou Escaleno. 
'''
print('CLASSIFICADOR DE TRIâNGULOS')
print('===========================')
lado1 = float(input('Comprimento do 1º lado: '))
lado2 = float(input('Comprimento do 2º lado: '))
lado3 = float(input('Comprimento do 3º lado: '))
print()
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('As medidas formam um triângulo VÁLIDO!')
    if lado1 == lado2 and lado2 == lado3 and lado3 == lado1:
        print('Classificação: TRIÂNGULO EQUILÁTERO')
    elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
        print('Classificação: TRIÂNGULO ISÓSCELES')
    else:
        print('Classificação: TRIÂNGULO ESCALENO')
else: 
    print('As medidas NÃO formam um triângulo válido!')
print()
print('===========================')
print('PROGRAMA FINALIZADO')


# EXERCICIO 5
'''
Solicite os coeficientes a, b e c de uma equação do segundo grau (ax² + bx + c
= 0). Determine e mostre o número de raízes reais distintas que a equação
possui. 
'''
print('QUANTIDADE DE RAIZES REAIS')
print('==========================')
print('Equação do 2º grau: ax² + bx + c = 0')
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))
delta = b**2 - 4*a*c
print(f'O valor de delta é: {delta}')
if delta > 0:
    print('A equação possui duas raízes reais distintas')
elif delta == 0:
    print('A equação possui uma raiz real (ou duas raízes reais iguais)')
else:
    print('A equação não possui raízes reais.')
print('==========================')
print('PROGRAMA FINALIZADO')


# EXERCICIO 6
'''
Peça ao usuário a temperatura da água (em graus Celsius). Determine o
estado físico da água (sólido, líquido ou gasoso).
'''
print('CLASSIFICADOR DE ESTADO FÍSICO DA ÁGUA')
print('======================================')
temperatura = float(input('Digite a temperatura da água (em graus Celsius): '))
if temperatura <= 0: 
    print(f'Temperatura: {temperatura}°C')
    print('A água está em estado SÓLIDO')
elif temperatura > 0 and temperatura < 100:
    print(f'Temperatura: {temperatura}°C')
    print('A aguá está em estado LÍQUIDO')
elif temperatura >= 100:
    print(f'Temperatura: {temperatura}°C')
    print('A água está em estado GASOSO')
else: 
    print('Erro detectado. Tente novamente.')
print('======================================')
print('PROGRAMA FINALIZADO')


# EXERCICIO 7
'''
Escreva um código que imprima um relatório contendo o nome, valor da venda
e a comissão do corretor. 
'''
# VERSÃO 1
print('CÁLCULO DE COMISSÃO')
print('===================')
nome = input('Nome do(a) funcionário(a): ')
valor_venda = float(input('Digite o valor da venda: R$'))
if valor_venda >= 0 and valor_venda <= 500000:
    comissao = 0.06 * valor_venda
    print(f'Nome do(a) funcionário(a): {nome}')
    print(f'Valor da venda: R${valor_venda:.2f}')
    print(f'Comissão: R${comissao:.2f}')
elif valor_venda > 500000 and valor_venda <= 700000:
    comissao = 0.085 * valor_venda
    print(f'Nome do(a) funcionário(a): {nome}')
    print(f'Valor da venda: R${valor_venda:.2f}')
    print(f'Comissão: R${comissao:.2f}')
elif valor_venda > 700000 and valor_venda <= 1000000:
    comissao = 0.1 * valor_venda
    print(f'Nome do(a) funcionário(a): {nome}')
    print(f'Valor da venda: R${valor_venda:.2f}')
    print(f'Comissão: R${comissao:.2f}')
elif valor_venda > 1000000:
    comissao = 0.12 * valor_venda
    print(f'Nome do(a) funcionário(a): {nome}')
    print(f'Valor da venda: R${valor_venda:.2f}')
    print(f'Comissão: R${comissao:.2f}')
else: 
    print('Erro detectado. Tente novamente.')
print('===================')
print('PROGRAMA FINALIZADO')

# VERSAO 2
print('CÁLCULO DE COMISSÃO')
print('===================')
nome = input('Nome do(a) funcionário(a): ')
valor_venda = float(input('Digite o valor da venda: R$'))
if valor_venda < 0:
    print('Erro detectado. Tente novamente.')
else:
    if valor_venda <= 500000:
        taxa = 0.06
    elif valor_venda <= 700000:
        taxa = 0.085
    elif valor_venda <= 1000000:
        taxa = 0.1
    else:
        taxa = 0.12
    comissao = taxa * valor_venda
    print(f'Nome do(a) funcionário(a): {nome}')
    print(f'Valor da venda: R${valor_venda:.2f}')
    print(f'Comissão: R${comissao:.2f}')
print('===================')
print('PROGRAMA FINALIZADO')


# EXERCICIO 8
'''
Construa um código que mostre o nome do hóspede e o total da conta a pagar.
'''
# VERSAO 1 
print('HOTEL CENTRAL DE TERESINA')
print('=========================')
nome = input('Nome do hóspede: ')
diaria = int(input('Digite a quantidade de dias da hospedagem: '))
if diaria > 7: 
    taxa = 6.5 * diaria
    total = 290 + taxa
    print(f'Nome do hóspede: {nome}')
    print(f'Total a pagar: R${total:.2f}')
elif diaria == 7:
    taxa = 12 * diaria
    total = 290 + taxa
    print(f'Nome do hóspede: {nome}')
    print(f'Total a pagar: R${total:.2f}')
elif diaria > 0 and diaria < 7:
    taxa = 16.5 * diaria
    total = 290 + taxa
    print(f'Nome do hóspede: {nome}')
    print(f'Total a pagar: R${total:.2f}')
else: 
    print('Erro detectado. Tente novamente.')
print('=========================')
print('PROGRAMA FINALIZADO')

# VERSAO 2
print('HOTEL CENTRAL DE TERESINA')
print('=========================')
nome = input('Nome do hóspede: ')
diaria = int(input('Digite a quantidade de dias da hospedagem: '))
if diaria > 7: 
    taxa = 6.5 * diaria
    total = 290 + taxa
    print(f'Nome do hóspede: {nome}')
    print(f'Total a pagar: R${total:.2f}')
elif diaria == 7:
    taxa = 12 * diaria
    total = 290 + taxa
    print(f'Nome do hóspede: {nome}')
    print(f'Total a pagar: R${total:.2f}')
elif diaria > 0 and diaria < 7:
    taxa = 16.5 * diaria
    total = 290 + taxa
    print(f'Nome do hóspede: {nome}')
    print(f'Total a pagar: R${total:.2f}')
else: 
    print('Erro detectado. Tente novamente.')
print('=========================')
print('PROGRAMA FINALIZADO')
