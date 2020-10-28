from Aluno import Aluno
from AlunoEnsinoMedio import AlunoEnsinoMeedio
from AlunoGraduacao import AlunoGraduacao

joao = Aluno(1, 'Joao', 'ab01234')

joao.imprimir()

maria = AlunoGraduacao(2, 'Maria', 'ab01235', 3)

maria.imprimir()

ana = AlunoEnsinoMeedio(2, 'Ana', 'ab01236', 8)

ana.imprimir()

joao = AlunoEnsinoMeedio(joao.codigo, joao.nome, joao.matricula, 2)
joao.imprimir()