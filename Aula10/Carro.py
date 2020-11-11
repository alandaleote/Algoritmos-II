from Automovel import Automovel

class Carro(Automovel):
    def __init__(self, marca, rodas, modelo, potencia, portas):
        Automovel.__init__(self, marca, rodas, modelo, potencia)
        self.qtdPortas = portas

    def imprimirInformacoes(self):
        print('Carro - {5} portas, {2} Rodas\nMarca: {0}, Modelo: {1}\nPotência do motor: {4} - Velocidade atual = {3}km/h'.format(
            self.marca, self.modelo, str(self.qtdRodas), str(self.velocidade), str(self.potenciaDoMotor), self.qtdPortas))