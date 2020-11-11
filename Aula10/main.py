from Veiculo import Veiculo
from Bicicleta import Bicicleta
from Automovel import Automovel
from Carro import Carro
from Moto import Moto

veiculo = Veiculo('HomeMade', 3, "carrinho de lomba")
bike = Bicicleta("caloi", 2, "cross", 18, True)
auto = Automovel("VW", 6, "caminhão", 5.0)
carro = Carro("Ford", 4, "Ka", 1.4, 4)
moto = Moto("Honda", 2, "CBR500R", 0.5, True)


bike.imprimirInformacoes()
bike.acelerar(10)
bike.imprimirInformacoes()
veiculo.imprimirInformacoes()
auto.imprimirInformacoes()
carro.imprimirInformacoes()
moto.acelerar(70)
moto.frear(10)
moto.imprimirInformacoes()