class No:
    def __init__(self, carga:any):
        self.carga = carga
        self.esq = None
        self.dir = None

    def __str__(self) -> str:
        return f'{self.carga}'

# QUESTÂO 2
raiz = No(1)
raiz.esq = No(2)
raiz.esq.esq = No(4)
raiz.dir = No(3)
raiz.dir.esq = No(5)
raiz.dir.dir = No(6)

# QUESTÃO 3
def preordem(no):
    if no is None:
        return
    print(f'{no.carga}', end=' ')
    preordem(no.esq)
    preordem(no.dir)

preordem(raiz)

# QUESTÂO 4
