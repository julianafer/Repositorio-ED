# Implemente uma função recursiva que, dados dois números inteiros x e n, calcula o valor de xn.

def multiplicacao(x, n):
    if x==0 or n==0:
        return 0
    return multiplicacao(x, n-1) + x

print(multiplicacao(9, 8))