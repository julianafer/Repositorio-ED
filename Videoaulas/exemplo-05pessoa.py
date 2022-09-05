#INTRODUÇÃO A ENCAPSULAMENTO

#-----sem property e setter-----#
class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    def get_idade(self):
        return self._idade

    def set_idade(self, nova_idade):
        if nova_idade >= 0:
            self._idade = nova_idade

aluno = Pessoa('Carlos', 19)
print('Nome do Aluno:', aluno._nome)
aluno.set_idade(-3)
print('Idade do Aluno:', aluno.get_idade())

#-----com property e setter -----#
class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property #método get (vem antes do setter)
    def idade(self):
        return self._idade

    @idade.setter #método set (tem que ser o mesmo nome do property)
    def idade(self, nova_idade):
        if nova_idade >= 0:
            self._idade = nova_idade

aluno = Pessoa('Carlos', 19)
print('Nome do Aluno:', aluno._nome) #tenho que acessar nome com underline porque não foi definido propriedade
aluno.idade = -3 #se botar underline na frente ele vai chamar diretamente a propriedade, mas agente quer que ele chame o setter
print('Idade do Aluno:', aluno.idade) #posso acessar idade sem underline porque foi definido propriedade
