class ListaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class Node:
    def __init__(self, dado) -> None:
        self.__dado = dado
        self.__prox = None

    @property
    def dado(self):
        return self.__dado
    @property
    def prox(self):
        return self.__prox

    @dado.setter
    def dado(self, novoDado):
        self.__dado = novoDado
    @prox.setter
    def prox(self, novoProx):
        self.__prox = novoProx

    def __str__(self) -> str:
        return f'{self.__dado}'


class Lista:
    def __init__(self) -> None:
        self.__head = None
        self.__tamanho = 0

    def vazia(self) -> bool:
        return self.__tamanho == 0

    # def cheia(self) -> bool:
    #     pass

    def tamanho(self) -> int:
        return self.__tamanho

    def busca(self, dado:any) -> int:
        # for i in self.__dados:
        #     if i == dado:
        #         return i+1
        # return None

        # try:
        #     return self.__dados.index(dado) + 1
        # except:
        #     raise ListaException(f'O valor {dado} não se encontra na lista')

        if self.vazia():
            raise ListaException('A lista está vazia')
        cursor = self.__head
        cont = 1
        while cursor != None:
            if cursor.dado == dado:
                return cont
            cursor = cursor.prox
            cont += 1
        raise ListaException('O valor informado na busca não está na lista')

    def elemento(self, posicao:int) -> any:
        try:
            assert posicao > 0
            if self.vazia():
                raise ListaException('A lista está vazia')
            cursor = self.__head
            cont = 1
            while (cursor != None) and (cont < posicao):
                cursor = cursor.prox
                cont += 1
            if cursor != None:
                return cursor.dado
            raise ListaException('A posição é inválida para a lista')

        except TypeError:
            raise ListaException('O argumento posição deve ser um valor do tipo inteiro')
        except AssertionError:
            raise ListaException('Posição negativa não é válida para a lista')
        except:
            raise

    def inserir(self, posicao:int, dado:any):
        try:
            assert posicao > 0
            #CONDIÇÂO 1: inserção se a lista estiver vazia
            if self.vazia():
                if posicao != 1:
                    raise ListaException('A lista está vazia. Defina o argumento posição como 1')
                self.__head = Node(dado)
                self.__tamanho += 1
                return

            #CONDIÇÂO 2: inserção na primeira posição em uma lista não vazia
            if posicao == 1:
                novo = Node(dado)
                novo.prox = self.__head
                self.__head = novo
                self.__tamanho += 1
                return
                
            #CONDIÇÂO 3: inserção apos a primeira posição em uma lista não vazia
            cursor = self.__head
            cont = 1
            while (cont < (posicao - 1)) and (cursor != None):
                cursor = cursor.prox
                cont += 1
            if cursor == None:
                raise ListaException('A posição é inválida para inserção')
            novo = Node(dado)
            novo.prox = cursor.prox
            cursor.prox = novo
            self.__tamanho += 1

        # except TypeError:
        #     raise ListaException('O argumento posição deve ser um valor do tipo inteiro')
        except AssertionError:
            raise ListaException('Posição negativa não é válida para a lista')
        except:
            raise

    def remover(self, posicao:int):
        try:
            assert posicao > 0
            if self.vazia():
                raise ListaException('Lista vazia, não é possiível remover elementos')
            cursor = self.__head
            cont = 1
            while (cont <= (posicao - 1)) and (cursor != None):
                anterior = cursor
                cursor = cursor.prox
                cont += 1
            if cursor == None:
                raise ListaException('Posição inválida para remoção')
            dado = cursor.dado
            if posicao == 1:
                self.__head = cursor.prox
            else:
                anterior.prox = cursor.prox
            self.__tamanho -= 1
            return dado

        except TypeError:
            raise ListaException('O argumento posição deve ser um valor do tipo inteiro')
        except AssertionError:
            raise ListaException('Posição negativa não é válida para a lista')
        except:
            raise

    def __str__(self) -> str:
        str = 'Lista: [ '
        cursor = self.__head
        while cursor != None:
            str += f'{cursor.dado}'
            cursor = cursor.prox
            if cursor != None:
                str += ', '
        str += ']'
        return str

    def imprimir(self):
        print(self.__str__())

    def modificar(self, posicao:int, novoValor:any):
        try:
            assert posicao > 0
            if self.vazia():
                raise ListaException('Lista vazia. Não é possível romover elementos')
            cursor = self.__head
            cont = 1
            while (cursor != None) and (cont < posicao): #aqui pode ser (posicao - 1)
                cursor = cursor.prox
                cont += 1
            if cursor != None:
                cursor.dado = novoValor
                return
            raise ListaException('Posição inválida para a lista')

        except TypeError:
            raise ListaException('O argumento posição deve ser um valor do tipo inteiro')
        except AssertionError:
            raise ListaException('Posição negativa não é válida para a lista')
        except:
            raise



if __name__ == '__main__':
    # print('Lista encadeada')

    l1 = Lista()

    # if l1.vazia():
    #     print('Lista está vazia')
    
    # print('Tamanho:', l1.tamanho())

    for i in range(1,10):
        l1.inserir(i,i*10)
    print(l1)

    l1.inserir(1, 999)
    print(l1)
    l1.inserir(5, 888)
    print(l1)
    l1.inserir(12, 111)
    print(l1)
    
    try:
        l1.inserir(15, 333)
        print(l1)
    except ListaException as le:
        print(le)

    print(l1.remover(12))
    print(l1)
    print(l1.remover(1))
    print(l1)
    print(l1.remover(3))
    print(l1)

    try:
        print(l1.remover(15))
        print(l1)
    except ListaException as le:
        print(le)
