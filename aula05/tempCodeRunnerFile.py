# Faixa etária
idade = int(input('Informe a idade da pessoa: '))

match idade:
    case j if 0 <= j < 12:
        print('Criança')
    case j if 12 <= j <18:
        print('Adolescente')
    case j if j>=18:
        print('Adulto')
    case _:
        print('Idade Inválida') 