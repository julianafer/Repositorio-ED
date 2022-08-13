class Carro:
    def __init__(self, velocidade, cor):
        self.velocidade = velocidade
        self.resistencia = 0
        self.combustivel = 0
        self.cor = cor
    
    def print(self):
        print('velocidade:',self.velocidade)
        print('cor:',self.cor)