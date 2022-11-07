from binary_tree_exception import BinaryTreeException

class Node:
    def __init__(self, dado = None):
        self.__dado = dado
        self.__esq = None
        self.__dir = None

    @property #get
    def dado(self):
        return self.__dado

    @dado.setter #set
    def dado(self, novo):
        self.__dado = novo

    @property #get
    def esq(self):
        return self.__esq

    @esq.setter #set
    def esq(self, novo):
        if self.__esq is not None:
            raise BinaryTreeException('Nó esquerdo já existe')
        self.__esq = novo

    @property #get
    def dir(self):
        return self.__dir

    @dir.setter #set
    def dir(self, novo):
        if self.__dir is not None:
            raise BinaryTreeException('Nó direito já existe')
        self.__dir = novo