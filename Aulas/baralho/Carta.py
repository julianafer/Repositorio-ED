class Carta:
    def __init__(self, valor, naipe, cor):
        # definir as propriedades da classe
        self.__naipe = naipe
        self.__valor = valor
        self.__cor = cor

    def getValor(self):
        return self.__valor

    def getNaipe(self):
        return self.__naipe

    def getCor(self):
        return self.__cor

    def __str__(self):
        return f'{self.__valor} de {self.__naipe}'
