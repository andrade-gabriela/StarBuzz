# Gabriela -> github.com/andrade-gabriela
# 04/10/2022

from logging import lastResort
import urllib.request
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def main():
    #função principal analisa o valor dos produtos e solicita o envio de e-mail
    def compra(url):

        preco = float(lerUrl("http://beans.itcarlow.ie/prices-loyalty.html"))
        
        email = input('Digite seu e-mail para receber um aviso quando o preço for inferior a R$4,70\n')

        if preco < 4.7:
            enviaEmail(email, preco)

    #le uma url e identifica o valor do produto nela
    def lerUrl(url):
        pagina = urllib.request.urlopen(url)
        texto = pagina.read().decode("utf8")
        return identificaValor(texto)

    #procura dentro de um texto os caracteres que indicam valor e retorna somente o preço
    def identificaValor(conteudo):
        inicio = conteudo.find(">$") + 2
        fim = conteudo.find('</', inicio)
        return conteudo[inicio:fim]

    #envia um email pelo gmail
    def enviaEmail(email,preco):

        msg = MIMEMultipart()

        #mensagem a ser enviada
        message = f"O preço atual de compra é: {preco}"

        #parametros para enviar a mensagem
        password = "password"
        msg['Subject'] = "subject"
        msg['From'] = "email"
        msg['To'] = "{}".format(email)

        msg.attach(MIMEText(message, 'plain'))

        #criando servidor e enviando o e-mail
        server = smtplib.SMTP('smtp.gmail.com', 587)

        server.ehlo()

        server.starttls()

        server.login(msg['From'], password)

        server.sendmail(msg['From'], msg['To'], msg.as_string())

        server.quit()
 
        print("successfully sent email")


    compra("http://beans.itcarlow.ie/prices-loyalty.html")

if __name__ == '__main__':
    main()