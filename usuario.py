# importando sqlite
import sqlite3

# criando conexao
banco = sqlite3.connect("usuario.db")

# inserir dados
def inserir_form(i):
    with banco:
        cur = banco.cursor()
        query = "INSERT INTO Usuario(nome, email) VALUES(?,?)"
        cur.execute(query,i)

# Atualizar dados
def atualizar_form(i):
    with banco:
        cur = banco.cursor()
        query = "UPDATE Usuario SET nome=?, email=?, WHERE id=? "
        cur.execute(query, i)

# Deletar dados
def deletar_form(i):
    with banco:
        cur = banco.cursor()
        query = "DELETE FROM Usuario WHERE id=?"
        cur.execute(query,i)

# Ver dados
def ver_form():
    ver_dados = []
    with banco:
        cur = banco.cursor()
        query = "SELECT * FROM Usuario"
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)
    return ver_dados        


# Ver dados
def ver_item(id):
    ver_dados_individual = []
    with banco:
        cur = banco.cursor()
        query = "SELECT * FROM Usuario WHERE id=?"
        cur.execute(query,id)

        rows = cur.fetchall()
        for row in rows:
            ver_dados_individual.append(row)


# VALIDADOR DE CPF
def quantidade():
    if len(verificacao_usuario) < 11 or len(verificacao_usuario) > 11:
        # print(f"O CPF é invalido pois nele há {len(verificacao_usuario)} caracteres")
        return False
    else:
        return True


if quantidade() == False:
    print("CPF é invalido!")
else:
    usuario = cursor
