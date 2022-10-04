import urllib.request

def main():
    def compra(url):
        preco = lerUrl("http://beans.itcarlow.ie/prices-loyalty.html")
        print(preco)

    def lerUrl(url):
        pagina = urllib.request.urlopen(url)
        texto = pagina.read().decode("utf8")
        return identificaValor(texto)

    def identificaValor(conteudo):
        inicio = conteudo.find(">$") + 2
        fim = conteudo.find('</', inicio)
        return conteudo[inicio:fim]

    compra("http://beans.itcarlow.ie/prices-loyalty.html")

if __name__ == '__main__':
    main()