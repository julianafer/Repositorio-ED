from No import No

def preordem(no):
    if no is None:
        return
    print(f'{no.carga}', end=' ')
    preordem(no.esq)
    preordem(no.dir)

def emordem(no):
    if no is None:
        return
    emordem(no.esq)
    print(f'{no.carga}', end=' ')
    emordem(no.dir)

def posordem(no):
    if no is None:
        return
    posordem(no.esq)
    posordem(no.dir)
    print(f'{no.carga}', end=' ')

def busca(chave, no) -> bool:
    if no is None:
        return False
    if no.carga == chave:
        return True
    if busca(chave, no.esq):
        return True
    else:
        return busca(chave, no.dir)

raiz = No(10)
raiz.esq = No(32)
raiz.dir = No(23)
cursor = raiz.esq # cursor desce para o nó 32
cursor.esq = No(12)
cursor.dir = No(40)
cursor = cursor.esq
cursor.esq = No(5)
cursor = raiz.dir # cursor desce para o nó 23, a partir do raiz
cursor.dir = No(30)
cursor = cursor.dir # cursor desce para o nó 30
cursor.esq = No(60)
cursor = cursor.esq # cursor desce para o nó 60
cursor.dir = No(22)

print('Pre-ordem: ', end='')
preordem(raiz)
print()
print('Em-ordem: ', end='')
emordem(raiz)
print()
print('Pós-ordem: ', end='')
posordem(raiz)
print()