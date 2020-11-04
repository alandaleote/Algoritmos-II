from Pessoa import Pessoa

class Juridica(Pessoa):
    def __init__(self, nome, endereco, telefone, cnpj, inscricao_estadual, quantidade_funcionarios):
        Pessoa.__init__(self, nome, endereco, telefone)
        self._cnpj = cnpj
        self._inscricao_estadual = inscricao_estadual
        self.quantidade_funcionarios = quantidade_funcionarios

    def imprime_cnpj(self):
        print(self._cnpj)
    
    def _emitir_nota_fiscal(self):
        print("Nota Fiscal")
