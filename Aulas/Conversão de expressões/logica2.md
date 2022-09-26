# Formato de expressões aritiméticas

## Infixa
```
(A-B)/(C+D)
```

## Préfixa
* Notação polonesa
```
/-AB+CD
```

## Pósfixa
* Notação polonesa reversa
* Mais eficiente para resolução de expressões aritméticas
```
AB-CD+/
```

# Prioridades

operador | prioridade
---- | ----
( | prioridade 1
_+ , -_ | prioridade 2
_* , /_ | prioridade 3
^ | prioridade 4

# Lógica
1. Inicie com uma pilha vazia
2. Realize uma varredura na expressão **infixa**, a partir do primeiro caractere, enviando todos os operandos encontrados diretamente para a saída.
3. Ao encontrar um operador:
    1. Enquanto a pilha não estiver vazia e houver no seu topo um operador com prioridade maior ou igual ao que está sendo avaliado, desempilhe o operador e copie-o na saída.
    2. Empilhe o operador encontrado.
4. Ao encontrar um parênteses de abertura, empilhe-o.
5. Ao encontrar um parêntese de fechamento, retire um símbolo do topo da pilha e copie-o na saída, até que seja desempilhado em um parênteses de fechamento.
6. Ao final da varredura, esvazie a pilha e envie os símbolos para a saída.

## Exemplo 
```
A * (B + C) / D
```
Caractere | Pilha | Saída
--------- | ----- | -----
A | [ ] | A
_*_ | [ * ] | A
( | [ * , ( ] | A
B | [ * , ( ] | A B
_+_ | [ * , ( , + ] | A B
C | [ * , ( , + ] | A B C
) | [ * ] | A B C +
/ | [ / ] | A B C + *
D | [ / ] | A B C + * D
acabou a expressão | [ ] | A B C + * D /

## Avaliando a expressão
```
ABC+*D/
```
* Da esquerda para a direita, **localize o primeiro operador**. Efetue a operação aritmética com os dois operandos antecessores.
```
ABC+*D/
BC+ = B+C = X
AX*D/
```
* Repita o raciocínio até que não hajam operadores e operandos.
```
AX*D/
AX* = A*X = Y
YD/ = Y/D = Z
```

# Exemplos

Infixa | Pósfixa
-------| -------
A + B * C | A B C * +
A * ( B + C) | A B C + *
(A + B ) / (C – D) | A B + C D - /
(A + B ) / (C – D)* E | A B + C D - / E *
A + B | AB+
A + B – C | AB + C -
(A + B) * ( C – D) | AB + CD - *
A^B * C – D + E / F / (G + H ) | AB ^C * D – EF / GH + / +
((A + B) * C – ( D – E )) ^ (F + G) | AB + C * DE - - FG + ^
A – B / (C * D ^E) | ABCDE^ * / -


### **Exemplo 2**
```
A-B/(C*D^E)
```

Caractere | Pilha | Saída
-- | -- | --
A | [  ] | A
_-_ | [ - ] | A
B | [ - ] | A B
/ | [ - , / ] | A B
( | [ - , / , ( ] | A B
C | [ - , / , ( ] | A B C
_*_ | [ - , / , ( , * ] | A B C
D | [ - , / , ( , * ] | A B C D
^ | [ - , / , ( , * , ^ ] | A B C D
E | [ - , / , ( , * , ^ ] | A B C D E
) | [ - , / ] | A B C D E ^ *
acabou | [ ] | A B C D E ^ * / -
