#Escolha forma de pagamento
venda = float(input('Informe o valor da venda: '))
#alt+shift para copiar a fila toda.
#Só o alt pega a fila e desce com ela
print("""
ESCOLHA A FORMA DE PAGAMENTO
1 - Pix (12% de desconto)
2 - Débito (8% de desconto)
3 - Crédito (5% de desconto)
4 - Dinheiro (15% de desconto)
""")

opcao = int(input('Escolha uma das opções: '))
desconto = 0

match opcao:
    case 1:
        desconto = venda*0.12
        print(f'\n ---Pagamento no Pix---\n')
    case 2: 
        desconto = venda*0.08
        print(f'\n ---Pagamento no Débito---\n')
    case 3: 
        desconto = venda*0.05
        print(f'\n ---Pagamento no Crédito---\n')
    case 4: 
        desconto = venda*0.15
        print(f'\n ---Pagamento no Dinheiro---\n')
    case _: 
        print('Opção Inválida')
if desconto != 0:
    valor_final = venda - desconto
    print(f'Valor: {venda}')
    print(f'Desconto: {desconto}')
    print(f'Valor com desconto: {valor_final}')
else:
    print('Por favor, informe uma das opções acima.')