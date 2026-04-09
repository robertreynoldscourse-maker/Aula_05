
## IF encadeado
print('IF encadeado')
nota = float(input('Informe a nota do aluno: '))

if nota >= 9:
    print('A')
elif nota >= 7:
    print('B')
elif nota >= 5:
    print('C')
elif nota >= 3:
    print('D')
else:
    print('E')

print('------------------------------------------')
# IF não encadeado
print('IF não encadeado')
nota = float(input('Informe a nota do aluno: '))
if nota >= 9:
    print('A')
if nota >= 7:
    print('B')
if nota >= 5:
    print('C')
if nota >= 3:
    print('D')
else:
    print('E')

print('------------------------------------------')

# IF aninhados

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