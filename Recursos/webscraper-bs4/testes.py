from urllib.request import urlopen
import requests as rq

teste = rq.get('https://pokeapi.co/api/v2/pokemon/ditto')

print(teste)