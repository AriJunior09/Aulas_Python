# APRENDENDO A USAR O COUNT E O SPLIT JUNTOS:

frase01 = "amo amoras e o hipopotamo gosta de ramos de amoreira"

contagem1 = frase01.count("amo")  # Conta quantas vezes aparece a palavra "amo" na frase.
# O PROBLEMA É QUE DESSA FORMA, CONTA ATÉ DENTRO DAS PALAVRAS, POR EX. AMOras.
print("Contagem errada: ", contagem1)    # A saída será 5 (mas está errado!)
# AMO AMOras e o hipopotAMO gosta de rAMOs de AMOreira

# PARA CORRIGIR ISSO PRECISAMOS SEPARAR A FRASE EM UMA LISTA DE PALAVRAS E VERIFICAR UMA A UMA
separacao = frase01.split()        # Separando em lista de palavras
contagem2 = separacao.count("amo") # Contando todas as palavras "amo" na lista
print("Contagem correta: ", contagem2)     # Mostrando a contagem correta

