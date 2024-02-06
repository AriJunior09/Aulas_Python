from datetime import datetime

data_Hoje = datetime.now()
print("A data de hoje é: " , data_Hoje)

data_Hoje_Formatada = f"{data_Hoje:%d/%m/%Y}"
print("A data de hoje é: " ,data_Hoje_Formatada)
