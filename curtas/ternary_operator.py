# Condição if e else
def maioridade_if(idade):
  if idade >= 18:
    return 'Maior de idade'
  else:
    return 'Menor de idade'

# Sintaxe da ternary operator
# valor_se_verdadeiro if condição else valor_se_falso
# Exemplo acima usando ternary
def maioridade_ternary(idade):
  return 'Maior de idade' if idade >= 18 else 'Menor de idade'

print(maioridade_if(12))
print(maioridade_if(20))
print(maioridade_ternary(12))
print(maioridade_ternary(20))