# DESAFIO PRATICO 2

# EXERCICIO 1 - FATORIAL DE UM NÚMERO
'''Escreva um programa em Python que
calcule o fatorial de um número informado pelo usuário
'''
import math
print(' === FATORIAL ===')
num = int(input('Digite um número: '))

fatorial = math.factorial(num) # modulo fatorial da biblioteca math

print(f'{num}! = ', end='') 

c = num + 1

while c > 1:
    c -= 1
    if c > 1:
        print(c, end=' X ')
    else: 
        print(c, end='')

print(f' = {fatorial}')
print('FIM DO PROGRAMA')


# EXERCICIO 2
'''Faça um programa que calcule
e escreva o número de anos necessários para que a população do país A
ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento. 
'''
print('PAÍS A = 90.000 habitantes')
print('PAÍS B = 200.000 habitantes')
print()
pop_a = 90000
pop_b = 200000

taxa_a = 0.05 # 5%
taxa_b = 0.015 # 1.5%

anos = 0

while pop_a < pop_b:
    pop_a = taxa_a * pop_a + pop_a
    pop_b = taxa_b * pop_b + pop_b
    anos += 1

print(f'Em {anos} anos a população de A será maior que a de B.')
print(f'População final de A: {round(pop_a)}')
print(f'População final de B: {round(pop_b)}')


# EXERCICIO 3
'''
Resumo estatístico de notas de um curso. Leia as notas de uma turma até que
o usuário digite algo para sair. Para cada nota válida, determine se o estudante
foi aprovado, ficou em recuperação ou foi reprovado. Considere aprovado para
nota maior ou igual a 7,0, recuperação para nota entre 5,0 e 6,9, e reprovação
para nota inferior a 5,0.
Ao final, apresente a média da turma, a maior nota, a menor nota, o percentual
de aprovação e a situação geral da turma. Classifique a turma como “desempenho
satisfatório” quando o percentual de aprovação for igual ou superior a 70%.
Requisitos: utilizar while; aceitar notas entre 0 e 10; não encerrar a leitura ao
receber um valor inválido; impedir divisão por zero; utilizar decisões para a
situação individual e para a classificação geral. 
'''
print("===================================")
print("       RESUMO DA TURMA")
print("===================================")

soma = 0
quantidade = 0
aprovados = 0
maior = 0
menor = 10

while True:
    entrada = input("Digite uma nota ou 'fim' para encerrar: ")

    if entrada.lower() == "fim":
        break

    nota = float(entrada)

    if nota < 0 or nota > 10:
        print("Nota inválida! Digite uma nota entre 0 e 10.")
        continue

    quantidade += 1
    soma += nota

    if nota > maior:
        maior = nota

    if nota < menor:
        menor = nota

    if nota >= 7:
        print("Situação: Aprovado")
        aprovados += 1

    elif nota >= 5:
        print("Situação: Recuperação")

    else:
        print("Situação: Reprovado")

if quantidade > 0:

    media = soma / quantidade
    percentual_aprovacao = (aprovados / quantidade) * 100

    print("\n===================================")
    print("          RESUMO DA TURMA")
    print("===================================")

    print(f"Média da turma: {media:.2f}")
    print(f"Maior nota: {maior:.2f}")
    print(f"Menor nota: {menor:.2f}")
    print(f"Percentual de aprovação: {percentual_aprovacao:.2f}%")

    if percentual_aprovacao >= 70:
        print("Situação geral: Desempenho satisfatório")
    else:
        print("Situação geral: Desempenho insatisfatório")

else:
    print("\nNenhuma nota válida foi informada.")

# EXERCICIO 4 
'''
Seleção de atributos para um modelo. Um conjunto de dados possui n atributos
disponíveis. O analista deseja selecionar r atributos para uma etapa de
modelagem, sem considerar a ordem de seleção. Calcule o número de
subconjuntos possíveis usando: 
C(n, r) = n! / (r! * (n-r)!)
O programa deve validar 0 <= r <= n e informar se a quantidade de subconjuntos
é compatível com uma busca exaustiva. Considere viável a busca quando houver
até 10.000 combinações.
Requisitos: calcular o resultado sem função pronta de fatorial; utilizar repetição;
aplicar decisões para validar os parâmetros e classificar a viabilidade; explicar
por que a ordem dos atributos não altera uma combinação.
'''
print('   AMOSTRAGEM DE ATRIBUTOS   ')
print('=============================')

n = int(input('Digite a quantidade de atributos disponíveis: '))
r = int(input('Digite a quantidade de atributos a selecionar: '))

if r < 0 or r > n:
    print('Erro: 0 <= r <= n.')
else: 
    fatorial_n = 1
    for i in range(1, n + 1):
        fatorial_n = fatorial_n * i

    fatorial_r = 1
    for i in range(1, r + 1):
        fatorial_r = fatorial_r * i

    fatorial_nr = 1
    for i in range(1, n - r + 1):
        fatorial_nr = fatorial_nr * i

    combinacoes = fatorial_n // (fatorial_r * fatorial_nr)
    print(f"Número de subconjuntos possíveis: {combinacoes}")

    if combinacoes <= 10000:
        print("Busca exaustiva: VIÁVEL.")
    else:
        print("Busca exaustiva: NÃO VIÁVEL.")

# EXERCICIO 5 
'''
Uma população inicial de 2727 indivíduos cresce a uma taxa de 4% ao ano.
Escreva um programa em Python que simule o crescimento dessa população e
mostre o tamanho da população ao final de cada ano, durante 5 anos.
'''
print('   PROJEÇÃO POPULACIONAL   ')
print('===========================')
populacao = 2727
taxa = 0.04   # taxa de 4% ao ano
anos = 5

for c in range(1, anos + 1):
    populacao = populacao * (1 + taxa)
    print(f'PROJEÇÃO ANO {c}: {populacao:.0f} habitantes')
print('===========================')
print('      FIM DO PROGRAMA   ')

# EXERCICIO 6
'''
Probabilidade experimental. Um experimento consiste em lançar um dado 20
vezes. O programa recebe o resultado de cada lançamento e deve contar quantas
vezes apareceu um número par. Ao final, deve calcular a probabilidade
experimental de obter um número par.
'''
import random
print('  PROBABILIDADE EXPERIMENTAL  ')
print('==============================')

print('O dado será lançado...')

cont_par = 0

for c in range(1, 21):

    resultado = random.randint(1, 6)
    print(f'Resultado do {c}º lançamento: {resultado}')

    if resultado % 2 == 0:
        cont_par += 1

probabilidade = (cont_par / 20) * 100 

print(f'A probabilidade de cair um número par é {probabilidade:.2f} %')
