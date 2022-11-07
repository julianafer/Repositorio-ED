# Faça uma função recursiva que retorne a soma de todos os elementos de um list de inteiros passado como argumento. O protótipo da função é definido por:

def soma(lista):
    if len(lista) == 0:
        return 0
    return lista[0] + soma(lista[1:])

print(soma([1, 9, 6]))