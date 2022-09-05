class Curso:
    def __init__(self, nome='', periodo=20222):
        self.nome = nome #propriedades ou atributos
        self.periodo = periodo #o fato de começarem com o self já identifica que é uma prpriedade de instância

    def getNome(self): #método de instância porque o primeiro argumento é o self
        return self.nome
    
    def imprime(self):
        print('Curso:', self.nome, '/', self.periodo)

curso1 = Curso()
curso2 = Curso()

curso1.nome = 'CSTSI'
curso1.periodo = 20201
curso2.nome = 'CSTRC'
curso2.periodo = 20202

curso1.imprime()
curso2.imprime()
