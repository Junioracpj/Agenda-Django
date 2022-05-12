# VALIDAÇÃO DE VARIAVEL

def validaInt(pergunta, min, max):
    x = int(input(pergunta))
    while x < min or x > max:
        x = int((input(pergunta)))
    return x


# VALIDAÇÃO DE DADO NUMERAL E INTEIRO

while True:
    try:
        comp = int(input('Digite um número : '))
        if comp >= 0:
            break
        else:
            print('Oops! Número inválido, tente novamente...')
    except ValueError:
        print('Você digitou um valor não numérico, tente novamente...')

# VALIDACAO CONDICIONANTE

while True:
    volume = input()
    if volume <= 1000:
        print('faca algo')
    else:
        print('Nao executou')
        continuar = input('Deseja tentar novamente?\n S or N\n>>')
        if continuar.upper() == 'S':
            continue
        else:
            quit()


# CRIAÇÃO LISTAS COM DICIONARIOS

listaCadastro = []
def cadastrarPeca(cp):
    print('Bem vindo ao cadastro de peças')
    print('Código da peça: {}'.format(cp))
    peca = input('Qual o nome da peça:>>')
    fabrica = input('Qual o nome fabricante da peça:>>')
    valor = input('Qual o valor da peça:>>')
    dicionarioPeca = {'CD': cp,
                      'Peca': peca,
                      'Fabricante': fabrica,
                      'Valor': valor}
    listaCadastro.append(dicionarioPeca.copy())