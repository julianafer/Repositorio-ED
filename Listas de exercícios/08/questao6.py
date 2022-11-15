# Faça uma função recursiva chamada ispalindrome() que retorne verdadeiro caso uma string seja palíndrome, ou falso caso contrário. O protótipo da operação é definido por:

def ispalindrome(str = '') -> bool:
    if str == '':
        return True
    elif str[0] == str[-1]:
        return ispalindrome(str[1:-1])
    return False

print(ispalindrome('ana'))
print(ispalindrome('pao com ovo'))