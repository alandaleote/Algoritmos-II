from Veiculo import Veiculo

class Bicicleta(Veiculo):
    def __init__(self, marca, rodas, modelo, num, bag = False):
        Veiculo.__init__(self, marca, rodas, modelo)
        self.numMarchas = num
        self.bagageiro = bag

    def temBagageiro(self):
        if self.bagageiro:
            return 'com bagageiro'
        return 'sem bagageiro'

    def imprimirInformacoes(self):
        print('Bicicleta - {2} Rodas, Marca: {0}\nModelo: {1}, {4} marchas, {5}\nVelocidade atual = {3}km/h'.format(
            self.marca, self.modelo, str(self.qtdRodas), str(self.velocidade), str(self.numMarchas), self.temBagageiro()))
            