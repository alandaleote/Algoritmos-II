class Veiculo:
    def __init__(self, marca, rodas, modelo):
        self.marca = marca
        self.qtdRodas = rodas
        self.modelo = modelo
        self.velocidade = 0
    
    
    def imprimirInformacoes(self):
        print('Veículo {2} Rodas - Marca: {0} Modelo: {1}\nVelocidade Atual = {3}km/h'.format(
            self.marca, self.modelo, str(self.qtdRodas), str(self.velocidade)))

    def acelerar(self, value):
        self.velocidade += value

    def frear(self, value):
        self.velocidade -= value