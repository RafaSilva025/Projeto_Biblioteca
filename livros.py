from validate_docbr import CPF
import sqlite3
import datetime as dt
import datetime
import time


def bem_vindo():
    print("*********************************")
    print("***********BEM VINDO!************")
    print("*********************************\n")
    print("-----------Biblioteca------------\n")
    cadastro()

# Função para o cadastro de usuários

def cadastro():
    con = sqlite3.connect('user.db')
    cursor = con.cursor()
    # cursor.execute("CREATE TABLE user (nome text, cpf text, telefone text)")

# VERIFICAÇÂO DE USUARIO
    print("Informe seu CPF cadastrado, para acessar a biblioteca, caso nao tenha ou digite um CPF irregular, irá automaticamente pra tela de cadastro!")
    verificacao_usuario = str(input("-")).replace('.', '').replace('-', '')

    cpf_list = [row[0] for row in cursor.execute('SELECT cpf FROM user')]
    if verificacao_usuario not in cpf_list:
        print("CPF não encontrado.")
        dados()
    else:
        print(f"\nSeja Bem-Vindo")
        print("Perfeito, usuario cadastrado, vamos prossegir...\n")
        opcoes()


def dados():
    try:
        con = sqlite3.connect('user.db')
        cursor = con.cursor()
        print("\n------CADASTRO------")
        nome = str(input("Digite seu nome:")).title()
        cpf = str(input("Digite seu CPF:")).replace('.', "").replace('-', "")
        if not CPF().validate(cpf):
            print("CPF inválido, tente novamente...")
            return    
        telefone = str(input("Digite seu Telefone/Celular:"))
        cursor.execute(f"""INSERT INTO user (nome, cpf, telefone) 
        VALUES ('{nome}' , '{cpf}', '{telefone}')""")
    # Salva as alterações
        con.commit()
    # Fecha a conexão com o banco de dados
        con.close()
        time.sleep(2)
        print("Cadastro Efetuado com Sucesso")
        
    except sqlite3.Error as erro:
        print("Erro ao cadastrar: ",erro)

# CATALAGOS DOS LIVROS


def catalogo_livro():
    global comedia
    comedia = ['Livro 01-A Extraordinária Viagem do Faquir Que Ficou Preso Em um Armário Ikea',
               'Livro 02-A Troca, Ed Mort  Todas as Histórias', 'Livro 03-Cadê Você Bernadette?', 'Livro 04-O Diabo Veste Prada', 'Livro 05-Te Vendo Um Cachorro', 'Livro 06-Vermelho, Branco e Sangue Azul']

    global romance
    romance = ['Livro 01-10 DATES SURPRESA', 'Livro 02-13 SEGUNDOS', 'Livro 03-4 HOMENS EM 44 CAPÍTULOS', 'Livro 04-A ALTURA DESLUMBRANTE', 'Livro 05-A BARRACA DO BEIJO', 'Livro 06-A BUSCA', 'Livro 07-A CANÇÃO DA ÓRFÃ', 'Livro 08-A CANÇÃO DAS ÁGUAS', 'Livro 09-A CIDADE DE VAPOR', 'Livro 10-A CINCO PASSOS DE VOCÊ',
               'Livro 11-A CORRIDA DE ESCORPIÃO', 'Livro 12-A DAMA DA MATA LINDÍSSIMO ROMANCE SÁFICO DE FANTASIA', 'Livro 13-A INSUSTENTÁVEL LEVEZA DO SER', 'Livro 14-A LISTA DA SORTE', 'Livro 15-A MALDIÇÃO DO MAR UMA HISTÓRIA SOBRE AMOR E VINGANÇA SURPREENDENTE', 'Livro 16-A PRINCESA PROMETIDA', 'Livro 17-A PROBABILIDADE ESTATÍSTICA DO AMOR À PRIMEIRA VISTA', 'Livro 18-A PROMETIDA SEM CORAÇÃO', 'Livro 19-SER FELIZ É ASSIM', 'Livro 20-SEX EDUCATION: PÉ NA ESTRADA', 'Livro 21-SHINE – UMA CHANCE DE BRILHAR', 'Livro 22-SIMPLESMENTE ACONTECE', 'Livro 23-SOBRE AMOR E ESTRELAS E A CABEÇA NAS NUVENS', 'Livro 24-TRÊS HISTÓRIA ROMÂNTICAS COM OS SIGNOS COMO DESTAQUE', 'Livro 25-SOL DA MEIA-NOITE', 'Livro 26-SOMBRA E OSSOS', 'Livro 27-SONATA EM PUNK ROCK']

    global educacao
    educacao = ['Livro 01-A HISTÓRIA DA ASTROLOGIA PARA QUEM TEM PRESSA', 'Livro 02-A HISTÓRIA DO FUTEBOL PARA QUEM TEM PRESSA',
                'Livro 03-A HISTÓRIA DO UNIVERSO PARA QUEM TEM PRESSA', 'Livro 04-APARELHO SEXUAL E CIA', 'Livro 05-O QUE TEM DE MAIS LINDO DO QUE ISSO?', 'Livro 06-SEX EDUCATION: UMA GUIA PARA A VIDA']

    global infantis
    infantis = ['Livro 01-ABCDELAS', 'Livro 02-AMIGA URSA', 'Livro 03-CORALINE', 'Livro 04-DESVENTURAS DE UM GAROTO NADA COMUM', 'Livro 05-DR. ALEX', 'Livro 06-EU FICO EM SILÊNCIO', 'Livro 07-HISTÓRIAS DE TERROR PARA CRIANÇAS ESTRANHAS',
                'Livro 08-JACK E O PORQUINHO DE NATAL', 'Livro 09-MORTINA', 'Livro 10-MORTINA E O PRIMO INSUPORTÁVEL', 'Livro 11-REINAÇÕES DE NARIZINHO', 'Livro 12-TURMA DA MÔNICA: LAÇOS(HQ)']

    global aventura
    aventura = ['Livro 01-A FILHA DAS PROFUNDEZAS', 'Livro 02-A OUTRA VIDA MAIS DO MESMO, MAS MESMO ASSIM É BOM', 'Livro 03-A VOLTA AO MUNDO EM 80 DIAS', 'Livro 04-ARTEMIS FOWL', 'Livro 05-ENOLA HOLMES', 'Livro 06-JOGADOR NÚMERO DOIS', 'Livro 07-JOGADOR NÚMERO UM', 'Livro 08-MULHERES ESMERALDAS', 'Livro 09-O CASO DA MANSÃO DEBOËN', 'Livro 10-O FOGO ENTRE A NÉVOA', 'Livro 11-O GUIA DA DONZELA PARA ANÁGUAS E PIRATARIA', 'Livro 12-O GUIA DO CAVALHEIRO PARA O VÍCIO E A VIRTUDE', 'Livro 13-O REINO DE ZÁLIA', 'Livro 14-PERCY JACKSON E O LADRÃO DE RAIOS', 'Livro 15-ROBINSON CRUSOÉ'
                'Livro 16-SEX EDUCATION: PÉ NA ESTRADA', 'Livro 17-UMA JORNADA SEM FIM, A GRANDE SURPRESA DESTE ANO', 'Livro 18-VINGANÇA']

    global terror
    terror = ['Livro 01-13 DIAS DE MEIA-NOITE', 'Livro 02-A ALCATÉIA', 'Livro 03-A ASSOMBRAÇÃO DA CASA DA COLINA', 'Livro 04-A BALADA DO BLACK TOM, MAIS 13 FATOS SOBRE LOVECRAFT', 'Livro 05-A CIDADE DOS FANTASMAS', 'Livro 06-A HORA DO LOBISOMEM – TERROR CLÁSSICO JUVENIL', 'Livro 07-A INCENDIÁRIA', 'Livro 08-A MALDIÇÃO DO MAR – UMA HISTÓRIA SOBRE AMOR E VINGANÇA SURPREENDENTE', 'Livro 09-A METADE SOMBRIA', 'Livro 10-A NOITE DOS MORTOS-VIVOS, MAIS 5 CURIOSIDADES E 5 DETALHES DA EDIÇÃO',
              'Livro 11-A RAINHA DOS CONDENADOS', 'Livro 12-AMIGO IMAGINÁRIO', 'Livro 13-ANNA VESTIDA DE SANGUE, Livro 14-TRANSFORMA O TERROR EM UMA AVENTURA ALUCINANTE COM UM ROMANCE FOFO', 'Livro 15-AS GÊMEAS DO GELO – UM SUSPENSE COM TOQUES DE TERROR IMPRESSIONANTE', 'Livro 16-ASYLUM E SCARLETS', 'Livro 17-CARMILLA – UMA DAS MELHORES HISTÓRIAS DE VAMPIROS', 'Livro 18-CARRIE, Livro 19-BULLYING E FANATISMO RELIGIOSO NO PRIMEIRO TERROR DE STEPHEN KING', 'Livro 20-CARROSSEL SOMBRIO']

    global suspense
    suspense = ['Livro 01-13 SEGUNDOS', 'Livro 02-A BIBLIOTECA DA MEIA-NOITE', 'Livro 03-A CACHORRA', 'Livro 04-A CASA HOLANDESA', 'Livro 05-A CINCO PASSOS DE VOCÊ', 'Livro 06-A CORRIDA DE ESCORPIÃO', 'Livro 07-A CRIANÇA NO TEMPO', 'Livro 08-A DANÇA DA ÁGUA', 'Livro 09-A ESCRAVA ISAURA',
                'Livro 10-O LABIRINTO DO FAUNO + 9 CURIOSIDADES', 'Livro 11-O LIVRO DE MEMÓRIAS', 'Livro 12-O MARIDO PERFEITO', 'Livro 13-O MENINO QUE SOBREVIVEU', 'Livro 14-O PODEROSO CHEFÃO', 'Livro 15-O PRIMEIRO E O ÚLTIMO VERÃO', 'Livro 16-O PRÍNCIPE DA NÉVOA', 'Livro 17-O QUE ALICE ESQUECEU']

    global ficcao
    ficcao = ['Livro 01-A CURVA DO SONHO', 'Livro 02-A DIABÓLICA', 'Livro 03-A ESTRELA MAIS ESCURA', 'Livro 04-A MÃO ESQUERDA DA ESCURIDÃO', 'Livro 05-A MÁQUINA DO TEMPO', 'Livro 06-A MENINA QUE TINHA DONS', 'Livro 07-A PERGUNTA E A RESPOSTA', 'Livro 08-A QUINTA ESTAÇÃO E O PORTÃO DO OBELISCO', 'Livro 09-A SEGUNDA AURORA', 'Livro 10-ATRAVÉS DO VAZIO', 'Livro 11-AURORA ARDE, CONTINUAÇÃO DAS AVENTURAS DE UM ESQUADRÃO DE HERÓIS', 'Livro 12-AURORA ASCENDE', 'Livro 13-BABEL-17 E ESTRELA IMPERIAL',
              'Livro 14-BINTI(TRILOGIA COMPLETA)', 'Livro 15-CIDADE DA MEIA-NOITE', 'Livro 16-CIDADE NAS NUVENS', 'Livro 17-CINDER', 'Livro 18-DESAFIANDO AS ESTRELAS', 'Livro 19-DESPERTAR', 'Livro 20-DEVORADORES DE ESTRELAS', 'Livro 21-DORMIR EM UM MAR DE ESTRELAS', 'Livro 22-DUNA(LIVRO+HQ)', 'Livro 23-É ASSIM QUE SE PERDE A GUERRA DO TEMPO', 'Livro 24-ESPERE AGORA PELO ANO PASSADO', 'Livro 25-FLORES PARA ALGERNON', 'Livro 26-FLORES PARA ALGERNON, MAIS CINCO MOTIVOS PARA LER', 'Livro 27-FORWARD']

# OPÇÔES DA INTERFACE


def opcoes():
    opcao = int(input('SELECIONE OQUE VOCÊ IRÁ FAZER! \n 1- Empréstimo Livro(s) \n 2- Devolução Livro(s)\n 3- Cadastrar Novo Usuario \n 4- Sair \n 5- Avaliar Biblioteca \n\n'))
    if (opcao == 1):
        genero = int(input("\nMuito bem, selecione o Genero do(s) Livro(s): \n 1- Humor\n 2- Romance\n 3- Educação\n 4- Livros infantis/gibis\n 5- Aventura \n 6- Terror\n 7- Suspense/Drama\n 8- Ficção-Científica\n"))
        if (genero == 1):
            print("#"*40)
            print("\n".join(comedia))
            print("\nCaso for retirar mais de um livro, comece a seleção deles em 'ORDEM DECRESCENTE'")
            emprestimo_comedia = int(input("Temos essas opções para emprestimo, digite o numero do Livro que voce quer retirar: #só numero, exemplo - (02)\n"))
            # Removendo o livro da Lista
            while emprestimo_comedia in range(1, 28):
                comedia.pop(emprestimo_comedia-1)
                print("\n".join(comedia))
                print("\nLivro retirado com sucesso!")
                time.sleep(3)
                print("\n".join(comedia))
                continua = input("\nVoce deseja retirar mais algum livro?[S/N]\n").lower()
                if continua == "s":
                    emprestimo_comedia = int(input("\n Temos essas opções para emprestimo, digite o numero do Livro que voce quer retirar: #só numero, exemplo - (02)\n"))
                else:
                    print("\nObrigado, e volte sempre!")
                    data_emprestimo()
                    break
            else:
                print(
                    "O numero digitado nao consta na lista, Por favor digite Novamente outro número!")

        elif (genero == 2):
            print("#"*40)
            catalogo_livro()
            print("\n".join(romance))
            emprestimo_romance = int(input("\n Temos essas opções para emprestimo, digite o numero do Livro que voce quer retirar: #só numero, exemplo - (02)\n"))
            # Removendo o livro da Lista
            while emprestimo_romance in range(1, 28):
                romance.pop(emprestimo_romance-1)
                print("\n".join(romance))
                print("\nLivro retirado com sucesso!")
                time.sleep(3)
                continua = input("\nVoce deseja retirar mais algum livro?[S/N]\n").lower()
                if continua == "s":
                    emprestimo_romance = int(input("\n Temos essas opções para emprestimo, digite o numero do Livro que voce quer retirar: #só numero, exemplo - (02)\n"))
                else:
                    print("Obrigado, e volte sempre!")
                    data_emprestimo()
                    break
            else:
                print("O numero digitado nao contem na lista, Por favor digite Novamente outro número!")

        elif (genero == 3):
            print("#"*40)
            print("\n".join(educacao))
            emprestimo_educacao = int(input("\n Temos essas opções para emprestimo, digite o numero do Livro que voce quer retirar: #só numero, exemplo - (02)\n"))
            # Removendo o livro da Lista
            while emprestimo_educacao in range(1, 28):
                educacao.pop(emprestimo_educacao-1)
                print("\n".join(educacao))
                print("\nLivro retirado com sucesso!")
                time.sleep(3)
                continua = input("\nVoce deseja retirar mais algum livro?[S/N]\n").lower()
                if continua == "s":
                    emprestimo_educacao = int(input("\n Temos essas opções para emprestimo, digite o numero do Livro que voce quer retirar: #só numero, exemplo - (02)\n"))
                else:
                    print("Obrigado, e volte sempre!")
                    data_emprestimo()
                    break
            else:
                print("O numero digitado nao contem na lista, Por favor digite Novamente outro número!")

        elif (genero == 4):
            print("#"*40)
            print("\n".join(infantis))
            emprestimo_infantil = int(input("\n Temos essas opções para emprestimo, digite o numero do Livro que voce quer retirar: #só numero, exemplo - (02)\n"))
            # Removendo o livro da Lista
            while emprestimo_infantil in range(1, 28):
                infantis.pop(emprestimo_infantil-1)
                print("\n".join(infantis))
                print("\nLivro retirado com sucesso!")
                time.sleep(3)
                continua = input("\nVoce deseja retirar mais algum livro?[S/N]\n").lower()
                if continua == "s":
                    emprestimo_infantil = int(input("\n Temos essas opções para emprestimo, digite o numero do Livro que voce quer retirar: #só numero, exemplo - (02)\n"))
                else:
                    print("Obrigado, e volte sempre!")
                    data_emprestimo()
                    break
            else:
                print("O numero digitado nao contem na lista, Por favor digite Novamente outro número!")

        elif (genero == 5):
            print("#"*40)
            print("\n".join(aventura))
            emprestimo_aventura = int(input("\n Temos essas opções para emprestimo, digite o numero do Livro que voce quer retirar: #só numero, exemplo - (02)\n"))
            # Removendo o livro da Lista
            while emprestimo_aventura in range(1, 28):
                aventura.pop(emprestimo_aventura-1)
                print("\n".join(aventura))
                print("\nLivro retirado com sucesso!")
                time.sleep(3)
                continua = input(
                    "\nVoce deseja retirar mais algum livro?[S/N]\n").lower()
                if continua == "s":
                    emprestimo_aventura = int(input("\n Temos essas opções para emprestimo, digite o numero do Livro que voce quer retirar: #só numero, exemplo - (02)\n"))
                else:
                    print("Obrigado, e volte sempre!")
                    data_emprestimo()
                    break
            else:
                print("O numero digitado nao contem na lista, Por favor digite Novamente outro número!")

        elif (genero == 6):
            print("#"*40)
            print("\n".join(terror))
            emprestimo_terror = int(input("\n Temos essas opções para emprestimo, digite o numero do Livro que voce quer retirar: #só numero, exemplo - (02)\n"))
            # Removendo o livro da Lista
            while emprestimo_terror in range(1, 28):
                terror.pop(emprestimo_terror-1)
                print("\n".join(terror))
                print("\nLivro retirado com sucesso!")
                time.sleep(3)
                continua = input("\nVoce deseja retirar mais algum livro?[S/N]\n").lower()
                if continua == "s":
                    emprestimo_terror = int(input("\n Temos essas opções para emprestimo, digite o numero do Livro que voce quer retirar: #só numero, exemplo - (02)\n"))
                else:
                    print("Obrigado, e volte sempre!")
                    data_emprestimo()
                    break
            else:
                print("O numero digitado nao contem na lista, Por favor digite Novamente outro número!")

        elif (genero == 7):
            print("#"*40)
            print("\n".join(suspense))
            emprestimo_suspense = int(input("\n Temos essas opções para emprestimo, digite o numero do Livro que voce quer retirar: #só numero, exemplo - (02)\n"))
            # Removendo o livro da Lista
            while emprestimo_suspense in range(1, 28):
                suspense.pop(emprestimo_suspense-1)
                print("\n".join(suspense))
                print("\nLivro retirado com sucesso!")
                time.sleep(3)
                continua = input("\nVoce deseja retirar mais algum livro?[S/N]\n").lower()
                if continua == "s":
                    emprestimo_suspense = int(input("\n Temos essas opções para emprestimo, digite o numero do Livro que voce quer retirar: #só numero, exemplo - (02)\n"))
                else:
                    print("Obrigado, e volte sempre!")
                    data_emprestimo()
                    break
            else:
                print("O numero digitado nao contem na lista, Por favor digite Novamente outro número!")

        elif (genero == 8):
            print("#"*40)
            print("\n".join(ficcao))
            emprestimo_ficcao = int(input("\n Temos essas opções para emprestimo, digite o numero do Livro que voce quer retirar: #só numero, exemplo - (02)\n"))
            # Removendo o livro da Lista
            while emprestimo_ficcao in range(1, 28):
                suspense.pop(emprestimo_ficcao-1)
                print("\n".join(ficcao))
                print("\nLivro retirado com sucesso!")
                time.sleep(3)
                continua = input(
                    "\nVoce deseja retirar mais algum livro?[S/N]\n").lower()
                if continua == "s":
                    emprestimo_ficcao = int(input(
                        "\n Temos essas opções para emprestimo, digite o numero do Livro que voce quer retirar: #só numero, exemplo - (02)\n"))
                else:
                    print("Obrigado, e volte sempre!")
                    data_emprestimo()
                    break
            else:
                print(
                    "O numero digitado nao contem na lista, Por favor digite Novamente outro número!")

# DEVOLUÇÂO DE LIVROS
    if (opcao == 2):

        # Data atual
        data_atual = datetime.date.today()

        # Data do empréstimo
        data_emprestimo_str = input("Informe a data que você retirou o(s) livro(s) - (DIA/MES/ANO): ")
        data_emprestimo_str = dt.datetime.strptime(data_emprestimo_str, '%d/%m/%Y')
        print(data_emprestimo_str.date())
        ano, mes, dia = data_emprestimo_str.year, data_emprestimo_str.month, data_emprestimo_str.day
        dia_emprestimo = dt.date(ano, mes, dia)

        # Verifica se já se passaram 14 dias desde a data do empréstimo
        dias_passados = (data_atual - dia_emprestimo).days
        print(f"\nForam {dias_passados} dias desde que, foi feito o emprestimo!")
        if dias_passados >= 14:
            print("Infelizmente, ja passou do prazo!")
            cpf = str(input("Informe seu CPF:")).replace('.', '').replace('-', '')
            if len(cpf) == 11:
                print("CPF verificado... Infelizmente voce ficará 1 mes, sem poder pegar nenhum livro emprestado!\n")
                time.sleep(2)
                nome_livro = str(input("Digite o nome do livro que voce irá devolver:"))
                print("O livro '" + nome_livro +"' foi devolvido com sucesso!")
                verificacao = str(input("Tem mais algum livro pra ser devolvido?[S/N]\n")).upper()
                while verificacao == 'S':
                    nome_livro = str(input("Digite o nome do livro que voce irá devolver:"))
                    print("O livro '" + nome_livro +"' foi devolvido com sucesso!")
                    verificacao = str(input("Tem mais algum livro pra ser devolvido?[S/N]\n")).upper()

                else:
                    print("Muito obrigado por utilizar, a Biblioteca...")

            else:
                print(
                    "CPF invalido, por favor insira seu CPF novamente, os 11 digitos.. ")

        else:
            nome_livro = str(
                input("Digite o nome do livro que voce irá devolver:"))
            print("O livro '" + nome_livro + "' foi devolvido com sucesso!")
            verificacao = str(
                input("Tem mais algum livro pra ser devolvido?[S/N]\n")).upper()
            while verificacao == 'S':
                nome_livro = str(
                    input("Digite o nome do livro que voce irá devolver:"))
                print("O livro '" + nome_livro +
                      "' foi devolvido com sucesso!")
                verificacao = str(
                    input("Tem mais algum livro pra ser devolvido?[S/N]\n")).upper()
            else:
                print("Muito obrigado por utilizar, a Biblioteca... Volte Sempre")
                print(
                    "Quem lê expande as próprias ideias e se transporta para outros mundos.")

# CADASTRO USUARIO
    if (opcao == 3):
        dados()

# FINALIZAR PROGRAMA
    if (opcao == 4):
        print("finalizando... Obrigado e volte sempre!!")

# AVALIAÇÂO DA BIBLIOTECA
    if (opcao == 5):
        print("Por favor, avalie o atendimento na biblioteca de 1 a 10:")
        avaliacao = input()
        avaliacao = int(avaliacao)

        if avaliacao >= 1 and avaliacao <= 10:
            if avaliacao < 4:
                print("O atendimento na biblioteca foi extremamente insatisfatório.")
            elif avaliacao < 6:
                print("O atendimento na biblioteca foi insatisfatório.")
            elif avaliacao < 8:
                print("O atendimento na biblioteca foi bom.")
            elif avaliacao < 10:
                print("O atendimento na biblioteca foi excelente.")
            else:
                print("O atendimento na biblioteca foi perfeito.")
        else:
            print("Por favor, avalie o atendimento na biblioteca de 1 a 10.")


#CRIANDO A DATA QUE VAI SER DEFINIDA QUANTOS DIAS DURARÁ O EMPRESTIMO!
def data_emprestimo():
    hoje = datetime.date.today()
    delta = datetime.timedelta(days=14)
    devolucao = hoje + delta 
    print(f"A data que vocẽ está retirando o livro(s) é o dia: {hoje.day}/{hoje.month}/{hoje.year}!!!\n")
    print("--"*30)
    print(f"######## A devolução tem que ocorrer até o dia: {devolucao.day}/{devolucao.month}/{devolucao.year}!!! ########\n")
    print("--"*30)
    print("Caso não ocorra, terá seu CPF bloqueado na Biblioteca!")
    
# CATALAGOS DOS LIVROS
catalogo_livro()

# VERIFICAÇÂO DA DEVOLUÇÂO DO LIVRO

if __name__ == '__main__':
    bem_vindo()
