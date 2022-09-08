class PilhaException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)


class PilhaSequencial:
    def __init__(self):
        self.__dados = []

    def vazia(self):
        return len(self.__dados) == 0
    
    def tamanho(self):
        return len(self.__dados)

    def topo(self):
        if self.vazia():
            raise PilhaException('A pilha está vazia')
        return self.__dados[0]

    def inserir(self, dado):
        self.__dados.insert(0, dado)
        #poderia ser só o append

    def remover(self):
        if self.vazia():
            raise PilhaException('A pilha está vazia')
        return self.__dados.pop(0)
        #se fosse o append poderia ser só o pop sem parâmetro

    def __str__(self):
        return self.__dados.__str__()

    def imprimir(self):
        print(self.__str__())
    

if __name__ == '__main__':
    p = PilhaSequencial()

    # for i in range(1,6):
    #     p.inserir(i * 10)

    # print(p)

    try:
        p.remover()
    except PilhaException as pe:
        print(pe)
    
    print(p)
