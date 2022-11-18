# Defina a função div que recebe como argumentos dois números naturais  m  e  n  e devolve o resultado da divisão inteira de  m  por  n . Neste exercício não pode recorrer às operações aritméticas de multiplicação, divisão e resto da divisão inteira.

def div(m:int, n:int) -> int:
    if m < n:
        return 0
    elif m == 0:
        return 0

    return div(m-n, n) + 1

print(div(7,2))
print(div(3,4))
