import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=input('Senha BD: ')
)

cursor = mydb.cursor()



def enviar_dados(bd, username, password):
  cursor.execute(f'Use {bd};')

  cursor.execute(f'INSERT INTO {bd} values({username}, {password};')

  return cursor

def exibir_dados(bd, table):
  cursor.execute(f'USE {bd}')

  cursor.execute(f'SELECT * FROM {table};')

  return cursor

for i in exibir_dados('fallbot', 'users'):
  print(i)