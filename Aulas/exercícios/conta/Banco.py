from Conta import Conta
from typing import List

class OperacaoInvalidaException(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class Banco:
    def __init__(self):
        self.__contas = list()
        self.__saldoTotal = 0

    def sacar(self, numero:int, quantia:float)->bool:
        pass

    def depositar(self, numero:int, quantia:float):
        pass

    def addConta(self, numero:int, titular:str):
        self.__contas[numero] = Conta(numero,titular)
        # for conta in self.__contas:
        #     if conta.numero == numero:
        #         raise OperacaoInvalidaException('Conta de numero {numero} já está cadastrada')
        # self.__contas.append(Conta(numero, titular))