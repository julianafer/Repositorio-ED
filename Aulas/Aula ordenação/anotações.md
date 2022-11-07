# Ordenação de Dados

## Buble Sort
* Identifica o maior número e faz ele "flutuar" para o final

#### Código:

```
def bolha(array):
    for i in range(len(array)-1, 0, -1):
        for j in range(0, i):
            if array[j] > array[j-1]:
                array[j], array[j+1] = array[j+1], array[j]
                # Efetua a troca
```

#### Recursivo:

```
def bolha(array, n):
    if n == 1:
        return
    troca = False
    for j in range(0, n-1):
        if array[j] > array[j-1]:
            array[j], array[j+1] = array[j+1], array[j] # Efetua a troca 
            troca = True
    if not troca: # não houve troca
        return
    bolha(array, n-1)
```

## Selection Sort
* Compara todos com um número específico (o primeiro)

#### Código:

```
def selectionSort(array):
    for i in range(len(array)-1):
        min = 1
        for j in range(i+1, len(array)):
            if array[j] < array[min]:
                min = j
        array[min], array[i] = array[i], array[min] # troca
```

## Insertion Sort
* Vai empurrando os menores para frente e os maiores para trás

#### Código:

```
def insertionSort(array):
    for i in range(1, len(array)):
        chave = array[i]
        j = i-1
        while j>=0 and chave < array[i]:
            array[j+1] = array[j]
            j -= 1
            # perdi o final :(
```