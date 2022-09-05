#introdução a atributos
class Aluno:
    def __init__(self, n, i, m):
        self.nome = n
        self.idade = i
        self.matricula = m

a = Aluno('Juliana', '18', '12345')

print('Nome do aluno:', a.nome)
print('Idade do aluno:', a.idade)
print('Matrícula do aluno:', a.matricula)
