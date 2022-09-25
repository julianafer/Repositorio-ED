class erro(Exception):
  def __init__(self, msg):
    super().__init__(msg)

class Fusca:
  def __init__(self, cor):
    self.__cor = cor

  def perdeuFusca(self, com_fusca:bool):
    if not com_fusca:
      raise erro('Vc não tem um fusca!')

  def __str__(self):
    return f'Fusca {self.__cor}'

if __name__ == '__main__':
  try:
    fusca = Fusca('verde')
    print(fusca)
    fusca.perdeuFusca(False)
  except erro as e:
    print(e)

print('QUERO MEU FUSCA')
