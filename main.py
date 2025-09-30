#Import da biblioteca ftplib
from ftplib import FTP_TLS
import os

#Conexão com o servidor
ftp=FTP_TLS('ftp.server.test@testserver.com')
print('Conexão realizada com sucesso.')
ftp.login(user='api@testserver.com',passwd='Api@2020')
print('Login efetuado com sucesso.')
ftp.prot_p() #Método relacionado a segurança TSL

#Buscando o arquivo .ZIP
dirPrincipal=r'/outbound/report/customer_instance_info/'
ftp.cwd(dirPrincipal) #Mudança de diretório
dir2=ftp.nlst()[0] #SQL_Customer_Instance_Info_XXXXXXXXXXXXXXXXXXXX_XXXXXXXXXXXXXXXX
ftp.cwd(dir2)
dirArquivo=ftp.nlst()[1] #SQL_Customer_Instance_Info_XXXXXXXXXXXXXXXX_XXXXXXXXXXXXXXXX.zip

#Donwload do arquivo
local=open(r"../ftp_report_extract\Reports\\"+dirArquivo,'wb')
print('Fazendo download do arquivo '+dirArquivo+'...')
ftp.retrbinary('RETR '+dirArquivo,local.write)
print('Download concluido com sucesso.')

'''
#Movendo o arquivo para a pasta backup.
ftp.rename(dirArquivo,r'/outbound/report/customer_instance_info/backup/'+dirArquivo)
ftp.cwd('/outbound/report/customer_instance_info/')

#Excluido o diretório
files = list(ftp.nlst(dir2))
for f in files:
    ftp.delete(f)

ftp.rmd(dir2)
'''

#Fechando conexão FTP.
ftp.quit()
local.close()

#Alterando o nome do arquivo local
nameArq=dirArquivo[:26]+'.zip'
os.rename(r'../fatp_report_extract\Reports\\'+dirArquivo,r'../ftp_report_extract\Reports\\'+nameArq)