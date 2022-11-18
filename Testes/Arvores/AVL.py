class No:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return f'{self.carga}'

class AVLTree:
    def __init__(self, value):
        if value is None:
            self.__root = None
        else:
            self.__root = self.insert(value)

    def isEmpty(self) -> bool:
        return self.__root == None

    def insert(self, key):
        if self.__root == None:
            self.__root = No(key)
        else:
            self.__root = self.__insert(self.__root, key)

    def __insert(self, root, key):
        if not root:
            return No(key)
        elif key < root.value:
            root.left = self.__insert(root.left, key)
        else:
            root.right = self.__insert(root.right, key)
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)
        # caso 1 → rotação a direita
        if (balance > 1) and (key < root.left.value):
            return self.__rightRotate(root)
        # caso 2 → rotação a esquerda
        if (balance < -1) and (key > root.right.value):
            return self.__leftRotate(root)
        # caso 3 → rotação dupla a direita
        if (balance > 1) and (key > root.left.value):
            root.left = self.__leftRotate(root.left)
            return self.__rightRotate(root)
        # caso 4 → rotação dupla a esquerda
        if (balance < -1) and (key < root.right.value):
            root.right = self.__rightRotate(root.right)
            return self.__leftRotate(root)
        return root

    def __leftRotate(self, p):
        u = p.right
        t2 = u.left
        u.left = p
        p.right = t2
        p.height = 1 + max(self.getHeight(p.left), self.getHeight(p.right))
        u.height = 1 + max(self.getHeight(u.left), self.getHeight(u.right))
        # return the new root
        return u

    def __rightRotate(self, p):
        u = p.left
        t2 = u.right
        u.right = p
        p.left = t2
        p.height = 1 + max(self.getHeight(p.left), self.getHeight(p.right))
        u.height = 1 + max(self.getHeight(p.left), self.getHeight(p.right))
        # return the new root
        return u

    def getHeight(self, no) -> int:
        if no is None:
            return 0
        return no.height # não entendi mais nada