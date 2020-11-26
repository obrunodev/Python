# Aula 03 - Renderizando páginas

Com certeza não queremos renderizar apenas pequenos textos, mas sim páginas completas que fizermos usando arquivos de HTML, CSS e JS.

Para fazer isso primeiramente precisamos importar do flask um recurso chamado render_template.

Para isto basta digitar no server.py:

```python
from flask import Flask, render_template
```

Agora basta retornarmos na nossa rota o index ao invés de uma simples string:

```python
@app.route('/')
def hello_world():
	return render_template('index.html')
```

Caso você tenha sido apressado e tentado acessar o servidor, percebeu que obteve um erro... O motivo disso é porque o render_template busca arquivos em uma pasta chamada template. Por isso basta criá-la e jogar os arquivos lá dentro.