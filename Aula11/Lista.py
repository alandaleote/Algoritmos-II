
def listar_itens():
    lista = []
    arq = open("lista.txt", "r")
    for linha in arq:
        lista.append(linha.strip())
    return lista
    arq.close()

def salvar_lista(nova_lista):
    lista = nova_lista
    arq = open("lista.txt", "w")
    for item in nova_lista:
        arq.write(item + '\n')

def adicionar():
    item = input("Insira o item a ser adicionado: ")
    arq = open("lista.txt", "a") 
    arq.write(item + '\n')
    arq.close()

def remover():
    item = input("Insira o item a ser excluído: ")
    lista = listar_itens()
    for i in lista:
        if i == item:
            lista.remove(item)
            salvar_lista(lista)

def visualizar():
        lista = listar_itens()
        for item in lista:
            print(item)
        