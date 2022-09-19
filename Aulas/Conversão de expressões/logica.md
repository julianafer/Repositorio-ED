# Conversão de expressões

## **infixa**
operadores entre os operandos

```
(A-B) / (C+D)
```

## **pósfixa**
operadores após os operandos

```
A*(B+C)/D
```

Caractere | Pilha | Saída
--------- | ----- | -----
A | [ ] | A
* | [ * ] | A
( | [ * ( ] | A
( | [ * ( ] | A
B | [ * ( ] | A B
+ | [ * ( + ] | A B
C | [ * ( + ] | A B C
) | [ * ] | A B C +
/ | [ / ] | A B C + * _=> y_
D | [ / ] | y D /

```
A+B/(C*D^E)
```

Caractere | Pilha | Saída
--------- | ----- | -----
A | [ ] | A
+ | [ + ] | A
B | [ + ] | AB
/ | [ + / ] | AB
( | [ + / ( ] | AB
C | [ + / ( ] | ABC
* | [ + / ( * ] | ABC
D | [ + / ( * ] | ABCD
^ | [ + / ( * ^ ] | ABCD
E | [ + / ] | ABCDE^*/+
) | [ ] | 

## **préfixa**
operadores antes dos operandos
