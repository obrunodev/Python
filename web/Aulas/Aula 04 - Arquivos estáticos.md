# Aula 04 - Arquivos estáticos

Quando estamos falando de web, os arquivos estáticos são aqueles relacionados ao estilo e script, ou seja, CSS e JS.

Para utilizar na nossa aplicação flask, basta criar uma pasta nomeada como "static" na raiz do projeto (mesmo caminho do [server.py](http://server.py) e chamá-los no html passando o caminho "static/style.css".

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Meu site</title>
  <link rel="stylesheet" href="static/style.css">
</head>
<body>
  <h1>Minha aplicação flask</h1>
</body>
</html>
```

Salve e atualize o servidor para conferir o funcionamento.