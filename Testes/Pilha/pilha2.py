class PilhaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class Pilha:
    def __init__(self):
        self.__dados = []

    def estaVazia(self):
        return self.__dados == []

    def inserir(self, conteudo:any) -> any:
        self.__dados.append(conteudo)

    def remover(self):
        if self.estaVazia():
            raise PilhaException('VAZIAAAA')
        self.__dados.pop()

    def __str__(self):
        return f'{self.__dados}'
