# SELECTION SORT

# 1. Selecione o primeiro elemento (i=0) do array
# 2. A partir de i+1, faça a varredura do array e identifique o valor que é menor ao que está armazenado no primeiro elemento
# 3. Troque o valor armazenado no índice do primeiro elemento por aquele determinado como o menor valor
# 4. Ao final da varredura, o menor elemento estará posicionado na primeira posição
# 5. Repetir o procedimento para os n-1 elementos restantes (i = 1, 2, 3, ..., n-1)

def selectionSort(array):
    for i in range(len(array)-1):
        min = i
        for j in range(i+1, len(array)):
            if(array[j] < array[min]):
                min = j
        array[min], array[i] = array[i], array[min]
        # troca

v = [5, 9, 7, 21, 18, 1, 4]
print(v)
selectionSort( v )
print(v)
'''
print()
a = [25, 48, 37, 12, 57, 86, 33, 92]
print(a)
selectionSort(a)
print(a)
'''