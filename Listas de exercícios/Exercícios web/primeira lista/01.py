# Dado um array de inteiros e o seu número de elementos, inverta a posição dos seus elementos

def invert(array):
    if array == []:
        return []
    aux = array[0]
    array[0] = array[-1]
    array[-1] = aux
    return invert(array[1:-1])

array = [1, 8, 5, 0]
print(invert(array))