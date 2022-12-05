# BUBLE SORT

# 1. Quando dois elementos estão fora de ordem, é feita a inversão e estes são trocados de
# 2. Primeiro elemento é comparado com o segundo, o segundo com o terceiro, o terceiro com o quarto, ... (Inversões são executadas quando necessárias)
# 3. Fim da comparação: quando o penúltimo é comparado com o último (Ao final da varredura, o maior elemento ficará posicionado na última posição)
# 4. O processo continua até que todo o vetor esteja ordenado

# Identifica o maior número e faz ele "flutuar" para o final

def bolha(array):
    for i in range(len(array)-1, 0, -1):
        for j in range(0, i):
            if (array[j] > array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]
                # Efetua a troca

v = [5, 9, 7, 21, 18, 1, 4]
print(v)
bolha(v)
print(v)
'''
print()
a = [25, 48, 37, 12, 57, 86, 33, 92]
print(a)
bolha(a)
print(a)
'''