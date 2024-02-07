
print("Abrindo um arquivo...")
try: # O código crítico que desejamos executar deve estar no escopo do try,
    open("exercicio01.txt")
    print("Arquivo aberto!")

except FileNotFoundError as erro: # Se acontecer esse erro execute essa parte do codigo
    print("O Arquivo não existe ou não foi encontrado!")
    
except FileExistsError as erro:   # Se acontecer esse erro execute essa parte do codigo
    print("O Arquivo ou diretório já existe!")