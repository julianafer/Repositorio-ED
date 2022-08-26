notas = [7.0,8.0,9.0,10.0]

while(True):
    try:
        index = int(input('Digite o índice referente a nota: '))

        if index < 0:
            break

        print('Nota:', notas[index], '\n')

        if index == 1:
            raise FileNotFoundError('Erro na abertura do arquivo.')

        print('Nota dividido pelo índice:', notas[index]/index, '\n')

    except ValueError as ve:
        print('Índice inválido. Digite um número inteiro.')
        print('Mensagem embutida:', ve)

        print(ve)
    except IndexError as ie:
        print(f'Erro: Digite um número entre 0 e {len(notas)}')
        print('Mensagem embutida:', ie)

    except ZeroDivisionError as ze:
        print('Erro: A divisão não pode ser realizada por 0')
        print('Mensagem embutida:', ze)

    except BaseException as e: # BaseException
        print('\nDeu erro')
        print('Exceção responsável:', e.__class__.__name__)
        print('Mensagem da exceção:', e)
    
    print('Valeu, vamos à próxima interação.')

print('Fim do programa.')
