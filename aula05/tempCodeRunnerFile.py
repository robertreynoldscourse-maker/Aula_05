
nota_aluno = float(input('Informe a nota do aluno: '))
frequencia = float(input('Informe a frequência do aluno: '))

porcentagem_frequencia = frequencia / 100

if nota_aluno >= 7:
    # Aprovado por nota, mas precisa checar a frequência
    if porcentagem_frequencia >= 0.75:
        print('Aluno aprovado por Nota e Frequência.')
    else:
        print('Reprobado por frequência baixa.')
else:
    print('Reprobado por nota baixa.')