class Ponto:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

ponto1 = Ponto(1,2)
print('{},{}'.format(ponto1.__x,ponto1.__y)) #tentativa de acesso ao atributo privado fora da classe, vai dar erro
