from Fila import Fila

fila = Fila()
menu = '''
+--------MENU--------+
|   1 - Adicionar    |
|   2 - Remover      |
|   3 - Imprimir     |
|   0 - Sair         |
+--------------------+
Escolha: '''

while True:
    opcao = (input(menu))

    if opcao == '0':
        break
    elif opcao == '1':
        # dado = input('Informe um valor: ')
        fila.adicionar(input('Informe um valor: '))
    elif opcao == '2':
        fila.remover()
    elif opcao == '3':
        fila.imprimir()
    else:
        print('Opção inválida')