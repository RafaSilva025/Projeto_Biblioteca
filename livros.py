import view

print("*********************************")
print("***********BEM VINDO!************")
print("*********************************\n")
print("-----------Biblioteca------------\n")

opcao = int(input('SELECIONE OQUE VOCÊ IRÁ FAZER! \n 1- Empréstimo Livro(s) \n 2- Devolução Livro(s)\n 3- Cadastro de Usuario\n\n'))

if (opcao == 1):
    print("\nMuito bem, preencha os dados para a liberação do(s) Livro(s):")
    
    Nome = str(input("Nome completo: \n"))
    view.Usuario()
elif (opcao == 2):
    Cpf_Usuario = str(input("Perfeito, informe seu CPF para verificar status de devolução! "))    





    
class Livro:
    def __init__(self, Nome_Livro, Usuario, limite, codigo_livro):
        print(f"Construindo objeto...{self}")
        self.__Nome_Livro = Livro
        self.__Usuario = Usuario
        self.__limite = limite
        self.__codigo_livro = "001"


def devolucao(self):
    pass
    
def verificando_emprestimo(self):
    pass

def emprestimo(self):
    pass    

def cadastrarLivro(self, titulo, genero):
    codigo = geradorCodigo(titulo)
    novolivro = Livro(titulo, codigo, genero)
    self.__Listalivro.adicionar(int(codigo), novolivro)
    print("O livro: " + titulo + " foi cadastrado com sucesso")


