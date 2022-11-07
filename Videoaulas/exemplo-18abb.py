class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, data):
        if self.leftChild == None:
            self.leftChild = Node(data)

    def insertRight(self, data):
        if self.rightChild == None:
            self.rightChild = Node(data)

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setValue(self, newValue):
        self.data = newValue

    def getValue(self):
        return self.data
