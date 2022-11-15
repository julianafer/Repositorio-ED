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


    def __count(self, no:No) -> int:
        if no is None:
            return 0
        return 1 + self.__count(no.esq) + self.__count(no.dir)
    
    def __len__(self):
        return self.__count(self.__raiz)

    
    def busca(self, chave:any):
        return self.__busca(chave, self.__raiz)

    def __busca(self, chave, no:No):
        if no is None:
            return False
        if chave == no.carga:
            return True
        elif (chave < no.carga) and (no.esq != None):
            return self.__busca(chave, no.esq)
        elif (chave > no.carga) and (no.dir != None):
            return self.__busca(chave, no.dir)
        else:
            return False
            

    def removeNo(self, chave:any):
        if self.__raiz is None:
            return None
        if chave == self.__raiz.carga:
            if (self.__raiz.esq is None) and (self.__raiz.dir is None):
                self.__raiz = None
                return None # não entendi pq retorna
            elif self.__raiz.esq is None: # no original ele usa if normal mas acho q n faz diferença
                self.__raiz = self.__raiz.dir
                return self.__raiz.carga # tbm n entendi
            elif self.__raiz.dir is None:
                self.__raiz = self.__raiz.esq
                return self.__raiz.carga
        retorno = self.__removeNo(self.__raiz, chave)
        return retorno.carga

    def __removeNo(self, no, chave):
        if no is None:
            return None
        '''Se a chave a ser deletada é menor do que a chave do nó raiz (da vez), então a chave se encontra na subárvore esquerda'''
        if chave < no.carga:
            no.esq = self.__removeNo(no.esq, chave)
        elif chave > no.carga:
            no.dir = self.__removeNo(no.dir, chave)
        else:
            ''' (1) Nó com apenas 1 ou 0 filho '''
            if no.esq is None:
                temp = no.dir
                no = None
                return temp # não entendi
            elif no.dir is None:
                temp = no.esq
                no = None
                return temp
            ''' (2) Nó com dois filhos: obtem o sucessor emordem (o menor nó da subárvore direita) '''
            temp = self.__minValueNode(no.dir)
            '''copia o conteúdo do sucessor emordem para esté nó'''
            no.carga = temp.carga
            '''deleta o sucessor emordem'''
            no.dir = self.__removeNo(no.dir, temp.carga)
        return no


    def __minValueNode(self, no:'No'):
        cursor = no
        while cursor.esq is not None:
            cursor = cursor.esq
        return cursor

    # def __maxValueNode(self, no:'No'):
    #     cursor = no
    #     while cursor.dir is not None:
    #         cursor = cursor.dir
    #     return cursor

    
    def __go(self, chave:int, no:No) -> No: # não entendi o que esse método faz
        if no is None:
            return None
        elif no.carga == chave:
            return no
        resultado = self.__go(chave, no.esq)
        if resultado: # ???
            return resultado
        else:
            return self.__go(chave, no.dir)
