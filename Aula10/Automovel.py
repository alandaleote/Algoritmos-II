from Veiculo import Veiculo

class Automovel(Veiculo):
    def __init__(self, marca, rodas, modelo, potencia):
        Veiculo.__init__(self, marca, rodas, modelo)
        self.potenciaDoMotor = potencia

    def imprimirInformacoes(self):
        print('Automóvel - {2} Rodas, Marca: {0}\nModelo: {1}, Potência do motor: {4}\nVelocidade atual = {3}km/h'.format(
            self.marca, self.modelo, str(self.qtdRodas), str(self.velocidade), str(self.potenciaDoMotor)))