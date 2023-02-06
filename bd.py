# importando sqlite
import sqlite3

# criando conexao
banco = sqlite3.connect("usuario.db")

# criando tabela
cursor = banco.cursor()

cursor.execute("CREATE TABLE Usuario (id INTEGER PRIMARY KEY AUTOINCREMENT, nome text, email text)")

cur.execute("INSERT INTO Usuario VALUES('Aline', 'maria@gmail.com')")

banco.commit()
