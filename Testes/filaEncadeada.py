
from pilha2 import *


class FilaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class Head: #nó cabeça, só de controle
    def __init__(self):
        self.inicio = None
        self.final = None
        self.tamanho = 0
        #sempre começa com nada, depois a genete adiciona


class No: #nó igual de pilha sequencial
    def __init__(self, carga):
        self.carga = carga
        self.prox = None

    def __str__(self):
        return f'{self.carga}'


class Fila:
    def __init__(self):
        self.__head = Head() #váriável para armazenar o nó de controle

    def estaVazia(self):
        return self.__head.tamanho == 0

    def tamanho(self):
        return self.__head.tamanho

    def enfileirar(self, conteudo):
        novo = No(conteudo) #cria um novo nó
        if self.estaVazia():
            self.__head.inicio = novo #o começo do head vai receber o novo nó
            self.__head.final = novo #e o topo também vai receber o novo nó porque a fila estava vazia
        else:
            self.__head.final.prox = novo  #o atual topo da lista vai apontar pro novo nó, ou seja o próximo vai ser o novo nó
            self.__head.final = novo #agr faz com que o novo nó seja o atual topo da fila
        self.__head.tamanho += 1

    def desemfileirar(self):
        if self.estaVazia():
            raise FilaException('A fila está vazia BURRE!')
        else:
            pokebola = self.__head.inicio #guardar em uma variável pra fazer como um pop
            self.__head.inicio = self.__head.inicio.prox #o final vai ser o próximo do final, ou seja vai meio que ignorar o final
            self.__head.tamanho -= 1
            return pokebola #retorna como um pop

    def __str__(self) -> str:
        s = '[ '
        cursor = self.__head.inicio
        while cursor != None:
            s += f'{cursor.carga} '
            cursor = cursor.prox
        s += ']'
        return str(s)

    # def inverter(self):
    #     novo_inverte = Fila()
    #     pokebola = Pilha()
    #     cursor = self.__head.inicio
    #     while cursor != None:
    #         pokebola.inserir(self.desemfileirar())
    #         cursor = cursor.prox
    #         #pokebola = [19, 46, 23]
    #     while not pokebola.estaVazia():
    #         novo_inverte = self.enfileirar(pokebola.remover())
    #     return novo_inverte


if __name__ == '__main__':

    f1 = Fila()
    f1.enfileirar(19)
    f1.enfileirar(46)
    f1.enfileirar(23)
    print(f1)
    # print(f1.inverter())