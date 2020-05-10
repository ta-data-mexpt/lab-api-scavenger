import re
from github import Github
g=Github('4854303114327f3e7e5cb3334d629d19e1535cc5')
repo=g.get_repo('ironhack-datalabs/scavenger')
contenidos=repo.get_contents('')
lista_paths=[]
for contenido in contenidos[1:]:
    for contents in repo.get_contents(contenido.path):
        if contents.path.endswith('scavengerhunt'):
            lista_paths.append(contents)
paths_string=[]
for x in lista_paths:
    paths_string.append(x.path[6:])
ordered_paths=sorted(list(zip(paths_string,lista_paths)))
for x in ordered_paths:
    print(re.sub('b','',str(x[1].decoded_content)).replace('\\n',''),end='')