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


def imprimir_produto(ind):
    print('Produto: ' + nome_produto[ind] + '\nPreço: R$ ' + preco_produto[ind] + '\nQuantidade: ' + quantidade_produto[ind])


def deletar_produto(ind):
    nome_produto.delete(ind)
    preco_produto.pop(ind)
    quantidade_produto.delete(ind)