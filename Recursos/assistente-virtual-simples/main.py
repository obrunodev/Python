from neuralintents import GenericAssistant
from datetime import datetime
import sys

exercicios = ['Supino reto, 3 séries de 10', 'Cross over, 4 sérise de 8', 'Agachamento, 3 séries de 15']

def mostrar_exercicios():
    print('Lista de exercícios de hoje')
    for numero, exercicio in enumerate(exercicios):
        print(f'{numero + 1} - {exercicio}')

def adicionar_exercicio():
    exercicio = input('Que exercício você deseja adicionar: ')
    exercicios.append(exercicio)

def remover_exercicio():
    idx = int(input('Qual exercicio deseja remover: ')) - 1
    if idx <= len(exercicios):
        print(f'Removendo exercicio {exercicios[idx]}')
        exercicios.pop(idx)
    else:
        print('Não existe um exercício com essa numeração')

def tchau():
    print('Até mais')
    sys.exit(0)

def mostrar_data():
    print(f'Data de hoje: {datetime.today().strftime("%d/%m/%y")}')

def mostrar_hora():
    print(f'Agora são {datetime.now().strftime("%H:%M")}hr')

mappings = {
        'mostrar_exercicios': mostrar_exercicios,
        'adicionar_exercicio': adicionar_exercicio,
        'remover_exercicio': remover_exercicio,
        'despedida': tchau,
        'data': mostrar_data,
        'hora': mostrar_hora
        }

assistente = GenericAssistant("intents.json", mappings)

assistente.train_model()
assistente.save_model()

while True:
    
    message = input('Message: ')
    assistente.request(message)

