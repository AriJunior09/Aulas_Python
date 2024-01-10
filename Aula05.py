print('________________________________    ANALISANDO O TIPO DE TRIÂNGULO    _______________________')
r1 = int(input('Digite o valor da Reta A: '))
r2 = int(input('Digite o valor da Reta B: '))
r3 = int(input('Digite o valor da Reta C: '))
if ((r1 + r2) > r3) and ((r2 + r3) > r1) and ((r3 + r1) > r2):
    print('Essas 3 retas podem formar um Triângulo!')
    if r1 == r2 and r1 == r3 and r2 == r3:
        print('O Triângulo é Equilátero!')
    elif (r1 == r2 and r2 != r3) or (r2 == r3 and r2 != r1):
        print('O Triângulo é Isósceles!')
    else:
        print('O Triângulo é Escaleno!')
else:
    print('Não forma um triângulo!')