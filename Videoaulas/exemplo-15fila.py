class FilaException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)


class FilaSequencial:
    def __init__(self):
        self.__dados =[]

    def vazio(self):
        return len(self.__dados) == 0

    def tamanho(self):
        return len(self.__dados)

    def inicio(self):
        if self.vazio():
            raise FilaException('A fila está vazia')
        return self.__dados[0]

    def inserir(self, dado):
        self.__dados.append(dado)
        #poderia ser um insert na posição de índice 0

    def remover(self):
        if self.vazio():
            raise FilaException('A fila está vazia')
        return self.__dados.pop(0)
        #se fosse um insert poderia ser um pop vazio

    def __str__(self):
        return self.__dados.__str__()

    def imprimir(self):
        print(self.__str__())


if __name__ == '__main__':
    f = FilaSequencial()

    # for i in range(1,6):
    #     f.inserir(i * 10)

    # print(f)
    # f.remover()
    # print(f)
    
    try:
        f.remover()
    except FilaException as fe:
        print(fe)
    print(f)
