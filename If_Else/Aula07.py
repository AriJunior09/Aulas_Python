import random
print('________________________   PEDRA, PAPEL E TESOURA    ______________________________')
lista = ['pedra', 'papel', 'tesoura']
pc_esc = random.choice(lista)
print('Vamos lá quero ver você ganhar de mim! escolha \033[31mPEDRA\033[m, \033[31mPAPEL \033[mou \033[31mTESOURA')
usuario = str(input('\033[36m>>>: '))
if pc_esc == 'pedra' and usuario == 'tesoura' or pc_esc == 'papel' and usuario == 'pedra' or pc_esc == 'tesoura' and usuario == 'papel':
    print('\033[31mVOCÊ PERDEU! \033[mEu escolhi \033[31m{}'.format(pc_esc))
elif pc_esc == 'pedra' and usuario == 'papel' or pc_esc == 'papel' and usuario == 'tesoura' or pc_esc == 'tesoura' and usuario == 'pedra':
    print('\033[36mVOCÊ GANHOU! \033[mEu havia escolhido \033[31m{}'.format(pc_esc))
elif pc_esc == 'pedra' and usuario == 'pedra' or pc_esc == 'papel' and usuario == 'papel' or pc_esc == 'tesoura' and usuario == 'tesoura':
    print('\033[34mEMPATE')