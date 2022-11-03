# Faça uma função recursiva chamada printInverse() que imprima uma string ao contrário

def printInverse(string = ''):
    # if string == '':
    #     return ''
    # return (f'{string[-1]}{printInverse(string[:-1])}')
    return '' if string == '' else f'{string[-1]}{printInverse(string[:-1])}'

print(printInverse('socorram me subi no onibus em marrocos'))