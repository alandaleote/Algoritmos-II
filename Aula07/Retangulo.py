'''
▷Construa um algoritmo para implementar a classe
Retângulo que possui os atributos: altura e largura.
▷ A classe deve ter os seguintes métodos:
○ Método construtor
○ Método que calcula a área do retângulo ( altura * largura) e
retorna o resultado
○ Método que imprime os valores dos atributos da classe.
'''

class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def calcular_area(self):
        area = int(self.altura) * int(self.largura)
        return area

    def imprimir_atributos(self):
        print('Altura= {}\nLargura= {}'.format(self.altura, self.largura))


r1 = Retangulo(3, 4)
Retangulo.imprimir_atributos(r1)
print('Área = {}'.format(str(Retangulo.calcular_area(r1))))
