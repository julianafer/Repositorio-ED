class Motor:
    def __init__(self, motorizacao, combustivel='flex'):
        self._motorizacao = motorizacao
        self._combustivel = combustivel

    def get_motorizacao(self):
        return self._motorizacao

    def set_motorizacao(self, nova_motorizacao):
        self._motorizacao = nova_motorizacao

    #Fazer o mesmo para 'combustível'

    def __str__(self):
        return f'Motor: {self._motorizacao}L, Combustível: {self._combustivel}'

if __name__ == '__main__': #só vai executar se esse programa for o main, ou seja se for ele que eu estiver rodando
    motor = Motor(2.0)

    motor.set_motorizacao(3.5)
    print(motor.get_motorizacao())
