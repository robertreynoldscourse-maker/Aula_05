
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