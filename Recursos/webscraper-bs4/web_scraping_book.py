from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

url_teste = 'http://pythonscraping.com/pages/page1.html'

def coletar_titulo(url):
  try:
    html = urlopen(url)
  except HTTPError as e:
    return None
  
  try:
    bs = BeautifulSoup(html.read(), 'html.parser')
    title = bs.body.h1
  except AttributeError as e:
    return None
  
  return title

title = coletar_titulo(url_teste)
if title == None:
  print('Título não foi encontrado!')
else:
  print(title)