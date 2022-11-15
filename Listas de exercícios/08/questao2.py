# Faça uma função recursiva chamada printstr() que imprima na tela uma string (caractere a caractere).

def printstr(string = ''):
    # if string == '':
    #     return ''
    # return(f'{string[0]}{printstr(string[1:])}')
    return '' if string == '' else f'{string[0]}{printstr(string[1:])}'

print(printstr('bom dia'))