from Aluno import Aluno

class AlunoEnsinoMeedio(Aluno):

    def __init__(self,codigo, nome, matricula, ano):
        Aluno.__init__(self, codigo, nome, matricula)
        self.ano = ano

    def imprimir(self):
        print('Código: {} - Nome: {} - Matrícula: {} Ano: {}'.format(str(self.codigo), self.nome, self.matricula, str(self.ano)))