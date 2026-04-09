# Math Case
print("""
[1] - Marketing
[2] - Financeiro
[3 a 5] - ADM
[6 a 9] - TI
[10] - Seviços Gerais
""")
codigo = int(input('Digite o código de acesso: '))

match codigo:
    case 1:
        print('Marketing')
    case 2:
        print('Financeiro')
    case 3 | 4 | 5:
        print('ADM')
    case 6 | 7 | 8 | 9:
        print('TI')
    case 10:
        print('Seviços Gerais')
    case _:
        print('Acesso Negado')

##########################################

