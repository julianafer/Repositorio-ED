# FILA SEQUENCIAL CIRCULAR

class FilaException(Exception):
  def __init__(self, msg):
    super().__init__(msg)


class Fila:
  def __init__(self, tamanho:int = 10):
    self.__inicio = 0
    self.__final = -1
    self.__tamanho = tamanho
    self.__ocupados = 0
    #self.__dados = [None]*tamanho
    self.__dados = ['-' for i in range(tamanho)]

  def estaVazia(self):
    return self.__ocupados == 0

  def estaCheia(self):
    return self.__ocupados == self.__tamanho

  def enfileirar(self, dado):
    if self.estaCheia():
      raise FilaException('E banheire des não bináres está cheie!')
    else:
      self.__inicio = self.__inicio % self.__tamanho
      self.__dados[self.__inicio] = dado
      self.__ocupados += 1
      self.__inicio += 1

  def desenfileirar(self):
    if self.estaVazia():
      raise FilaException('Não tem ninguém ne banheire des não bináres para expulsar!!')
    self.__final += 1
    self.__dados.pop(self.__final)
    self.__dados.insert(self.__final, '-')
    self.__ocupados -= 1

  def __str__(self) -> str:
    s = 'Banheiro dos não bináres:[ '
    for i in self.__dados:
      s += f'{i} '
    s +=']'
    return f'{s}'



if __name__ == '__main__':

  try:
    fc = Fila()
    print(fc)
    fc.enfileirar(0)
    fc.enfileirar(1)
    fc.desenfileirar()
    fc.enfileirar(2)
    fc.enfileirar(3)
    fc.enfileirar(4)
    fc.enfileirar(5)
    fc.enfileirar(6)
    fc.desenfileirar()
    fc.enfileirar(7)
    fc.enfileirar(8)
    fc.enfileirar(9)
    print(fc)
    fc.enfileirar(0)
    print(fc)
  except FilaException as fe:
    print(f'ERRO: {fe}')
