from Automovel import Automovel

class Moto(Automovel):
    def __init__(self, marca, rodas, modelo, potencia, partida = False):
        Automovel.__init__(self, marca, rodas, modelo, potencia)
        self.partidaEletrica = partida

    def temPartidaEletrica(self):
        if self.partidaEletrica:
            return 'com partida elétrica'
        return 'sem partida elétrica'

    def imprimirInformacoes(self):
        print('Moto - {2} Rodas, Marca: {0}, Modelo: {1}\nPotência do motor: {4}, {5}\nVelocidade atual = {3}km/h'.format(
            self.marca, self.modelo, str(self.qtdRodas), str(self.velocidade), str(self.potenciaDoMotor), self.temPartidaEletrica()))