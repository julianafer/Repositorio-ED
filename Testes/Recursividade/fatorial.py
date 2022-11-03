# solução "normal"
'''
def fatorial(n):
    if n == 0:
        return 1
    fat = 1
    for i in range(n, 0, -1):
        fat *= i
    return fat
'''

# SOLUÇÃO RECURSIVA
def fatorial(n):
    # caso base:
    if n == 0:
        return 1
    return (n * fatorial(n-1))

print(fatorial(4))

# como funciona: (pilha)
'''
n = 4
def fatorial(4):
    if 4 == 0: (passa pelo if)
    return (4 * fatorial(4-1 = 3))

def fatorial(3):
    if 3 == 0: (passa pelo if)
    return (3 * fatorial(3-1 = 2))

def fatorial(2):
    if 2 == 0: (passa pelo if)
    return (2 * fatorial(2-1 = 1))

def fatorial(1):
    if 1 == 0: (passa pelo if)
    return (1 * fatorial(1-1 = 0))

def fatorial(0):
    if 0 == 0: (CAIU NO IF)
        return 1
'''
# finalmente retornou algo, então volta a pilha
'''
def fatorial(0):
    RETORNOU 1

def fatorial(1):
    return (1 * 1) → RETORNOU 1

def fatorial(2):
    return (2 * 1) → RETORNOU 2

def fatorial(3):
    return (3 * 2) → RETORNOU 6

def fatorial(4):
    return (4 * 6) → RETORNOU 24

ACABOU A FUNÇÃO!!
'''
