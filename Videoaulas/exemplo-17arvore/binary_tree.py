class BinaryTree:
    def em_ordem(self, arvore):
        if arvore is not None:
            self.em_ordem(arvore.esq)
            print(arvore.dado, end=' ') #visita a raíz
            self.em_ordem(arvore.dir)