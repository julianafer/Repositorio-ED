class Pilha:
    def __init__(self):
        self.__dados = []

    def empilhar(self, dado):
        self.__dados.append(dado)

    def desempilhar(self):
        return self.__dados.pop()

    def tamanho(self):
        return len(self.__dados)

    def elementoTopo(self):
        index = self.tamanho() - 1
        return f'{self.__dados[index]}'

    def estaVazia(self):
        return len(self.__dados)==0
    
    def esvaziar(self):
        while not self.estaVazia():
            self.desempilhar()

    def __str__(self) -> str:
        return f'{self.__dados}'

