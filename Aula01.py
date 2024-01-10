frase = 'Curso em Video Python'
print(frase[9:21])    #mostra a letra de número 9 até a letra 21
frase = 'Curso em Video Python'
print(frase[9:21:2])  #mostra a letra de número 9 até a letra 21 pulando de 2 em 2
frase = 'Curso em Video Python'
print(frase[:5])      #mostra da primeira letra até a quinta
frase = 'Curso em Video Python'
print(frase[15:])     #mostra da letra número 15 até o fim
frase = 'Curso em Video Python'
print(frase[9::3])    #mostra da letra num. 9 até a última saltando de 3 em 3
print(len(frase))     #conta quantas letras tem na frase
print(frase.count('o')) #conta quantas letras "o" tem na frase
print(frase.count('o', 0, 13)) #conta quantas letras "o" tem no intervalo de 0 a 13
print(frase.find('deo')) #Pesquisa "deo" dentro da frase e diz onde começa
print('Curso' in frase) #Pesquisa "Curso" na Frase e responde True ou False
print(frase.replace('Python', 'Android')) #Troca a palavra Python por Android
print(frase.upper()) #Coloca em Maiúscula
print(frase.lower()) #Coloca em Minúscula
frase2 = '   Aprenda Python  '
print(frase2) #Frase com espaços no começo
print(frase2.strip()) #Essa função remove os espaços do inicio e do fim
# rstrip (Remove os espaços da Direita)
# lstrip (Remove os espaços da Esquerda)
print(frase.split()) #Separa as palavras da frase em listas de palavras
print('-'.join(frase.split())) #Coloca o "-" entre as palavras
print('-'.join(frase)) #Separa as letras colocando '-'