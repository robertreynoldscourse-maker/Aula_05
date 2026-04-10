numero = float(input('Digite um número qualquer: '))

match numero:
    case i if i < 0:
        print('O número é negativo.')
    case i if i == 0:
        print('O número é neutro.')
    case i if i > 0:
        print('O número é positivo.')