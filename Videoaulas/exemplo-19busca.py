def search(self, key):
    if self.__root != None:
        return self.searchData(key, self.__root)
    else:
        return None

def searchData(self, key, node):
    if key == node.data:
        return node
    elif (key < node.data) and (node.left != None):
        return self.searchData(key, node.left)
    elif (key > node.data) and (node.right != None):
        return self.searchData(key, node.right)
    else:
        return None

# era pra ser __searchData mas eu tirei o __