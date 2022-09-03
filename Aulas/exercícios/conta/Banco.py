from Conta import Conta
from typing import List

class OperacaoInvalidaException(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class Banco:
    def __init__(self):
        self.__contas = dict() #dicionário
        self.__saldoTotal = 0

    def sacar(self, numero:int, quantia:float):
        try:
            assert quantia > 0
            # obter o objeto correspondente à conta
            conta = self.__contas[numero]
            if conta.saldo - quantia >= 0:
                conta.saldo -= quantia
            else:
                raise OperacaoInvalidaException(f' Conta {numero}: Saldo insuficiente para saque')
        except AssertionError:
            raise OperacaoInvalidaException('Quantia a retirar não pode ser negativa')
        except KeyError:
            raise OperacaoInvalidaException(f'Conta {numero} não está cadastrada')

    def depositar(self, numero:int, quantia:float):
        pass

    def addConta(self, numero:int, titular:str):
        if numero not in self.__contas.keys():
            self.__contas[numero] = Conta(numero,titular)
        else:
            raise OperacaoInvalidaException(f'Conta de numero {numero} já está cadastrada')

    
    def __str__(self):
        s = ''
        cont = 1
        for key in self.__contas.keys():
            s+= f'{cont:02}: {key}, titular {self.__contas[key].titular}, saldo =  {self.__contas[key].saldo}\n'
            cont += 1
        return s