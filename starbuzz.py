import urllib.request

pagina = urllib.request.urlopen("http://beans.itcarlow.ie/prices-loyalty.html")
texto = pagina.read().decode("utf8")
inicio = texto.find(">$") + 2
fim = texto.find('</', inicio)
preco = texto[inicio:fim]
print(preco)