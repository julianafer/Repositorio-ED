from motor import Motor

class Carro:
    def __init__(self, cor, placa, motor):
        self._cor = cor
        self._placa = placa
        self._motor = motor
    
    def get_motor(self):
        return self._motor
    def set_motor(self, novo_motor):
        self._motor = novo_motor

    def __str__(self):
        return f'Cor: {self._cor}, Placa: {self._placa}, Motor: {self._motor}'


if __name__ == '__main__': #só vai executar se esse programa for o main, ou seja se for ele que eu estiver rodando

    '''motor = Motor(1.8, 'gasolina')''' #também posso fazer isso dentro do próprio carro
    carro = Carro('preto', 'ABC-1234', Motor(1.8, 'gasolina')) #também vai imprimir o __str__ da classe motor, é em cadeia

    '''motor.motorizacao = 3.5''' #só da pra fazer isso quando eu tenho a variável motor
    carro.get_motor().set_motorizacao(3.5)

    print(carro)
