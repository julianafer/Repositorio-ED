from Pilha import *

def binario(alvo: int):
    bin = Pilha()
    i = alvo
    if alvo == 0:
        out = '0'
    else:                    
        while i != 0:
            bin.empilhar(i % 2)
            i = i // 2                    
        out = ''
        while not bin.estaVazia():
            out+=f'{bin.desempilhar()}'

    return out


if __name__ == '__main__':

    print(binario(0))
    print(binario(1))
    print(binario(5))
    print(binario(10))
    print(binario(256))
    print(binario(511))
    print(binario(512))