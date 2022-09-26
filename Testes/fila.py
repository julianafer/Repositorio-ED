class Fila:
    def __init__(self):
        self.__dados = []
    
    def inserir(self, dado):
        self.__dados.append(dado)

    def remover(self):
        self.__dados.pop(0)
    
    def estaVazia(self):
        return len(self.__dados)==0

    def esvaziar(self):
        while not self.estaVazia():
            self.remover()

    def __str__(self) -> str:
        return f'remove -> {self.__dados} <- adiciona'


if __name__ == '__main__':
    
    f1 = Fila()
    for i in range(1,10):
        f1.inserir(i*10)
    print(f1)
    f1.remover()
    print(f1)
    f1.remover()
    print(f1)
    f1.inserir(100)
    print(f1)
    f1.esvaziar()
    print(f1)
    f1.inserir('oi')
    print(f1)