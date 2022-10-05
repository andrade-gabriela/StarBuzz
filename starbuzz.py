# Gabriela -> github.com/andrade-gabriela
# 04/10/2022

import urllib.request
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def main():
    # 
    def compra(url):

        preco = float(lerUrl("http://beans.itcarlow.ie/prices-loyalty.html"))
        
        email = input('Digite seu e-mail para receber um aviso quando o preço for inferior a R$4,70\n')

        if preco < 4.7:
            enviaEmail(email)

    #
    def lerUrl(url):
        pagina = urllib.request.urlopen(url)
        texto = pagina.read().decode("utf8")
        return identificaValor(texto)

    def identificaValor(conteudo):
        inicio = conteudo.find(">$") + 2
        fim = conteudo.find('</', inicio)
        return conteudo[inicio:fim]

    def enviaEmail(email):

        msg = MIMEMultipart()

        message = "oi"

        #parametros para enviar a mensagem
        password = "3nv143m41l851"
        msg['Subject'] = "Test e-mail"
        msg['From'] = "enviaemailbsi@gmail.com"
        msg['To'] = "{}".format(email)

        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com: 587')

        server.starttls()

        server.login(msg['From'], password)

        server.sendmail(msg['From'], msg['To'], msg.as_string())

        server.quit()
 
        print("successfully sent email")



        # remetente = 'enviaemailbsi@gmail.com'
        # destino = ['{}'.format(email)]

        # port = 1025
        # msg = MIMEText('Texto do e-mail')

        # msg['Subject'] = 'Test e-mail'
        # msg['From'] = 'enviaemailbsi@gmail.com'
        # msg['To'] = '{}'.format(email)

        # with smtplib.SMTP('localhost', port) as server:

        #     # server.login('username', 'password')
        #     server.sendmail(remetente, destino, msg.as_string())
        #     print("E-mail enviado com sucesso")


    compra("http://beans.itcarlow.ie/prices-loyalty.html")

if __name__ == '__main__':
    main()