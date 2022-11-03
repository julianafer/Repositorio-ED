class ExceptionPilha(Exception):
  def __init__(self, mensagem):
    super().__init__(mensagem)

class Pilha:
  def __init__(self):
    self.__dados = []

  def empilhar(self, dado):
    self.__dados.append(dado)

  def desempilhar(self):
    if not self.estaVazia():
      self.__dados.pop()
    else:
      raise ExceptionPilha('A pilha está vazia!')

  def estaVazia(self)-> bool:
    return len(self.__dados) == 0
    
  def esvaziar(self):
    while not self.estaVazia():
      self.desempilhar()

  def tamanho(self):
    return len(self.__dados)
      

  def __str__(self):
    return f'Pilha: {self.__dados}'


if __name__ == "__main__":
  
  try:
    p1 = Pilha()

    p1.empilhar(20)
    p1.empilhar(30)
    p1.empilhar(40)
    print(p1)
    p1.desempilhar()
    print(p1)
    print(p1.tamanho())
    p1.esvaziar()
    print(p1)
    p1.esvaziar()
    p1.desempilhar()
  except ExceptionPilha as ep:
    print(f'ERRO: {ep}')
    