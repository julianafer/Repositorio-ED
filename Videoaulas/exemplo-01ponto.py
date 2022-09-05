#introdução a objetos
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

ponto1 = Ponto(1,2)
print('Coordenadas do Ponto 1 (%d,%d)' %(ponto1.x, ponto1.y))

ponto2 = Ponto(5,5)
print('Coordenadas do Ponto 2 (%d,%d)' %(ponto2.x, ponto2.y))
