def buble(array):
    for i in range(len(array)-1, 0, -1):
        for j in range(0, i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

v = [4, 8, 3, 1]
print(v)
buble(v)
print(v)