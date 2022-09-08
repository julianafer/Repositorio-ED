class Conta:
    #construtor parametrizado da classe
    def __init__(self, agencia, conta):
        self.agencia = agencia
        self.conta = conta
        self.digito = self.__geraDigito(conta)
        self.saldo = 0

    #método de instância público
    def sacar(self, valor):
        pass
