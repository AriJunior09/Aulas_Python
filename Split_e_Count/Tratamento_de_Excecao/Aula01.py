
print("Abrindo um arquivo...")
try: # O código crítico que desejamos executar deve estar no escopo do try,
    open("exercicio01.txt")
    print("Arquivo aberto!")

except FileNotFoundError as erro: # Exceção para arquivo não encontrado
    print("O Arquivo não existe ou não foi encontrado!")
    
except FileExistsError as erro:   # Exceção para quando o arquivo ja existe
    print("O Arquivo ou diretório já existe!")

except PermissionError as erro:   # Exceção para falta de permissão
    print("Não temos permissão para realizar uma operação")