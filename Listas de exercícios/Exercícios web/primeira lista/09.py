# Escreva uma função recursiva que determine quantas vezes um dígito K ocorre em um número natural N. Por exemplo, o dígito 2 ocorre 3 vezes em 762021192.

def cont(num:int, key) -> int:
    num = str(num)
    if num == '':
        return 0
    elif num[0] == str(key):
        return 1 + cont(num[1:], key)
    else:
        return cont(num[1:], key)

print(cont(11, 1))