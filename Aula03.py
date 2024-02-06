print('_______________    MOSTRA O PRIMEIRO NÚMERO ATÉ O ÚLTIMO PULANDO DE ACORDO COM O PASSO    _________')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f+1, p):
    print(c, end=', ')
print('FIM')