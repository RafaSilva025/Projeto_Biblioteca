
'''#VALIDADOR DE CPF
def quantidade():
    if len(verificacao_usuario) <11 or len(verificacao_usuario) > 11:
        #print(f"O CPF é invalido pois nele há {len(verificacao_usuario)} caracteres")
        return False
    else:
        return True   ''' 
        
        '''if quantidade() == False:
    print("CPF é invalido!")
else:
    usuario = cursor'''

'''
    def devolucao(self, userKey, livroKey):
        livroKey = geradorCodigo(livroKey)
        usuario = self.__Arvoreusuario.pesquisar(int(userKey))
        livro = self.__Arvorelivro.pesquisar(int(livroKey))
        nomeLivro = self.__Arvorelivro.pesquisar(int(livroKey)).getValor()
        if usuario != None and livro != None:
            if nomeLivro in usuario.getValor().getListaLivros():
                indice = usuario.getValor().getListaLivros().index(nomeLivro)
                usuario.getValor().removeLivroListaLivros(indice)
                livro.getValor().setSituacao(True)
                hj = livro.getValor().strHoje()
                ft = livro.getValor().strFuturo()
                if hj < ft:
                    printar = "Você devolveu na data prevista e não gerou multas"
                else:
                    multa = hj - ft
                    printar = "Você não entregou na data prevista, entao sua multa é de" + \
                        str(multa)
                print(printar)
                return
            else:
                print("O usuário não pode devolver um livro que não possui")


def verificando_emprestimo(self):
    pass
'''
# criar uma avaliação sobre a biblioteca!!''
