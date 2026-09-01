# DESAFIO PRATICO 2

# EXERCICIO 1 - FATORIAL DE UM NÚMERO
'''Escreva um programa em Python que
calcule o fatorial de um número informado pelo usuário'''
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
'''Resumo estatístico de notas de um curso. Leia as notas de uma turma até que
o usuário digite algo para sair. Para cada nota válida, determine se o estudante
foi aprovado, ficou em recuperação ou foi reprovado. Considere aprovado para
nota maior ou igual a 7,0, recuperação para nota entre 5,0 e 6,9, e reprovação
para nota inferior a 5,0.
Ao final, apresente a média da turma, a maior nota, a menor nota, o percentual
de aprovação e a situação geral da turma. Classifique a turma como “desempenho
satisfatório” quando o percentual de aprovação for igual ou superior a 70%. 
'''
print('TURMA BANCO DE DADOS - PIT')
print('==========================')

maiusc = ''
soma = 0
cont_notas = 0
maior = 0
menor = 0
aprovacao = 0
notas_boas = 0
while maiusc != 'SAIR':
    print('Digite a nota e nome do aluno(a)')
    nome = input('Nome: ')
    nome_maiusc = nome.title()
    nota = float(input('Nota: '))

    if nota >= 0 and nota <= 10:

        soma += nota
        cont_notas += 1
        media = soma / cont_notas
        maior = nota
        menor = nota

        if nota >= 7:
            print('Situação: APROVADO(A)!')
            notas_boas += 1
        elif nota < 7 and nota >= 5:
            print('Situação: RECUPERAÇÃO!')
        else:
            print('Situação: REPROVADO(A)!')


        if nota > maior:
            maior = nota
        elif nota < menor:
            menor = nota

        aprovacao = (notas_boas / cont_notas) * 100
    else:
        print('Nota inváida!')

    print('============================')
    resp = input('[SIM - PARA CONTINUAR]\n[SAIR - PARA FINALIZAR]\nDeseja continuar: ')
    maiusc = resp.upper()
    print('============================')
print(f'Média da turma: {media:.2f}')
print(f'Maior nota: {maior}')
print(f'Menor nota: {menor}')
print(f'Percentual de aprovação: {aprovacao:.2f}%')
if aprovacao >= 70:
    print(f'DESEMPENHO SATISFATÓRIO DA TURMA!')

# EXERCICIO 4

# EXERCICIO 5

# EXERCICIO 6





