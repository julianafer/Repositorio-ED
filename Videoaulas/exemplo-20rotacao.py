def rotacao_esquerda(arvore): # arvore vai ser o p, o nó que tá "desbalanceado"
    aux = arvore.direito
    arvore.direito = aux.esquerdo
    aux.esquerdo = arvore

    return aux


def rotacao_direita(arvore): # arvore vai ser o p, o nó que tá "desbalanceado"
    aux = arvore.esquerdo
    arvore.esquerdo = aux.direito
    aux.direito = arvore

    return aux
