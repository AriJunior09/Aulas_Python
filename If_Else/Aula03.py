print('_________________________    ANÁLISE DE EMPRÉSTIMO PARA COMPRA DE CASA    ____________________')
valor_casa = float(input('Qual o valor da casa: R$ '))
salario = float(input('Qual o salário? R$ '))
qtd_anos = int(input('Em quantos anos que pagar? '))
num_parcelas = (qtd_anos * 12)
valor_parcela = (valor_casa / num_parcelas)
#print('Você vai pagar a casa em {} meses'.format(num_parcelas))
#print('A parcela fica de R$ {:.2f}'.format(valor_parcela))
if valor_parcela <= (salario * 0.3):
    print('\033[36mA sua aquisição foi aprovada!\033[m')
    print('Sua casa no valor de R${:.2f} foi financiada em {} meses com parcelas de R$ {:.2f} por mês!'.format(valor_casa, num_parcelas, valor_parcela))
else:
    print('\033[31mInfelizmente não é possível fazer essa compra agora!')