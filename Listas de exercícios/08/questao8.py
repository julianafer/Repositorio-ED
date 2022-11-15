# Faça uma função recursiva chamada menores_rec() que receba como parâmetro um list de valores numéricos e um número inteiro key. A função deve retornar quantos elementos da lista possuem valor inferior a key. O protótipo da função é definido por:0

def menores_rec(lista, key:int) -> int:
    if len(lista) == 0:
        return 0
    elif lista[0] < key:
        return 1 + menores_rec(lista[1:], key)
    else:
        return menores_rec(lista[1:], key)

lista = [1, 0, 2, 1, 7, 3]
print(menores_rec(lista, 2))