# Faça uma função recursiva chamada printInverse() que imprima uma string ao contrário

def printInverse(string = ''):
    if string == '':
        return ''
    else:
        # não sei como funciona, só sei que funciona
        printInverse(string[1:])
        print(f'{string[0]}',end='')

printInverse('salve')