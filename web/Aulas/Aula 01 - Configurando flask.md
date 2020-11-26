# Aula 01 - Configurando flask

### Windows

1. Crie uma pasta para o projeto.
2. Acesse o diretório criado pelo terminal.
3. Inicie um ambiente virtual com o comando "python -m venv venv".
4. Ative o ambiente com o comando "source venv/Scripts/activate"
5. Instale o flask "pip install flask"
6. Crie um arquivo chamado "server.py" com o seguinte código:

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello world!'
```

### Configurações e rodando o server:

1. Configure o [server.py](http://server.py) como arquivo principal do flask "export FLASK_APP=server.py".
2. Ative o debug mode "export FLASK_ENV=development". Dessa forma o app irá atualizar sem precisar derrubar o server e abrir novamente para atualizar.
3. Rode o servidor com "flask run".
4. Agora basta acessar o endereço passado e já terá o 'Hello world!' em tela.