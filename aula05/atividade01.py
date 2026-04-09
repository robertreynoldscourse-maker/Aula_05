print("""
[1] - Sul
[2] - Norte
[3] - Leste
[4] - Oeste
[5 | 6] - Nordeste
[7 | 8 | 9] - Sudeste
[10] - Centro - Oeste
[11] - Noroeste
""")
codigo = int(input('Digite o código de origem do produto: '))

match codigo:
    case 1:
        print('Sul')
    case 2:
        print('Norte')
    case 3:
        print('Leste')
    case 4:
        print('Oeste')
    case 5 | 6:
        print('Nordeste')
    case 7 | 8 | 9:
        print('Sudeste')
    case 10:
        print('Centro - Oeste')
    case 11:
        print('Noroeste')
    case _:
        print('Importado')