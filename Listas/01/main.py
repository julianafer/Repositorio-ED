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
    print(f'{pilhas[pilhaSelecionada]} <- topo')
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
        pilhas[pilhaSelecionada].empilhar(dado)

    elif opcao == 'd':
        pilhas[pilhaSelecionada].desempilhar()
    
    elif opcao == 't': #não tá pegando
        pilhas[pilhaSelecionada].tamanho()

    elif opcao == 'o':
        pilhas[pilhaSelecionada].elementoTopo()

    elif opcao == 'v':
        pilhas[pilhaSelecionada].estaVazia()

    elif opcao == 'r':
        numeroPilhas += 1
        pilhas[numeroPilhas] = Pilha()

    elif opcao == 'n':
        pass

    elif opcao == 'z':
        pilhas[pilhaSelecionada].esvaziar()

    elif opcao == 'c':
        pass

    elif opcao == 'm':
        pilhaSelecionada = int(input('Nova pilha: '))

    elif opcao == 'n':
        pass

    else:
        break