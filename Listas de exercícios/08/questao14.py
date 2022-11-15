# Dado um vetor de números inteiro, escreva uma função recursiva para identificar o maior valor armazenado no vetor.

def maior(vetor):
    if len(vetor) == 0:
        return

    if len(vetor) == 1:
        return vetor[0]
    elif vetor[0] > vetor[-1]:
        return maior(vetor[:-1])
    else:
        return maior(vetor[1:])

print(maior([1, 9, 6, 3, 29, 5]))