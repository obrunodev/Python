# Importando módulo de requisição
import requests

# Importando time
import time

# Importando BeautifulSoup
from bs4 import BeautifulSoup as bs

# Link que será consultado o preço
URL = 'https://www.amazon.com.br/dp/B08ZBY9ZBB/ref=s9_acsd_al_bw_c2_x_1_i?pf_rd_m=A3RN7G7QC5MWSZ&pf_rd_s=merchandised-search-5&pf_rd_r=GVD7KGKS1TWVAEXTGE5C&pf_rd_t=101&pf_rd_p=6252c826-8ce2-4f83-a9fa-ef75d9bd9c57&pf_rd_i=7791985011'

# Configurando o headers
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'}

def check_price():
  
  # Requisitando a página através da URL e instanciando em page
  page = requests.get(URL, headers=headers)

  # Coletando informações no HTML da página e armazenando em soup
  soup = bs(page.content, 'html.parser')

  # Selecionando o texto de um elemento no HTML pelo id
  title = soup.find(id="productTitle").get_text()

  # Selecionando o texto de um elemento HTML por id ou classe
  price = soup.find(id="priceblock_ourprice").get_text()

  # Pegando somente o valor antes da vírgula
  converted_price = float(price[2:-3])

  # Imprimindo resultados
  print('========================')
  print(title.strip())
  print(price)
  print('========================')

  # Se valor for menor que 300, gerar um arquivo para armazenar informação
  arquivo_preco = open('dados.txt', 'a')
  if converted_price <= 500:
    arquivo_preco.write(f'{title.strip()} \n')
    arquivo_preco.write(f'{price} \n=================\n')
    print('Valor salvo no arquivo de texto!')
  else:
    print("Preço acima do solicitado!")

  # Imprimindo conteúdo do soup
  # print(soup.prettify())

while True:
  try:
    check_price()
    time.sleep((60 * 60) * 2)
  except Exception:
    print('Ocorreu um erro. Tentando novamente!')
    time.sleep(60)
