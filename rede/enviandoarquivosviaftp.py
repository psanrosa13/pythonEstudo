from ftplib import *

ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())

usuario = input('Digite seu usuario: ')
senha = input('Digite sua senha: ')

ftp.login(usuario,senha)

print('Diretório atual de trabalho : ',ftp.pwd() )

ftp.cwd('pub')

print('Diretório corrente : ',ftp.pwd() )

ftp.retrlines('LIST')

ftp.quit()