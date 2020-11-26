# Aula 02 - Rotas

Na rota que criamos na aula passada, passamos como parâmetro o caminho '/', isso significa que aquela é a rota principal.

```python
@app.route('/')
```

Para criar outra rota, basta adicionar esta mesma linha com um valor depois da barra '/':

```python
@app.route('/blog')
def blog():
	return 'Hello, this is my blog'
```

Ao acessar essa rota terá a mensagem dada como retorno em tela.

Na próxima aula vamos aprender renderizar telas que criamos com html, css e js.