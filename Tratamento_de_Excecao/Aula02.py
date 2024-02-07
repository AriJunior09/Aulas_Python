import os
arquivo_a_remover = "arquivoParaRemover.txt"
try:
    os.remove(arquivo_a_remover)
    print(f"O Arquivo {arquivo_a_remover} foi removido com sucesso!")

except FileNotFoundError:
    print(f"O Arquivo {arquivo_a_remover} não foi encontrado!")
except Exception as e:
    print(f" Ocorreu um erro ao remover o arquivo: {e}")