#PILHA ENCADEADA
'''Questão tá lá em baixo'''

class PilhaException(Exception):
    def __init__(self, msg) -> None:
        super().__init__(msg)


class No:
    def __init__(self, carga:int):
        self.carga = carga
        self.ant = None

    def __str__(self):
        return f'{self.carga}'

  
class Pilha:
    def __init__(self):
        self.__topo = None
        self.__tamanho = 0

    def estaVazia(self):
        return self.__tamanho == 0

    def tamanho(self):
        return self.__tamanho

    def empilhar(self, conteudo):
        novo = No(conteudo)
        novo.ant = self.__topo #o anterior do novo nó vai ser o atual topo
        self.__topo = novo #agora o novo nó que vai ser o topo
        self.__tamanho += 1

    def desempilhar(self):
        if self.estaVazia():
            raise PilhaException('Impossível desempilhar de uma piolha vazia')
        pop = self.__topo.ant
        self.__topo = self.__topo.ant
        self.__tamanho -= 1
        return pop

    def __str__(self):
        s = 'topo -> [ '
        cursor = self.__topo
        while(cursor != None):
            s+= f'{cursor.carga} '
            cursor = cursor.ant
        s += ']'
        return s

#==================== Questão 2 ====================#
  '''Não tá funcionando por causa da minha pilha'''
    def clone(self):
        pclone = Pilha()
        for posicao in range(1,self.tamanho()+1):
            pclone.empilhar(self.elemento(posicao))
        return pclone
#===================================================#
    


if __name__ == '__main__':
    p1 = Pilha()
    for i in range(10):
        p1.empilhar(i*10)
    print(p1)
    print(p1.clone())
