'''
Construir um algoritmo que contenha 3 listas:
• Nomes de produtos
• Preços de cada produto
• Quantidades de cada produto
• Construir uma função para imprimir um dos produtos da lista e uma
função para retirar um dos produtos das listas
'''

nome_produto = []
preco_produto = []
quantidade_produto = []

def inserir_produto():
    try:
        nome = input('Nome do produto: ')
        preco = float(input('Preço unitário: '))
        quantidade = int(input('Quantidade: '))
        nome_produto.append(nome)
        preco_produto.append(preco)
        quantidade_produto.append(quantidade)
    except:
        print("valores inválidos")

def deletar_produto(nome):
    for i,e in enumerate(nome_produto):
        if e == nome:
            ind = i
    nome_produto.pop(ind)
    preco_produto.pop(ind)
    quantidade_produto.pop(ind)

def imprimir_tudo():
    if len(nome_produto) > 0:
        print('Produto ----------------------- --- Preço --- Quantidade')
        for i,nome in enumerate(nome_produto):
            print( str(nome).ljust(33,' '), 
                str(preco_produto[i]).center(10, ' '),
                str(quantidade_produto[i]).center(14, ' ')
            )
    else:
        print('Não existem produtos na lista.')


menu = '''
    +---------------MENU----------+
    |                             |
    |   0 - Sair                  |
    |   1 - Adicionar produto     |
    |   2 - Deletar produto       |
    |   3 - Visualizar produtos   |
    |                             |
    +-----------------------------+
    Escolha: '''

while (True):
    escolha = int(input(menu))
    if escolha == 0:
        break
    elif escolha == 1:
        inserir_produto()
    elif escolha == 2:
        prod = input('Digite o nome do produto: ')
        if prod in nome_produto:
            deletar_produto(prod)
            print('{} deletado com sucesso!'.format(prod))
        else:
            print('Produto não encontrado.')
    elif escolha == 3:
        imprimir_tudo()
    else:
        print('valor inválido')