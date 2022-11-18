# Defina a função media_digitos que recebe como argumento um número natural e devolve a média dos seus digitos.

def media_digitos(n:int) -> float:
    n = str(n)
    if n == '':
        return 0
    return ((int(n[0]) + media_digitos(n[1:])) / len(n))

print(media_digitos(1234))
