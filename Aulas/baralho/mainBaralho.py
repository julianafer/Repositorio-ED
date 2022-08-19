from Baralho import Baralho

def embaralhar():
    print('função embaralhar()')

embaralhar()

baralho = Baralho(True)
# for i in range(53):
while (baralho.temCarta()):
    carta = baralho.retirarCarta()
    print(carta)

print('Não há mais cartas a serem retiradas')

print('Total de cartas no baralho:',len(baralho))
baralho.receberCarta(carta)
baralho.receberCarta(carta)
print('Total de cartas no baralho:',len(baralho))
print(baralho)

baralho2 = Baralho()
for i in range(42):
    baralho2.retirarCarta()
print('Baralho 2\n')
print(baralho2)

print('fazer o baralho 1 receber as cartas do 2')
baralho.juntarBaralho(baralho2)
print(baralho)
print(len(baralho))
print(len(baralho2))