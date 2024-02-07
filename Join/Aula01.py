# USANDO O METODO JOIN PARA CONCATENAR UMA LISTA DE PALAVRAS EM UMA STRING

minha_lista = ["arroz", "Feijão", "Macarrão"]

texto01 = ", ".join(minha_lista)
with open("texto01.txt", "w") as arquivo:
    arquivo.write(texto01)

texto02 = "\n".join(minha_lista)
with open("texto02.txt", "w") as arquivo:
    arquivo.write(texto02)

