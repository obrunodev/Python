# Aula 03 - números

Aqui iremos aprender um pouco sobre os tipos de números que Python trabalha. e iremos começar a utilizar também variáveis.

## Tipos numéricos

Python trabalha com vários tipos numéricos, mas os dois mais utilizados serão os int (inteiros) e float (pontos flutuantes, também conhecidos como números com casas decimais).

### Inteiros

São números com valor inteiro, sem vírgula, podendo ser eles positivos ou negativos.

Por exemplo: 5, 7, -3.

### Pontos flutuantes

Números de ponto flutuantes são números com casas decimais, ou seja, que contenham valor após a vírgula, eles são identificáveis no python através do ponto decimal, por exemplo, 5.7, 4.9 e por aí vai.

É possível que você encontre números assim: 2.0

Nesse caso é considerado um número de ponto flutuante, já que o ponto decimal está presente nele.

## Aritmética básica

Python suporta trabalhar com operações aritméticas de forma muito simples, para isso, basta entendermos qual caracter usar para obtermos o resultado desejado.

Dica: Você pode testar essas operações abrindo seu prompt de comando e digitando python, ao pressionar enter, ele entrará no modo do interpretador, dessa forma, basta digitar as operações que automaticamente será retornado o resultado.

```python
# Soma
4 + 7 # Retorna 11

# Subtração
8 - 3 # Retorna 5

# Multiplicação
4 * 3 # Retorna 12

# Divisão (Esses sempre retornam um valor float)
12 / 4 # Retorna 3.0 (Como eu disse, sempre retorna float)

# Elevação
4 ** 2 # Retorna 16

# Raiz quadrada
16 ** 0.5 # Retorna 4.0

# Módulo, retorna não o resultado, mas o resto da divisão
10 % 3 # Retorna 1

# As regras da aritmética são normalmente respeitadas em Python
12 + 5 * 3 # = 12 + 15 = 27

# Para somar primeiro, deve-se usar parênteses
(12 + 5) * 3 # = 17 * 3 = 51
```

## Variáveis

São pequenos espaços na memória que podemos nomear e armazenar informações para reutilizarmos no decorres do nosso código.

Variáveis são recursos extremamente importantes e impossíveis de criar projetos sem elas, são elas também que podem facilitar o entendimento do código, portanto, use sempre que possível.

Para criar uma variável, devemos respeitar algumas regras:

- Não começar o nome da variável com número. (Ex.: 1var)
- Não pode haver espaço no nome. (Ao invés de espaçar, é possível usar underscore "_")
- Não é possível utilizar caracteres especiais como %<>$&-+ e afins.
- É uma boa prática utilizar sempre letras minúsculas.

Sabendo disso, vamos criar e trabalhar com variáveis.

```python
# Para atribuir uma variável em Python, basta digitar seu nome, seguido do sinal de 
# igual(=) e o valor que deseja atribuir.
numero1 = 5

# É possível realizar operações aritméticas com essas variáveis.
numero1 * numero1 # Retorna 25

# Você pode também redefinir as variáveis da mesma forma que criou
numero1 = 10
numero1 # Agora retorna 10

# Vamos criar uma variável que armazene o resultado de uma operação aritmética entre duas
# variáveis
resultado = numero1 + numero1
resultado # Retorna 20
```

É importante sermos claros ao criar uma variável, usando palavras que podem ser facilmente identificáveis caso outra pessoa pegue nosso código para ler.

Exemplo:

```python
# Calcular o diâmetro do círculo através do raio
raio = 5
diametro  = raio * 2

# Mostrar diametro
diametro # Retorna 10
```

Hoje aprendemos a utilizar números, operações aritméticas e como criar nossas primeiras variáveis para armazenar esses números.

Agora vamos fazer alguns exercícios!

## Exercícios:

Crie um arquivo chamado "ex01.py" para resolver os exercícios.

Dica: Use o símbolo # para criar um comentários e identificar melhor seu código.

1. Crie um código que mostre em tela o resultado de 5 elevado a 4ª potência. Res.: 625
2. Crie um código que mostre o resultado da seguinte divisão: 18 / 4. Res.: 4.5

### Bônus

Crie um código com as variáveis valorHora e horasTrabalhadas.

Se código deve retornar o salário final.

---

## [Aula anterior](https://github.com/obrunodev/aprenda-python/blob/main/Iniciantes/primeiroCodigo.md)
## [Próxima aula (Em breve)]()