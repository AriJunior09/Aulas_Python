# APRENDENDO A USAR O COUNT PARA CONTAR: LETRAS, PALAVRAS OU CARACTERES

frase01 = "amo amoras e o hipopotamo ama pamonhas com ramos de amoreira"

contagem1 = frase01.count("amo")  # Conta quantas vezes aparece a palacra "amo" na frase
# PROBLEMA É QUE DESSA FORMA, CONTA ATÉ DENTRO DAS PALAVRAS. 
print("Contagem: ", contagem1)    # A saída será 6 (mas está errado!)


# PARA CORRIGIR ISSO PRECISAMOS SEPARAR A FRASE EM UMA LISTA DE PALAVRAS E VERIFICAR UMA A UMA
separacao = frase01.split()        # Separando em lista de palavras
contagem2 = separacao.count("amo") # Contando todas as palavras "amo" na lista
print("Contagem: ", contagem2)     # Mostrando a contagem correta

