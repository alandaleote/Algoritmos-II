from No import No

class Lista: 

    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def __len__(self):
        return self.tamanho 

    def adicionar(self, dado):
        no = No(dado)
        if self.__len__ == 0:
            self.inicio = no
            self.fim = no
        elif self.inicio = self.fim:
            aux = self.inicio
            aux.proximo = no
            no.anterior = aux
            self.fim = no
        else:
            aux = self.inicio
            while(aux.proximo):
                aux.anterior = aux
                aux = aux.proximo
            aux.anterior = aux
            aux.proximo = no
            self.fim.proximo = no
            self.fim = no
        self.tamanho += 1
        elif self.inicio and !(self.fim):
            aux = self.inicio




            aux = self.inicio
            while(aux.proximo):
                aux = aux.proximo
            aux.proximo = no
        else:
            
        self.tamanho += 1


    def imprimir(self):
        aux = self.inicio
        if self.inicio == None:
            print("--Lista Vazia--")
        else:
            while(aux):
            print( str(aux.dado) + "\n" )
            aux = aux.proximo
        print( "Tamanho da Lista: " + str(self.__len__))
        

    def excluir(self, dado):
        if self.tamanho == 0 :
            print( "--Lista Vazia--")
        elif self.tamanho == 1 :
            if self.inicio.dado == dado:
                self.inicio = None
                self.fim = None
                self.tamanho -= 1
            else:
                print( "--não consta na lista--")
        else:
            if self.inicio.dado == dado:
                aux = self.inicio.proximo
                self.inicio = aux
                self.tamanho -= 1
            else:
                ant = self.inicio
                aux = ant.proximo
                while(aux):
                    if aux.dado == dado:
                        ant.proximo = aux.proximo
                    ant = aux
                    aux = aux.proximo
                self.tamanho -= 1