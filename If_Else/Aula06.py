print('_________________________    CALCULANDO O IMC    ____________________')
altura = float(input('Digite sua altura em metros: '))
peso = float(input('Digite o seu peso em Kgs: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('\033[31mAbaixo do Peso!')
elif imc < 25:
    print('\033[36mPeso ideal!')
elif imc < 30:
    print('\033[33mSobrepeso!')
elif imc < 40:
    print('\033[33mObesidade!')
else:
    print('\033[31mObesidade Mórbida!')