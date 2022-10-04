# Gabriela -> github.com/andrade-gabriela
# 04/10/2022

import urllib.request
import smtplib
from email.mime.text import MIMEText


def main():
    # 
    def compra(url):
        preco = lerUrl("http://beans.itcarlow.ie/prices-loyalty.html")
        print(preco)

    #
    def lerUrl(url):
        pagina = urllib.request.urlopen(url)
        texto = pagina.read().decode("utf8")
        return identificaValor(texto)

    def identificaValor(conteudo):
        inicio = conteudo.find(">$") + 2
        fim = conteudo.find('</', inicio)
        return conteudo[inicio:fim]

    def enviaEmail():
        remetente = '' #criar um email
        destino = [''] #email de quem vai receber

        port = 1025
        msg = MIMEText('Texto do e-mail')

        msg['Subject'] = 'Test e-mail'
        msg['From'] = ''#email criado p/ remetente
        msg['To'] = ''#email destino

        with smtplib.SMTP('localhost', port) as server:

            # server.login('username', 'password')
            server.sendmail(remetente, destino, msg.as_string())
            print("E-mail enviado com sucesso")


    compra("http://beans.itcarlow.ie/prices-loyalty.html")

if __name__ == '__main__':
    main()