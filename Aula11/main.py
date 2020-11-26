import Lista

arquivo = open("lista.txt", "w")
arquivo.write("--- Lista de Compras ---\n")
arquivo.close()

menu = '''
+-----------------------+
1 - visualizar lista
2 - adicionar item
3 - remover item
0 - sair
+-----------------------+
Escolha: '''

while True:
    opcao = input(menu)
    if opcao == "0":
        break
    elif opcao == "1":
        Lista.visualizar()
    elif opcao == "2":
        Lista.adicionar()
    elif opcao == "3":
        Lista.remover()
    else:
        print("opção inválida")

