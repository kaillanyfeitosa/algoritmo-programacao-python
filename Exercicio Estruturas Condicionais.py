# EXERCICIO 1 
'''
meu_nome = input('Digite seu nome: ')
minha_idade = int(input('Digite sua idade: '))
nome_amigo = input('Digite o nome do seu amigo(a): ')
idade_amigo = int(input('Digite a idade do seu amigo(a): '))
if minha_idade > idade_amigo:
    print(f'{meu_nome} é mais velho(a) que {nome_amigo}.')
elif minha_idade < idade_amigo: 
    print(f'{nome_amigo} é mais velho que {meu_nome}.')
elif minha_idade == idade_amigo:
    print(f'{meu_nome} e {nome_amigo} têm idades iguais.') 
else: 
    print('Há algo de errado.')


# EXERCICIO 2
print('STRANS - RADAR DE VELOCIDADE')
print('============================')
print('Local: Av. dos Ipês')
print('Velocidade máxima permitida: 60 km/h')
print('============================')
placa = input('Digite a placa do veículo: ')
placa_maiuscula = placa.upper()
velocidade = float(input('Digite a velocidade do veículo: '))
if velocidade > 60:
    print(f'Veículo - Placa: {placa_maiuscula}')
    print('Situação: MULTADO')
elif velocidade <= 60: 
    print(f'Veículo - Placa: {placa_maiuscula}')
    print('Situação: REGULAR')
else: 
    print('Um erro aconteceu. Tente novamente.')
'''

# EXERCICIO 3
print(' LOJA DA MARIA ')
print('===============')
produto = input('Nome do produto: ')
valor = float(input('Valor do produto: '))
print('===============')
if valor > 200:
    desconto = 0.1 * valor
    valor_final = valor - desconto
    print(f'Nome do produto: {produto}')
    print(f'Valor do produto: R${valor:.2f}')
    print(f'Desconto: R${desconto:.2f}')
    print(f'Valor final do produto: R${valor_final:.2f}')
elif valor >= 50 and valor <= 200:
    desconto = 30
    valor_final = valor - desconto
    print(f'Nome do produto: {produto}')
    print(f'Valor do produto: R${valor:.2f}')
    print(f'Desconto: R${desconto:.2f}')
    print(f'Valor final do produto: R${valor_final:.2f}')
elif valor < 50:
    desconto = 0
    valor_final = valor
    print(f'Nome do produto: {produto}')
    print(f'Valor do produto: R${valor:.2f}')
    print('Não há desconto.')
    print(f'Valor final: R${valor_final:.2f}')
else: 
    print('Um erro aconteceu. Tente novamente.')

