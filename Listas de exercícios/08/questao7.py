#Escreva uma função recursiva que retorne a soma dos n primeiros números inteiros. Se n = 3, a soma seria igual a 1 + 2 + 3 = 6

def soma(numero:int) -> int:
    if numero < 0:
        return -1
    # caso base:
    elif numero == 0:
        return numero
    return numero + soma(numero-1)

print(soma(5))