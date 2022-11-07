# Conversão de expressões

## **Infixa**
### operadores entre os operandos

```
(A-B) / (C+D)
```

## **Pósfixa**
### operadores após os operandos

```
A*(B+C)/D
```

Caractere | Pilha | Saída
--------- | ----- | -----
A | [ ] | A
.* | [ * ] | A
( | [ * ( ] | A
( | [ * ( ] | A
B | [ * ( ] | A B
.+ | [ * ( + ] | A B
C | [ * ( + ] | A B C
) | [ * ] | A B C +
/ | [ / ] | A B C + * _=> y_
D | [ / ] | y D /

_ponto na frente do + e do * só pra deixar a tabela certinha_

```
A+B/(C*D^E)
```

Caractere | Pilha | Saída
--------- | ----- | -----
A | [ ] | A
.+ | [ + ] | A
B | [ + ] | AB
/ | [ + / ] | AB
( | [ + / ( ] | AB
C | [ + / ( ] | ABC
.* | [ + / ( * ] | ABC
D | [ + / ( * ] | ABCD
^ | [ + / ( * ^ ] | ABCD
E | [ + / ] | ABCDE^*/+
) | [ ] | 

_ponto na frente do + e do * só pra deixar a tabela certinha_

## **Préfixa**
### operadores antes dos operandos
