from No import No

class ArvoreBinaria:
    def __init__(self, carga_da_raiz:any = None):
        # self.__raiz = No(carga_da_raiz) if carga_da_raiz != None else carga_da_raiz
        if carga_da_raiz != None:
            self.__raiz = No(carga_da_raiz)
        else:
            self.__raiz = carga_da_raiz
        # não entendi essa par5te, na minha cabeça devia ser ao contrário

    def criarRaiz(self, carga_da_raiz:any):
        if self.__raiz is None:
            self.__raiz = No(carga_da_raiz)
            # isso aqui fez bem mais sent8ido, mas ainda não entendi porque tem esse criarRaiz se o __init__ já tá meio que fzendo isso

    def estaVazia(self) -> bool:
        return self.__raiz == None

    def getRaiz(self) -> any:
        if self.__raiz is not None:
            return self.__raiz.carga
        else:
            return None

    def preordem(self):
        self.__preordem(self.__raiz)
        # não entendo porque os percursos tem 2 métodos

    def __preordem(self, no):
        if no is None:
            return
        print(f'{no.carga}', end=' ')
        self.__preordem(no.esq)
        self.__preordem(no.dir)

    def emordem(self):
        self.__emordem(self.__raiz)

    def __emordem(self, no):
        if no is None:
            return
        self.__emordem(no.esq)
        print(f'{no.carga}', end=' ')
        self.__emordem(no.dir)

    def posordem(self):
        self.__posordem(self.__raiz)

    def __posordem(self, no):
        if no is None:
            return
        self.__posordem(no.esq)
        self.__posordem(no.dir)
        print(f'{no.carga}', end=' ')

    def add(self, carga:any):
        if self.__raiz == None:
            self.__raiz = No(carga)
            # outro método pra adicionar na raiz??
        else:
            self.__add(carga, self.__raiz)
            # pelo visto não são só os métodos de percorrer que tem 2 métodos

    def __add(self, carga:any, node:'No'):
        if carga < node.carga:
            if node.esq != None:
                self.__add(carga, node.esq)
            else:
                node.esq = No(carga)
        else:
            if node.dir != None:
                self.__add(carga, node.dir)
            else:
                node.dir = No(carga)