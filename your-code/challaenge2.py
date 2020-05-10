
import json
import requests
requestA = requests.get('http://api.github.com/repos/ironhack-datalabs/madrid-oct-2018/commits')
resultados = requestA.json()

contador = 0

for res in resultados:
    commit = res.get('commit')
    author = commit.get('author')
    print (author)
    date = author.get('date')
    #print (date)
    contador = contador+1
print (contador)
    