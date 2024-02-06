print('___________________________    PRODUTO COM DESCONTO OU ACRÉSCIMO   _____________________\n')
valor = float(input('Digite o valor do produto: R$ '))
print('1 - A vista no Dinheiro ou Pix - 10% de Desconto')
print('2 - A vista no Cartão          - 5% de Desconto')
print('3 - Parcelado no Cartão em 2x  - Preço normal')
print('4 - Parcelado no Cartão em 3x  - 4% de Juros\n')
forma = input('Escolha a forma de pagamento: ')
opcoes = ['1', '2', '3', '4']
while forma not in opcoes:
    print('Favor digite uma opção válida!')
    forma = input('Escolha a forma de pagamento: ')
if forma == '1':
    valor = (valor - (valor * 0.1))
    print('O valor final ficou em \033[36mR$ {:.2f}'.format(valor))
elif forma == '2':
    valor = (valor - (valor * 0.05))
    print('O valor final ficou em \033[36mR$ {:.2f}'.format(valor))
elif forma == '3':
    print('O valor final ficou em \033[36mR$ {:.2f}'.format(valor))
elif forma == '4':
    valor = (valor + (valor * 0.04))
    print('O valor final ficou em \033[36mR$ {:.2f}'.format(valor))
    print('Serão 3 parcelas de R$ {:.2f}'.format((valor/3)))