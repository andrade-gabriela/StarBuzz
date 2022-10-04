import urllib.request

def lerUrl(url):
    pagina = urllib.request.urlopen(url)
    texto = pagina.read().decode("utf8")
    return identificaValor(texto)

def identificaValor(conteudo):
    inicio = conteudo.find(">$") + 2
    fim = conteudo.find('</', inicio)
    return conteudo[inicio:fim]

print(lerUrl("http://beans.itcarlow.ie/prices-loyalty.html"))
