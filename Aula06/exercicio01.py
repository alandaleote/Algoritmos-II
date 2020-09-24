'''
Construa um algoritmo que possua uma tupla com os números
escritos por extenso de “zero” a “nove”. Peça ao usuário para digitar
um nome de 0 a 9 e retorne a ele o número por extenso, sem usar
estruturas condicionais (if e switch).
'''

numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove')

index = int(input('Digite um número de 0 a 9: '))

print('Você digitou o número {}'.format(numeros[index]))
