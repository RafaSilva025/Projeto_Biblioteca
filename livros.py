import sqlite3

def bemvindo():
    print("*********************************")
    print("***********BEM VINDO!************")
    print("*********************************\n")
    print("-----------Biblioteca------------\n")
    cadastro()

def cadastro():
    con = sqlite3.connect('usuarios.db')
    cursor = con.cursor()

    # VERIFICAÇÂO DE USUARIO
    print("Informe seu CPF cadastrado, para acessar a biblioteca, caso nao tenha ou digite um CPF irregular, irá automaticamente pra tela de cadastro!")
    verificacao_usuario = str(input("-")).replace('.', '').replace('-', '') 

    for dados_banco in cursor.execute(f'''SELECT nome, cpf, telefone FROM usuarios'''): 
        if verificacao_usuario != dados_banco[1]:
            print("\n------CADASTRO------")
            nome = str(input("Digite seu nome:")).title()
            cpf = str(input("Digite seu CPF:"))
            telefone = int(input("Digite seu Telefone/Celular:"))
            
            cursor.execute(f"INSERT INTO usuarios VALUES ('{nome}' , '{cpf}' , '{telefone}')")
            con.commit()
            
        if verificacao_usuario == dados_banco[1]:
            print(f"\nSeja Bem-Vindo")
            print("Perfeito, tudo certo, vamos prossegir...")
            
                

# CATALAGOS DOS LIVROS
    def catalogo_livro():
        comedia = ['Livro 01-A Extraordinária Viagem do Faquir Que Ficou Preso Em um Armário Ikea',
                'Livro 02-A Troca, Ed Mort – Todas as Histórias', 'Livro 03-Cadê Você Bernadette?', 'Livro 04-O Diabo Veste Prada', 'Livro 05-Te Vendo Um Cachorro', 'Livro 06-Vermelho, Branco e Sangue Azul']

        romance = ['Livro 01-10 DATES SURPRESA', 'Livro 02-13 SEGUNDOS', 'Livro 03-4 HOMENS EM 44 CAPÍTULOS', 'Livro 04-A ALTURA DESLUMBRANTE', 'Livro 05-A BARRACA DO BEIJO', 'Livro 06-A BUSCA', 'Livro 07-A CANÇÃO DA ÓRFÃ', 'Livro 08-A CANÇÃO DAS ÁGUAS', 'Livro 09-A CIDADE DE VAPOR', 'Livro 10-A CINCO PASSOS DE VOCÊ',
                'Livro 11-A CORRIDA DE ESCORPIÃO', 'Livro 12-A DAMA DA MATA LINDÍSSIMO ROMANCE SÁFICO DE FANTASIA', 'Livro 13-A INSUSTENTÁVEL LEVEZA DO SER', 'Livro 14-A LISTA DA SORTE', 'Livro 15-A MALDIÇÃO DO MAR UMA HISTÓRIA SOBRE AMOR E VINGANÇA SURPREENDENTE', 'Livro 16-A PRINCESA PROMETIDA', 'Livro 17-A PROBABILIDADE ESTATÍSTICA DO AMOR À PRIMEIRA VISTA', 'Livro 18-A PROMETIDA SEM CORAÇÃO', 'Livro 19-SER FELIZ É ASSIM', 'Livro 20-SEX EDUCATION: PÉ NA ESTRADA', 'Livro 21-SHINE – UMA CHANCE DE BRILHAR', 'Livro 22-SIMPLESMENTE ACONTECE', 'Livro 23-SOBRE AMOR E ESTRELAS E A CABEÇA NAS NUVENS', 'Livro 24-TRÊS HISTÓRIA ROMÂNTICAS COM OS SIGNOS COMO DESTAQUE', 'Livro 25-SOL DA MEIA-NOITE', 'Livro 26-SOMBRA E OSSOS', 'Livro 27-SONATA EM PUNK ROCK']

        educacao = ['Livro 01-A HISTÓRIA DA ASTROLOGIA PARA QUEM TEM PRESSA', 'Livro 02-A HISTÓRIA DO FUTEBOL PARA QUEM TEM PRESSA',
                    'Livro 03-A HISTÓRIA DO UNIVERSO PARA QUEM TEM PRESSA', 'Livro 04-APARELHO SEXUAL E CIA', 'Livro 05-O QUE TEM DE MAIS LINDO DO QUE ISSO?', 'Livro 06-SEX EDUCATION: UMA GUIA PARA A VIDA']

        infantis = ['Livro 01-ABCDELAS', 'Livro 02-AMIGA URSA', 'Livro 03-CORALINE', 'Livro 04-DESVENTURAS DE UM GAROTO NADA COMUM', 'Livro 05-DR. ALEX', 'Livro 06-EU FICO EM SILÊNCIO', 'Livro 07-HISTÓRIAS DE TERROR PARA CRIANÇAS ESTRANHAS',
                    'Livro 08-JACK E O PORQUINHO DE NATAL', 'Livro 09-MORTINA', 'Livro 10-MORTINA E O PRIMO INSUPORTÁVEL', 'Livro 11-REINAÇÕES DE NARIZINHO', 'Livro 12-TURMA DA MÔNICA: LAÇOS(HQ)']

        aventura = ['Livro 01-A FILHA DAS PROFUNDEZAS', 'Livro 02-A OUTRA VIDA – MAIS DO MESMO, MAS MESMO ASSIM É BOM', 'Livro 03-A VOLTA AO MUNDO EM 80 DIAS', 'Livro 04-ARTEMIS FOWL', 'Livro 05-ENOLA HOLMES', 'Livro 06-JOGADOR NÚMERO DOIS', 'Livro 07-JOGADOR NÚMERO UM', 'Livro 08-MULHERES ESMERALDAS', 'Livro 09-O CASO DA MANSÃO DEBOËN', 'Livro 10-O FOGO ENTRE A NÉVOA', 'Livro 11-O GUIA DA DONZELA PARA ANÁGUAS E PIRATARIA', 'Livro 12-O GUIA DO CAVALHEIRO PARA O VÍCIO E A VIRTUDE', 'Livro 13-O REINO DE ZÁLIA', 'Livro 14-PERCY JACKSON E O LADRÃO DE RAIOS', 'Livro 15-ROBINSON CRUSOÉ'
                    'Livro 16-SEX EDUCATION: PÉ NA ESTRADA', 'Livro 17-UMA JORNADA SEM FIM, A GRANDE SURPRESA DESTE ANO', 'Livro 18-VINGANÇA']

        terror = ['Livro 01-13 DIAS DE MEIA-NOITE', 'Livro 02-A ALCATÉIA', 'Livro 03-A ASSOMBRAÇÃO DA CASA DA COLINA', 'Livro 04-A BALADA DO BLACK TOM, MAIS 13 FATOS SOBRE LOVECRAFT', 'Livro 05-A CIDADE DOS FANTASMAS', 'Livro 06-A HORA DO LOBISOMEM – TERROR CLÁSSICO JUVENIL', 'Livro 07-A INCENDIÁRIA', 'Livro 08-A MALDIÇÃO DO MAR – UMA HISTÓRIA SOBRE AMOR E VINGANÇA SURPREENDENTE', 'Livro 09-A METADE SOMBRIA', 'Livro 10-A NOITE DOS MORTOS-VIVOS, MAIS 5 CURIOSIDADES E 5 DETALHES DA EDIÇÃO',
                'Livro 11-A RAINHA DOS CONDENADOS', 'Livro 12-AMIGO IMAGINÁRIO', 'Livro 13-ANNA VESTIDA DE SANGUE, Livro 14-TRANSFORMA O TERROR EM UMA AVENTURA ALUCINANTE COM UM ROMANCE FOFO', 'Livro 15-AS GÊMEAS DO GELO – UM SUSPENSE COM TOQUES DE TERROR IMPRESSIONANTE', 'Livro 16-ASYLUM E SCARLETS', 'Livro 17-CARMILLA – UMA DAS MELHORES HISTÓRIAS DE VAMPIROS', 'Livro 18-CARRIE, Livro 19-BULLYING E FANATISMO RELIGIOSO NO PRIMEIRO TERROR DE STEPHEN KING', 'Livro 20-CARROSSEL SOMBRIO']

        suspense = ['13 SEGUNDOS', 'A BIBLIOTECA DA MEIA-NOITE', 'A CACHORRA', 'A CASA HOLANDESA', 'A CINCO PASSOS DE VOCÊ', 'A CORRIDA DE ESCORPIÃO', 'A CRIANÇA NO TEMPO', 'A DANÇA DA ÁGUA', 'A ESCRAVA ISAURA',
                    'O LABIRINTO DO FAUNO + 9 CURIOSIDADES', 'O LIVRO DE MEMÓRIAS', 'O MARIDO PERFEITO', 'O MENINO QUE SOBREVIVEU', 'O PODEROSO CHEFÃO', 'O PRIMEIRO E O ÚLTIMO VERÃO', 'O PRÍNCIPE DA NÉVOA', 'O QUE ALICE ESQUECEU']

        ficcao = ['A CURVA DO SONHO', 'A DIABÓLICA', 'A ESTRELA MAIS ESCURA', 'A MÃO ESQUERDA DA ESCURIDÃO', 'A MÁQUINA DO TEMPO', 'A MENINA QUE TINHA DONS', 'A PERGUNTA E A RESPOSTA', 'A QUINTA ESTAÇÃO E O PORTÃO DO OBELISCO', 'A SEGUNDA AURORA', 'ATRAVÉS DO VAZIO', 'AURORA ARDE, CONTINUAÇÃO DAS AVENTURAS DE UM ESQUADRÃO DE HERÓIS', 'AURORA ASCENDE', 'BABEL-17 E ESTRELA IMPERIAL',
                'BINTI(TRILOGIA COMPLETA)', 'CIDADE DA MEIA-NOITE', 'CIDADE NAS NUVENS', 'CINDER', 'DESAFIANDO AS ESTRELAS', 'DESPERTAR', 'DEVORADORES DE ESTRELAS', 'DORMIR EM UM MAR DE ESTRELAS', 'DUNA(LIVRO+HQ)', 'É ASSIM QUE SE PERDE A GUERRA DO TEMPO', 'ESPERE AGORA PELO ANO PASSADO', 'FLORES PARA ALGERNON', 'FLORES PARA ALGERNON, MAIS CINCO MOTIVOS PARA LER', 'FORWARD']
        
        opcao = int(input('SELECIONE OQUE VOCÊ IRÁ FAZER! \n 1- Empréstimo Livro(s) \n 2- Devolução Livro(s)\n 3- Cadastro de Usuario\n\n'))
        if (opcao == 1):
            genero = int(input("\nMuito bem, selecione o Genero do(s) Livro(s): \n 1- Humor\n 2- Romance\n 3- Educação\n 4- Livros infantis/gibis\n 5- Aventura \n 6- Terror\n 7- Suspense/Drama\n 8- Ficção-Científica\n"))
            if (genero == 1):
                print("#"*40)
                print("\n".join(comedia))
                emprestimo_comedia = int(input("\n Temos essas opções para emprestimo, digite o numero do Livro que voce quer retirar: #só numero, exemplo - (02)\n"))

                # Removendo o livro da Lista
                if emprestimo_comedia in range(1,7):
                    comedia.pop(emprestimo_comedia-1)
                    print("\n".join(comedia))
                else: 
                    print("O numero digitado nao contem na lista, Por favor digite Novamente outro número!")    

            elif (genero == 2):
                print("#"*40)
                print("\n".join(romance))
                emprestimo_romance = int(input(
                    "\n Temos essas opções para emprestimo, digite o numero do Livro que voce quer retirar: #só numero, exemplo - (02)\n"))

                # Removendo o livro da Lista
                if emprestimo_romance in range(1, 28):
                    romance.pop(emprestimo_romance-1)
                    print("\n".join(romance))
                else:
                    print("O numero digitado nao contem na lista, Por favor digite Novamente outro número!")

            elif (genero == 3):
                print("#"*40)
                print("\n".join(educacao))
                emprestimo_educacao = int(input(
                    "\n Temos essas opções para emprestimo, digite o numero do Livro que voce quer retirar: #só numero, exemplo - (02)\n"))

                # Removendo o livro da Lista
                if emprestimo_educacao in range(1, 28):
                    educacao.pop(emprestimo_educacao-1)
                    print("\n".join(educacao))
                else:
                    print("O numero digitado nao contem na lista, Por favor digite Novamente outro número!")

            elif (genero == 4):
                print("#"*40)
                print("\n".join(infantis))
                emprestimo_infantil = int(input(
                    "\n Temos essas opções para emprestimo, digite o numero do Livro que voce quer retirar: #só numero, exemplo - (02)\n"))

                # Removendo o livro da Lista
                if emprestimo_infantil in range(1, 28):
                    infantis.pop(emprestimo_infantil-1)
                    print("\n".join(infantis))
                else:
                    print("O numero digitado nao contem na lista, Por favor digite Novamente outro número!")
                
            elif (genero == 5):
                print("#"*40)
                print("\n".join(aventura))
                emprestimo_aventura = int(input(
                    "\n Temos essas opções para emprestimo, digite o numero do Livro que voce quer retirar: #só numero, exemplo - (02)\n"))

                # Removendo o livro da Lista
                if emprestimo_aventura in range(1, 28):
                    aventura.pop(emprestimo_aventura-1)
                    print("\n".join(aventura))
                else:
                    print("O numero digitado nao contem na lista, Por favor digite Novamente outro número!")

            elif (genero == 6):
                print("#"*40)
                print("\n".join(terror))
                emprestimo_terror = int(input(
                    "\n Temos essas opções para emprestimo, digite o numero do Livro que voce quer retirar: #só numero, exemplo - (02)\n"))

                # Removendo o livro da Lista
                if emprestimo_terror in range(1, 28):
                    terror.pop(emprestimo_terror-1)
                    print("\n".join(terror))
                else:
                    print("O numero digitado nao contem na lista, Por favor digite Novamente outro número!")

            elif (genero == 7):
                print("#"*40)
                print("\n".join(suspense))
                emprestimo_suspense = int(input(
                    "\n Temos essas opções para emprestimo, digite o numero do Livro que voce quer retirar: #só numero, exemplo - (02)\n"))
                
                # Removendo o livro da Lista
                if emprestimo_suspense in range(1, 28):
                    suspense.pop(emprestimo_suspense-1)
                    print("\n".join(suspense))
                else:
                    print("O numero digitado nao contem na lista, Por favor digite Novamente outro número!")
                
            elif (genero == 8):
                print("#"*40)
                print("\n".join(ficcao))
                emprestimo_ficcao = int(input("\n Temos essas opções para emprestimo, digite o numero do Livro que voce quer retirar: #só numero, exemplo - (02)\n"))
            
                # Removendo o livro da Lista
                if emprestimo_ficcao in range(1, 28):
                    suspense.pop(emprestimo_ficcao-1)
                    print("\n".join(ficcao))
                else:
                    print("O numero digitado nao contem na lista, Por favor digite Novamente outro número!")
                        
    
# CATALAGOS DOS LIVROS
    def catalogo_livro():
        comedia = ['Livro 01-A Extraordinária Viagem do Faquir Que Ficou Preso Em um Armário Ikea',
                'Livro 02-A Troca, Ed Mort – Todas as Histórias', 'Livro 03-Cadê Você Bernadette?', 'Livro 04-O Diabo Veste Prada', 'Livro 05-Te Vendo Um Cachorro', 'Livro 06-Vermelho, Branco e Sangue Azul']

        romance = ['Livro 01-10 DATES SURPRESA', 'Livro 02-13 SEGUNDOS', 'Livro 03-4 HOMENS EM 44 CAPÍTULOS', 'Livro 04-A ALTURA DESLUMBRANTE', 'Livro 05-A BARRACA DO BEIJO', 'Livro 06-A BUSCA', 'Livro 07-A CANÇÃO DA ÓRFÃ', 'Livro 08-A CANÇÃO DAS ÁGUAS', 'Livro 09-A CIDADE DE VAPOR', 'Livro 10-A CINCO PASSOS DE VOCÊ',
                'Livro 11-A CORRIDA DE ESCORPIÃO', 'Livro 12-A DAMA DA MATA LINDÍSSIMO ROMANCE SÁFICO DE FANTASIA', 'Livro 13-A INSUSTENTÁVEL LEVEZA DO SER', 'Livro 14-A LISTA DA SORTE', 'Livro 15-A MALDIÇÃO DO MAR UMA HISTÓRIA SOBRE AMOR E VINGANÇA SURPREENDENTE', 'Livro 16-A PRINCESA PROMETIDA', 'Livro 17-A PROBABILIDADE ESTATÍSTICA DO AMOR À PRIMEIRA VISTA', 'Livro 18-A PROMETIDA SEM CORAÇÃO', 'Livro 19-SER FELIZ É ASSIM', 'Livro 20-SEX EDUCATION: PÉ NA ESTRADA', 'Livro 21-SHINE – UMA CHANCE DE BRILHAR', 'Livro 22-SIMPLESMENTE ACONTECE', 'Livro 23-SOBRE AMOR E ESTRELAS E A CABEÇA NAS NUVENS', 'Livro 24-TRÊS HISTÓRIA ROMÂNTICAS COM OS SIGNOS COMO DESTAQUE', 'Livro 25-SOL DA MEIA-NOITE', 'Livro 26-SOMBRA E OSSOS', 'Livro 27-SONATA EM PUNK ROCK']

        educacao = ['Livro 01-A HISTÓRIA DA ASTROLOGIA PARA QUEM TEM PRESSA', 'Livro 02-A HISTÓRIA DO FUTEBOL PARA QUEM TEM PRESSA',
                    'Livro 03-A HISTÓRIA DO UNIVERSO PARA QUEM TEM PRESSA', 'Livro 04-APARELHO SEXUAL E CIA', 'Livro 05-O QUE TEM DE MAIS LINDO DO QUE ISSO?', 'Livro 06-SEX EDUCATION: UMA GUIA PARA A VIDA']

        infantis = ['Livro 01-ABCDELAS', 'Livro 02-AMIGA URSA', 'Livro 03-CORALINE', 'Livro 04-DESVENTURAS DE UM GAROTO NADA COMUM', 'Livro 05-DR. ALEX', 'Livro 06-EU FICO EM SILÊNCIO', 'Livro 07-HISTÓRIAS DE TERROR PARA CRIANÇAS ESTRANHAS',
                    'Livro 08-JACK E O PORQUINHO DE NATAL', 'Livro 09-MORTINA', 'Livro 10-MORTINA E O PRIMO INSUPORTÁVEL', 'Livro 11-REINAÇÕES DE NARIZINHO', 'Livro 12-TURMA DA MÔNICA: LAÇOS(HQ)']

        aventura = ['Livro 01-A FILHA DAS PROFUNDEZAS', 'Livro 02-A OUTRA VIDA – MAIS DO MESMO, MAS MESMO ASSIM É BOM', 'Livro 03-A VOLTA AO MUNDO EM 80 DIAS', 'Livro 04-ARTEMIS FOWL', 'Livro 05-ENOLA HOLMES', 'Livro 06-JOGADOR NÚMERO DOIS', 'Livro 07-JOGADOR NÚMERO UM', 'Livro 08-MULHERES ESMERALDAS', 'Livro 09-O CASO DA MANSÃO DEBOËN', 'Livro 10-O FOGO ENTRE A NÉVOA', 'Livro 11-O GUIA DA DONZELA PARA ANÁGUAS E PIRATARIA', 'Livro 12-O GUIA DO CAVALHEIRO PARA O VÍCIO E A VIRTUDE', 'Livro 13-O REINO DE ZÁLIA', 'Livro 14-PERCY JACKSON E O LADRÃO DE RAIOS', 'Livro 15-ROBINSON CRUSOÉ'
                    'Livro 16-SEX EDUCATION: PÉ NA ESTRADA', 'Livro 17-UMA JORNADA SEM FIM, A GRANDE SURPRESA DESTE ANO', 'Livro 18-VINGANÇA']

        terror = ['Livro 01-13 DIAS DE MEIA-NOITE', 'Livro 02-A ALCATÉIA', 'Livro 03-A ASSOMBRAÇÃO DA CASA DA COLINA', 'Livro 04-A BALADA DO BLACK TOM, MAIS 13 FATOS SOBRE LOVECRAFT', 'Livro 05-A CIDADE DOS FANTASMAS', 'Livro 06-A HORA DO LOBISOMEM – TERROR CLÁSSICO JUVENIL', 'Livro 07-A INCENDIÁRIA', 'Livro 08-A MALDIÇÃO DO MAR – UMA HISTÓRIA SOBRE AMOR E VINGANÇA SURPREENDENTE', 'Livro 09-A METADE SOMBRIA', 'Livro 10-A NOITE DOS MORTOS-VIVOS, MAIS 5 CURIOSIDADES E 5 DETALHES DA EDIÇÃO',
                'Livro 11-A RAINHA DOS CONDENADOS', 'Livro 12-AMIGO IMAGINÁRIO', 'Livro 13-ANNA VESTIDA DE SANGUE, Livro 14-TRANSFORMA O TERROR EM UMA AVENTURA ALUCINANTE COM UM ROMANCE FOFO', 'Livro 15-AS GÊMEAS DO GELO – UM SUSPENSE COM TOQUES DE TERROR IMPRESSIONANTE', 'Livro 16-ASYLUM E SCARLETS', 'Livro 17-CARMILLA – UMA DAS MELHORES HISTÓRIAS DE VAMPIROS', 'Livro 18-CARRIE, Livro 19-BULLYING E FANATISMO RELIGIOSO NO PRIMEIRO TERROR DE STEPHEN KING', 'Livro 20-CARROSSEL SOMBRIO']

        suspense = ['13 SEGUNDOS', 'A BIBLIOTECA DA MEIA-NOITE', 'A CACHORRA', 'A CASA HOLANDESA', 'A CINCO PASSOS DE VOCÊ', 'A CORRIDA DE ESCORPIÃO', 'A CRIANÇA NO TEMPO', 'A DANÇA DA ÁGUA', 'A ESCRAVA ISAURA',
                    'O LABIRINTO DO FAUNO + 9 CURIOSIDADES', 'O LIVRO DE MEMÓRIAS', 'O MARIDO PERFEITO', 'O MENINO QUE SOBREVIVEU', 'O PODEROSO CHEFÃO', 'O PRIMEIRO E O ÚLTIMO VERÃO', 'O PRÍNCIPE DA NÉVOA', 'O QUE ALICE ESQUECEU']

        ficcao = ['A CURVA DO SONHO', 'A DIABÓLICA', 'A ESTRELA MAIS ESCURA', 'A MÃO ESQUERDA DA ESCURIDÃO', 'A MÁQUINA DO TEMPO', 'A MENINA QUE TINHA DONS', 'A PERGUNTA E A RESPOSTA', 'A QUINTA ESTAÇÃO E O PORTÃO DO OBELISCO', 'A SEGUNDA AURORA', 'ATRAVÉS DO VAZIO', 'AURORA ARDE, CONTINUAÇÃO DAS AVENTURAS DE UM ESQUADRÃO DE HERÓIS', 'AURORA ASCENDE', 'BABEL-17 E ESTRELA IMPERIAL',
                'BINTI(TRILOGIA COMPLETA)', 'CIDADE DA MEIA-NOITE', 'CIDADE NAS NUVENS', 'CINDER', 'DESAFIANDO AS ESTRELAS', 'DESPERTAR', 'DEVORADORES DE ESTRELAS', 'DORMIR EM UM MAR DE ESTRELAS', 'DUNA(LIVRO+HQ)', 'É ASSIM QUE SE PERDE A GUERRA DO TEMPO', 'ESPERE AGORA PELO ANO PASSADO', 'FLORES PARA ALGERNON', 'FLORES PARA ALGERNON, MAIS CINCO MOTIVOS PARA LER', 'FORWARD']
# EMPRESTIMO DO LIVRO

        opcao = int(input('SELECIONE OQUE VOCÊ IRÁ FAZER! \n 1- Empréstimo Livro(s) \n 2- Devolução Livro(s)\n 3- Cadastro de Usuario\n\n'))
        if (opcao == 1):
            genero = int(input("\nMuito bem, selecione o Genero do(s) Livro(s): \n 1- Humor\n 2- Romance\n 3- Educação\n 4- Livros infantis/gibis\n 5- Aventura \n 6- Terror\n 7- Suspense/Drama\n 8- Ficção-Científica\n"))
            if (genero == 1):
                print("#"*40)
                print("\n".join(comedia))
                emprestimo_comedia = int(input("\n Temos essas opções para emprestimo, digite o numero do Livro que voce quer retirar: #só numero, exemplo - (02)\n"))

                # Removendo o livro da Lista
                if emprestimo_comedia in range(1,7):
                    comedia.pop(emprestimo_comedia-1)
                    print("\n".join(comedia))
                else: 
                    print("O numero digitado nao contem na lista, Por favor digite Novamente outro número!")    

            elif (genero == 2):
                print("#"*40)
                print("\n".join(romance))
                emprestimo_romance = int(input(
                    "\n Temos essas opções para emprestimo, digite o numero do Livro que voce quer retirar: #só numero, exemplo - (02)\n"))

                # Removendo o livro da Lista
                if emprestimo_romance in range(1, 28):
                    romance.pop(emprestimo_romance-1)
                    print("\n".join(romance))
                else:
                    print("O numero digitado nao contem na lista, Por favor digite Novamente outro número!")

            elif (genero == 3):
                print("#"*40)
                print("\n".join(educacao))
                emprestimo_educacao = int(input(
                    "\n Temos essas opções para emprestimo, digite o numero do Livro que voce quer retirar: #só numero, exemplo - (02)\n"))

                # Removendo o livro da Lista
                if emprestimo_educacao in range(1, 28):
                    educacao.pop(emprestimo_educacao-1)
                    print("\n".join(educacao))
                else:
                    print("O numero digitado nao contem na lista, Por favor digite Novamente outro número!")

            elif (genero == 4):
                print("#"*40)
                print("\n".join(infantis))
                emprestimo_infantil = int(input(
                    "\n Temos essas opções para emprestimo, digite o numero do Livro que voce quer retirar: #só numero, exemplo - (02)\n"))

                # Removendo o livro da Lista
                if emprestimo_infantil in range(1, 28):
                    infantis.pop(emprestimo_infantil-1)
                    print("\n".join(infantis))
                else:
                    print("O numero digitado nao contem na lista, Por favor digite Novamente outro número!")
                
            elif (genero == 5):
                print("#"*40)
                print("\n".join(aventura))
                emprestimo_aventura = int(input(
                    "\n Temos essas opções para emprestimo, digite o numero do Livro que voce quer retirar: #só numero, exemplo - (02)\n"))

                # Removendo o livro da Lista
                if emprestimo_aventura in range(1, 28):
                    aventura.pop(emprestimo_aventura-1)
                    print("\n".join(aventura))
                else:
                    print("O numero digitado nao contem na lista, Por favor digite Novamente outro número!")

            elif (genero == 6):
                print("#"*40)
                print("\n".join(terror))
                emprestimo_terror = int(input(
                    "\n Temos essas opções para emprestimo, digite o numero do Livro que voce quer retirar: #só numero, exemplo - (02)\n"))

                # Removendo o livro da Lista
                if emprestimo_terror in range(1, 28):
                    terror.pop(emprestimo_terror-1)
                    print("\n".join(terror))
                else:
                    print("O numero digitado nao contem na lista, Por favor digite Novamente outro número!")

            elif (genero == 7):
                print("#"*40)
                print("\n".join(suspense))
                emprestimo_suspense = int(input(
                    "\n Temos essas opções para emprestimo, digite o numero do Livro que voce quer retirar: #só numero, exemplo - (02)\n"))
                
                # Removendo o livro da Lista
                if emprestimo_suspense in range(1, 28):
                    suspense.pop(emprestimo_suspense-1)
                    print("\n".join(suspense))
                else:
                    print("O numero digitado nao contem na lista, Por favor digite Novamente outro número!")
                
            elif (genero == 8):
                print("#"*40)
                print("\n".join(ficcao))
                emprestimo_ficcao = int(input("\n Temos essas opções para emprestimo, digite o numero do Livro que voce quer retirar: #só numero, exemplo - (02)\n"))
            
                # Removendo o livro da Lista
                if emprestimo_ficcao in range(1, 28):
                    suspense.pop(emprestimo_ficcao-1)
                    print("\n".join(ficcao))
                else:
                    print("O numero digitado nao contem na lista, Por favor digite Novamente outro número!")
                    
        #DEVOLUÇÂO DE LIVROS                     
        elif (opcao == 2):
            nome_livro = input("Digite o nome do livro que você deseja devolver: ")
            print("O livro '" + nome_livro + "' foi devolvido com sucesso!")

        # CADASTRO USUARIO
        elif (opcao == 3):
            cadastro()

        #SELECIONANDO UM OPÇÂO ENEXISTENTE    
        else:
            print("A opção selecionada, não faz parte das opções! POR FAVOR, TENTE NOVAMENTE!! ")
        #VERIFICAÇÂO DA DEVOLUÇÂO DO LIVRO

if __name__=='__main__':
    bemvindo()        

