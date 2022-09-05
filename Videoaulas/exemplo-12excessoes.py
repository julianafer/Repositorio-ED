#programa principal

def lerConteudo(fileName):
    stream = open(fileNane, 'rt')
    linhas = stream.readlines()
    stream.close()
    return linhas

while True:
    print('''
    (1) Erro de lógica de Programação
    (2) Erros de condição do ambiente de execução do software
    (3) Erros graves que não permitem recuperação
    --------------------------------------------------''')
    opcao = int(input('opção: '))

    