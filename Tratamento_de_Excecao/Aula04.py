import os

try:
    entradas = os.scandir("If_Else")

    for obj in entradas:
        print(obj)
        print("Nome: ", obj.name)
        print("Caminho: ", obj.path)
        print("É Diretorio: ", obj.is_dir())
        print("É Arquivo: ", obj.is_file())
        if obj.is_file:
            print("Tamanho: ", obj.stat().st_size, "B")
        print("+++++++++++++++++++++++++++++++")
except FileNotFoundError:
    print("O Caminho não existe!")
except NotADirectoryError:
    print("O Caminho não é um diretório!")
