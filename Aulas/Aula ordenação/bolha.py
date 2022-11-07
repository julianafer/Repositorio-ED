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

array = [4, 3, 7, 9, 22, 13, 63, 0]
bolha(array, len(array))
print(array)
# não funciona noggers