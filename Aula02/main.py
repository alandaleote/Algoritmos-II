from Lista import Lista

lista = Lista()
print( "Tamanho da Lista: " + str( lista.tamanho ))
lista.adicionar( 3 )
lista.adicionar( 10 )
print( "Tamanho da Lista: " + str( lista.tamanho ))
lista.imprimir()

valor = input("Digite um valor: ")
lista.adicionar( valor )
lista.adicionar( 100 )
print( "\n -----------------\n")
lista.imprimir()
print( "Tamanho da Lista: " + str( lista.tamanho ))

valor = input("Digite um valor que sedeja excluir: ")
lista.excluir( valor )
lista.imprimir()