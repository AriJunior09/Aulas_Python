print('______________________    MUDANDO DE BASE    _________________________\n')
numero = int(input('Digite um número: '))
escolha = int(input('Escolha uma opção de conversão:\n1 - Binário\n2 - Octal\n3 - Hexadecimal\n>>>: '))
if escolha == 1:
    print('O valor em binário para \033[31m{} \033[mé \033[36m{}'.format(numero, (bin(numero)[2:])))
elif escolha == 2:
    print('O valor em Octal para \033[31m{} \033[mé \033[36m{}'.format(numero, (oct(numero)[2:])))
elif escolha == 3:
    print('O valor em Hexadecimal para \033[31m{} \033[mé \033[36m{}'.format(numero, (hex(numero)[2:]).upper()))

