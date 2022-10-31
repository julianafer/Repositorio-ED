# Árvores Binárias de Busca - ABB

* **Qunado for maior vai indo pro lado direito**
* **Quando for menor vai indo pro lado esquerdo**
* Pode decidir o lado de igual mas é melhor na direita

## Remoção de um nó
```
A remoção de qualquer nó deve garantir a propriedade de ordenção da árvore
```
#### Possibilidades de tratamento

* O nó a ser excluído **não contém subárvores**
    * Remove-se apenas o nó em questão

* O nó a ser excluído **contém somente uma subárvore**
    * O pai do nó alvo passa a apontar para seu sucessor

* O nó a ser excluído **contém dois filhos**
    * O filho mais a esquerda, a partir da raiz da subárvore direita, é copiado para o nó alvo


# Calculando a Altura:
```
def altura (self, no) -> int:
    if no is None:
        return 0
    else:
        return 1 + max(altura(no.esq), altura(no.dir))
```