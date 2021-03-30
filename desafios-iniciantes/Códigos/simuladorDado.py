

import random

repet = "s"
numeros = []

while True:
  try:
    dado = int(input('Insira o número de faces do dado: '))
    break
  except:
    print('Valor inválido!')

while (repet == "s"):
  while True:
    try:
      qtd = int(input('Número de dados: '))
      break
    except:
      print('Valor inválido!')
  soma_dado = 0

  for _ in range(qtd):
    num_gerado = random.randint(1, dado)
    numeros.append(str(num_gerado))
    soma_dado += num_gerado
  

  print('===============================================')
  print("Resultado: " + ', '.join(numeros))
  print(f'Soma dos números: {soma_dado}.')
  print('===============================================')
  repet = input('Deseja girar novamente? ("s" para continuar): ')

print('Programa encerrado!')