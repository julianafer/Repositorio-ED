# Examine a função recursiva abaixo e responda o que se pede:

def func1(n):
    # caso base:
    if n == 0:
        return 0
    else:
        return (n % 10 + func1(int(n/10)))

print(func1(35))

# O que vai ser impresso no print(func(35))?
# 8
'''
def func(35):
    passa pelo if
    return (35 % 10 + func(int(35/10)))
    → return (5 + func(3))
    → → return (5 + 3) → 8

def func(3):
    passa pelo if
    return (3 % 10 + func(int(3/10)))
    → return (3 + func(0))
    → → return (3 + 0) → 3

def func(0):
    if n == 0: CAIU NO IF
        retorna 0
'''

# O que essa função faz?

# Reescreva a função sem usar recursividade
'''
solução errada mas o mais próximo que a gente conseguiu
def func2(n):
    while n != 0: #← while inútil??
        x = n % 10
        n = int (n / 10)
        return x + n
print(func2(35))
'''

# Quantas chamadas recursivas serão realizadas?
# Como deu pra ver na questão 1, serão 2 chamadas recursivas porque a primeira chamada é uma chamada normal :)