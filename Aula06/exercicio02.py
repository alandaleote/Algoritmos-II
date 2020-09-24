'''
Construa um algoritmo que peça ao usuário para informar o nome, a
nota01 e a nota02 de um aluno. Guarde estas informações em um
dicionário. Após, calcule a nota final deste aluno [(nota01 + nota02)
/2] e adicione ao dicionário. Ao final, imprima todos os dados do
dicionário.
'''

nome = input('Digite o nome do(a) aluno(a): ')
nota1 = float(input('Insira a nota 01: '))
nota2 = float(input('Insira a nota 02: '))

aluno = { 'nome' : nome, 'nota01' : nota1, 'nota02' : nota2 }

media = (aluno['nota01'] + aluno['nota02'])/2

aluno['media'] = media

print(aluno)
