from Pilha import Pilha

numeroPilhas = int(input('Número de pilhas: '))
pilhaSelecionada = int(input('Pilha Selecionada: '))
print()

pilhas = [0]*numeroPilhas

for i in range(numeroPilhas):
    pilhas[i] = Pilha()

    for j in range(1,10):
        pilhas[i].empilhar(j*10)

while True:

    print('Editor de Pilha v1.2')
    print('=====================================')
    print(f'Pilha Selecionada: {pilhaSelecionada} de {numeroPilhas}')
    print(f'{pilhas[pilhaSelecionada-1]} <- topo')
    print('=====================================')
    print('(e) Empilhar')
    print('(d) Desempilhar')
    print('(t) Tamanho')
    print('(o) Obter elemento do topo')
    print('(v) Teste de pilha vazia')
    print('(r) Criar nova Pilha')
    print('(n) Inverter os elementos da pilha')
    print('(z) Esvaziar a pilha')
    print('(c) Concatenar duas pilhas')
    print('(m) Escolher outra pilha')
    print('(n) Conversão dec/bin')
    print('(s) Sair')
    print('=====================================')
    opcao = input('Digite sua opção: ').lower()

    if opcao == 'e':
        dado = int(input('Dado: '))
        pilhas[pilhaSelecionada-1].empilhar(dado)

    elif opcao == 'd':
        pilhas[pilhaSelecionada-1].desempilhar()
    
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
        pilhas.append(Pilha())

    elif opcao == 'n':
        pass

    elif opcao == 'z':
        pilhas[pilhaSelecionada-1].esvaziar()

    elif opcao == 'c':
        pass

    elif opcao == 'm':
        pilhaSelecionada = int(input('Nova pilha: '))

    elif opcao == 'n':
        pass

    else:
        break

    print()
