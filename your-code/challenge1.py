'''
import requests


requestA = requests.get('http://api.github.com/repos/ironhack-datalabs/madrid-oct-2018/forks')
resultados = requestA.json()
#print(resultados)

idiomas=[]

for res in resultados:
    print ( res.get('languages_url'))
'''

import json
import requests
requestA = requests.get('http://api.github.com/repos/ironhack-datalabs/madrid-oct-2018/forks')
resultados = requestA.json()
#print(resultados)
idiomas=[]
# python sale como valor None
for res in resultados:
    lenguaje=res.get('language')
    #print(lenguaje)
    if lenguaje not in idiomas:
        idiomas.append(lenguaje)
print(idiomas)


idiomas2=requests.get('http://api.github.com/repos/ironhack-datalabs/madrid-oct-2018/languages')
resultados2=idiomas2.json()
#print(resultados2.keys())
idiomas3=[]
for i in resultados2:
    idiomas3.append(i)
print(idiomas3)