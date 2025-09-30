import os

diretorio=r'C:\Users\Gustavo\Projects\ftp_report_extract'

print(os.listdir(diretorio))

os.chdir(os.listdir(diretorio)[2]) #Mudando para pasta Reports
print(os.listdir()) #listando o diretório
var=str(os.listdir()[1])  #Guardando nome da pasta numa variável
print(var) #Printando a variável

