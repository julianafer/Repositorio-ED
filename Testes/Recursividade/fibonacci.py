# Sequência de Fibonacci
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

def fibonacci(n):
    # casos base
    if (n == 0) or (n == 1):
        return n
    return (fibonacci(n-1) + fibonacci(n-2))

print(fibonacci(7))

# como funciona
'''
def fibonacci(7):
    passa pelo if
    return (fibonacci(6) + fibonacci(5))
    return (8 + 5)
        RETORNA 13

def fibonacci(6):
    passa pelo if
    return (fibonacci(5) + fibonacci(4))
    return (5 + 3)
        RETORNA 8

def fibonacci(5):
    passa pelo if
    return (fibonacci(4) + fibonacci(3))
    return (3 + 2)
        RETORNA 5

def fibonacci(4):
    passa pelo if
    return (fibonacci(3) + fibonacci(2))
    return (2 + 1)
        RETORNA 3

def fibonacci(3):
    passa pelo if
    return (fibonacci(2) + fibonacci(1))
    return (1 + 1)
        RETORNA 2

def fibonacci(2):
    passa pelo if
    return (fibonacci(1) + fibonacci(0))
    return (1 + 0)
        RETORNA 1

def fibonacci(1):
    if (n == 0) or (n == 1): CAIU NO IF
        RETORNA 1

def fibonacci(0):
    if (n == 0) or (n == 1): CAIU NO IF
        RETORNA 0
'''