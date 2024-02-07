# USANDO O RENAME PARA RENOMEAR ARQUIVOS

import os
nome_antigo = "nome_antigo.txt"
nome_novo = "nome_novo.txt"

try:
    os.rename(nome_antigo, nome_novo)
    print(f"O Arquivo {nome_antigo} foi renomeado para {nome_novo}")

except FileNotFoundError:
    print(f"O Arquivo {nome_antigo} não foi encontrado!")

except IsADirectoryError:
    print("Ocorre quando tentamos remover um diretório usando a função remove, em vez de rmdir.")

except Exception as e:
    print(f" Ocorreu um erro ao renomear o arquivo: {e}")