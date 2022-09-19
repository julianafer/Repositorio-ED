from PilhaSequencial import *

p1 = Pilha()
p2 = Pilha()

for i in range(1,20,3):
    p1.empilha(i)

for i in range(30,36):
    p2.empilha(i)

p2.concatena(p1)

print('Concatena P1 e P2')
print('P1:', p1)
print('P2:', p2)
