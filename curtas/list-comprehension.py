# Lista de teste
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Modo comum de copiar uma lista
lista_nova = []
for numero in lista:
  lista_nova.append(numero)

# Copiando lista usando list comprehension
# Sintaxe: [valor for valor in list if condição] (Pode ser usado sem if)
lista_pares = [numero for numero in lista if numero % 2 == 0]
lista_impares = [numero for numero in lista if numero % 2 != 0]
lista_completa = [numero for numero in lista]

print(lista_nova) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista_pares) # [2, 4, 6, 8, 10]
print(lista_impares) # [1, 3, 5, 7, 9]
print(lista_completa) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]