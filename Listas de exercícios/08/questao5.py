# Faça uma função recursiva chamada compareStr(char *str1, char *str2) que retorne:
# 0: str1 é igual a str2;
# 1: str1 é maior que str2;
# -1: str1 é menor que str2;

def compareStr(str1='', str2=''):
    if str1 == '' and str2 == '':
        return 0
    elif str1 == '':
        return -1
    elif str2 == '':
        return 1
    else:
        return compareStr(str1[:-1], str2[:-1])

# Resolução do professor que é por ordem alfabética, não por tamanho de string
'''
def compareStr(s1, s2):
    if(s1 == '' and s2 == ''):
        return 0
    elif (s1[0] == s2[0]):
        return compareStr(s1[1:], s2[1:])
    elif (s1[0] > s2[0]):
        return 1
    else:
        return -1
'''

print(compareStr('o', 'oi'))
print(compareStr('oi', 'oi'))
print(compareStr('oie', 'oi'))
