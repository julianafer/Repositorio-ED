
class No:
  def __init__(self, carga:int):
    self.carga = carga
    self.ant = None

  def __str__(self):
    return f'{self.carga}'

  
class Pilha:
  def __init__(self):
    self.__topo = None
    self.__tamanho = 0

  def empilhar(self, conteudo):
    novo = No(conteudo)
    novo.ant = self.__topo
    self.__topo = novo
    self.__tamanho += 1

  def desempilhar(self):
    carga = self.__topo.ant
    self.__topo = self.__topo.ant
    self.__tamanho -= 1
    return carga

  def __str__(self):
    s = 'topo -> [ '
    cursor = self.__topo
    while(cursor != None):
      s+= f'{cursor.carga} '
      cursor = cursor.ant
    s += ']'
    return s


if __name__ == '__main__':

  p1 = Pilha()
  for i in range(1,10):
    p1.empilhar(i*10)
  print(p1)
  p1.desempilhar()
  p1.desempilhar()
  print(p1)

'''
p1 = 1 4 8 2
p2 = 0 6 4 2
p2.concatenar(p1)
0 6 4 2 1 4 8 2
p1.concatenar(p2)
1 4 8 2 0 6 4 2
'''