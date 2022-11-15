# Faça uma função recursiva chamada recursiveLength() que retorne a quantidade de caracteres de um string.

def recursiveLength(string = '') -> int:
    # if string == '':
    #     return 0
    # return (1 + recursiveLength(string[:-1]))
    return 0 if string == '' else 1 + recursiveLength(string[:-1])

print(recursiveLength('abacate'))