# Faça uma função recursiva chamada invertString() que imprima uma string ao contrário

def invertString(string = ''):
    # if string == '':
    #     return ''
    # return (f'{string[-1]}{invertString(string[:-1])}')
    return '' if string == '' else f'{string[-1]}{invertString(string[:-1])}'
    # return invertString(s[1:]) + s[0]

print(invertString('socorram me subi no onibus em marrocos'))