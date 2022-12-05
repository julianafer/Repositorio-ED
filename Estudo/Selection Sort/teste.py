def selection(array):
    for i in range(len(array)-1):
        min = i
        for j in range(i+1, len(array)):
            if array[j] < array[min]:
                min = j
        array[i], array[min] = array[min], array[i]

v = [4, 8, 3, 1]
print(v)
selection(v)
print(v)