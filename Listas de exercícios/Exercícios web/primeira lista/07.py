# Usando recursividade, calcule a soma de todos os valores de um array de reais.

def soma(array) -> int:
    if len(array) == 0:
        return 0
    return array[0] + soma(array[1:])

array = [1, 8, 5]
print(soma(array))