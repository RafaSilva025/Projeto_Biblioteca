import sqlite3

# Função para exibir a tela de bem-vindo


def bem_vindo():
    print("*************************************")
    print("**********BEM VINDO À BIBLIOTECA!****")
    print("*************************************\n")

# Função para o cadastro de usuários


def cadastro():
    con = sqlite3.connect("usuarios.db")
    cursor = con.cursor()

    # Solicita as informações do usuário
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu CPF: ")
    telefone = input("Digite seu telefone: ")

    # Insere as informações do usuário na tabela "usuarios"
    cursor.execute(
        f"INSERT INTO usuarios (nome, cpf, telefone) VALUES ('{nome}', '{cpf}', '{telefone}')")

    # Salva as alterações
    con.commit()

    # Fecha a conexão com o banco de dados
    con.close()

# Função para verificar se o usuário já está cadastrado


def verificar_usuario():
    con = sqlite3.connect("usuarios.db")
    cursor = con.cursor()

    # Solicita o CPF do usuário
    cpf = input("Digite seu CPF: ")

    # Verifica se o CPF já está cadastrado na tabela "usuarios"
    cursor.execute(
        f"SELECT nome, cpf, telefone FROM usuarios WHERE cpf='{cpf}'")
    resultado = cursor.fetchall()

    # Se o usuário não estiver cadastrado, exibe a tela de cadastro
    if len(resultado) == 0:
        print("Usuário não encontrado. Realizando cadastro...\n")
        cadastro()
    else:
        print(f"Bem-vindo de volta, {resultado[0][0]}!\n")

    # Fecha a conexão com o banco de dados
    con.close()

# Função para exibir o catálogo de livros


def catalogo_livros():
    print("Catálogo de livros:\n")
    print("1. Comédia")
    print("2. Romance")
    print("3. Educação")
    print("4. Infantis\n")

# Função para realizar o empréstimo de livros


def emprestimo_livros():
    print("Realizar empréstimo:\n")
    print("Selecione o númer")
