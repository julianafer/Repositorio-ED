from Pais import Pais

p1 = Pais('Brasil', 'Brasília', 8516000)
p2 = Pais('Argentina', 'Buenos Aires', 2780000)

print(p1)
print(p2)
print(p1.vizinhos)
print(p2.vizinhos)
p1.addPaisDeFronteira('Uruguai')
p1.addPaisDeFronteira('Argentina')
p1.addPaisDeFronteira('Paraguai')
p1.addPaisDeFronteira('Peru')
p1.addPaisDeFronteira('Peru')
print(p1.vizinhos)
