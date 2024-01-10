# CORES NO TERMINAL
# ANSI - ESCOPE SEQUENCE
#\033[0;33;44m   # Para colorir texto e mudar o estilo sempre começa com \33[  e termina com m,
#____________ESTILOS:
# 0 - None (Nenhum estilo)
# 1 - Bold (Negrito)
# 4 - Underline (Sublinhado)
# 7 - Negative (Inverter as cores)

#_CORES DO TEXTO:    # CORES DO BACK
# 30 - Branco        # - 40
# 31 - Vermelho      # - 41
# 32 - Verde         # - 42
# 33 - Amarelo       # - 43
# 34 - Azul          # - 44
# 35 - Rosa          # - 45
# 36 - Celeste       # - 46
# 37 - Cinza         # - 47
print('\033[7;30mTeste de cores')
print('\033[1;41mTeste de cores')
print('\033[0;32mTeste de cores')
print('\033[0;33mTeste de cores')
print('\033[0;34mTeste de cores')
print('\033[0;35mTeste de cores')
print('\033[0;36mTeste de cores')
print('\033[0;37mTeste de cores')
a = 3
b = 5
print('\033[mOs valores são \033[32m{} \033[me \033[31m{}'.format(a, b))
nome = 'Ari'
print('{}Olá muito prazer, {}{}{}!'.format('\033[m', '\033[4;34m', nome, '\033[m'))