   # APRENDENDO A USAR O SPLIT PARA SEPARAR AS PALAVRAS TRANSFORMANDO EM LISTAS

frase01 = "Eu gosto de programar"
frase02 = "Abacaxi com ameixa para fazer vitamina"
frase03 = "Precisa comprar: Abacaxi, Ameixa e Leite"
frase04 = "Camisa-Calça-Moleton-Tênis-Sapatilha"

lista01 = frase01.split()    # Separando as palavras pelo espaço (padrão)
lista02 = frase02.split("a") # Separando pela letra "a" no caso remove apenas em minúsculo
lista03 = frase03.split(",") # Separando pela visgula
lista04 = frase04.split("-") # Separando pelo "-"

print(lista01)
print(lista02)
print(lista03)
print(lista04)