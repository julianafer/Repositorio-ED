class Pilha:
    def __init__(self):
        self.__dados = []

    def inserir(self, dado):
        self.__dados.append(dado)

    def remover(self):
        self.__dados.pop()

    def estaVazia(self):
        return len(self.__dados)==0

    def esvaziar(self):
        while not self.estaVazia():
            self.remover()

    def __str__(self) -> str:
        return f'{self.__dados} <- topo'


if __name__=='__main__':

    p1 = Pilha()
    for i in range(1,10):
        p1.inserir(i*5)
    print('P1:',p1)

    p1.remover()
    print('P1:',p1)
    p1.inserir(100)
    print('P1:',p1)
    p1.esvaziar()
    print('P1:',p1)

    p2 = Pilha()
    for i in range(1,5):
        p2.inserir(i*10)
    print('P2:',p2)
