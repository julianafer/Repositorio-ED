class PilhaException:
    def __init__(self, mensagem):
        super().__init__(mensagem)

class Pilha:
    def __init__(self):
        self.__dados = []

    def empilhar(self, dado):
        self.__dados.append(dado)

    def desempilhar(self):
        return self.__dados.pop()

    def tamanho(self):
        return len(self.__dados)

    def elementoTopo(self):
        index = self.tamanho() - 1
        return f'{self.__dados[index]}'

    def estaVazia(self):
        return len(self.__dados)==0
    
    def esvaziar(self):
        while not self.estaVazia():
            self.desempilhar()

    def inverter(self):
        pilhaAuxiliar = Pilha()
        while not self.estaVazia():
            pilhaAuxiliar.empilhar(self.desempilhar())
        self.__dados = pilhaAuxiliar
        return self.__dados

    def concatenar(self, outraPilha:'Pilha'):
        p_aux = Pilha()
        #a pilha auxiliar vai tirar os elementos da outraPilha
        while not outraPilha.estaVazia():
            p_aux.empilhar(outraPilha.desempilhar())
        #e jogar na self
        while not p_aux.estaVazia():
            self.empilhar(p_aux.desempilhar())

    def __str__(self) -> str:
        return f'{self.__dados}'

