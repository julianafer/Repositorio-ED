#introdução a métodos
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def quadrante(self): #método que retorna a informação sobre qual quadrante o ponto pertence
        if (self.x > 0) and (self.y > 0):
            return '1º quadrante'
        elif (self.x < 0) and (self.y > 0):
            return '2º quadrante'
        elif (self.x < 0) and (self.y < 0):
            return '3º quadrante'
        elif (self.x > 0) and (self.y < 0):
            return '4º quadrante'
        else:
            return 'nenhum dos quadrantes'

ponto1 = Ponto(1,2)
print('Coordenadas do Ponto 1 (%d,%d)' %(ponto1.x, ponto1.y))
print('Ponto 1 pertence a %s' %(ponto1.quadrante())) #enviando mensagem ao objeto ponto!, solicitando que ele informe seu quadrante
