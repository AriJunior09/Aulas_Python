print('______________________________    2 NOTAS DE ALUNO PARA ANALISAR    _________________________________\n')
nota1 = float(input('Entre com a primeira nota: '))
nota2 = float(input('Entre com a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('Sua média foi de {} e você ficou \033[31mREPROVADO!'.format(media))
elif media < 7:
    print('Sua média foi de {} e você ficou em \033[33mRECUPERAÇÃO!'.format(media))
else:
    print('Sua média foi de {} e você foi \033[36mAPROVADO!'.format(media))