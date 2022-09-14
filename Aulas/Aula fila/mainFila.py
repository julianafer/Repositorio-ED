from FilaSequencialCircular import Fila

fila = Fila(10)
# teste do vazia
if fila.estaVazia():
    print('Fila está vazia')
# tesde do cheia
if fila.estaCheia():
    print('Fila está cheia')
# tamanho da fila 
print('Tamanho: ', len(fila))
# consultando por elemento
print('Elemento 1:', fila.elemento(1))