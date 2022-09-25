from Pilha import *
from binario import binario

numeroPilhas = int(input('Número de pilhas: '))
pilhaSelecionada = int(input('Pilha Selecionada: '))
print()

pilhas = [0]*numeroPilhas

for i in range(numeroPilhas):
    pilhas[i] = Pilha()

    for j in range(1,10):
        pilhas[i].empilhar(j*10)

while True:

    print(f'''Editor de Pilha v1.2
=====================================
Pilha Selecionada: {pilhaSelecionada} de {numeroPilhas}
{pilhas[pilhaSelecionada-1]} <- topo
=====================================
(e) Empilhar
(d) Desempilhar
(t) Tamanho
(o) Obter elemento do topo
(v) Teste de pilha vazia
(r) Criar nova Pilha
(n) Inverter os elementos da pilha
(z) Esvaziar a pilha
(c) Concatenar duas pilhas
(m) Escolher outra pilha
(n) Conversão dec/bin
(s) Sair
=====================================''')
    opcao = input('Digite sua opção: ').lower()

    if opcao == 'e':
        dado = int(input('Dado: '))
        pilhas[pilhaSelecionada-1].empilhar(dado)

    elif opcao == 'd':
        try:
            assert pilhas[pilhaSelecionada-1].desempilhar()
        except:
            raise PilhaException('A pilha está vazia!')
    
    elif opcao == 't':
        print('Tamanho:', pilhas[pilhaSelecionada-1].tamanho())

    elif opcao == 'o':
        print('Topo:', pilhas[pilhaSelecionada-1].elementoTopo())

    elif opcao == 'v':
        if pilhas[pilhaSelecionada-1].estaVazia():
            print('Sim')
        else:
            print('Não')

    elif opcao == 'r':
        numeroPilhas += 1
        pilhas.empilhar(Pilha())

    elif opcao == 'n':
        pilhas[pilhaSelecionada-1].inverter()

    elif opcao == 'z':
        pilhas[pilhaSelecionada-1].esvaziar()

    elif opcao == 'c':
        index = int(input('Deseja concatenar com qual pilha? ')) - 1
        outraPilha = pilhas[index]
        pilhas[pilhaSelecionada-1].concatenar(outraPilha)

    elif opcao == 'm':
        pilhaSelecionada = int(input('Nova pilha: '))

    elif opcao == 'n':
        pass
        # pilha = pilhas[pilhaSelecionada-1]
        # for n in pilha:
        #     for b in n:
        #         bin = binario(b)

    else:
        break

    print()
