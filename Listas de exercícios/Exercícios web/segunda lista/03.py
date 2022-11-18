# Defina a função prim_alg que recebe como argumento um número natural e devolve o primeiro algarismo (o mais significativo) na representação decimal de  n.

def prim_alg(n):
    n = str(n)
    return n if len(n)==1 else prim_alg(n[:-1])

print(prim_alg(234567))
