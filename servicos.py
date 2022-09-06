from conexao import conect
##criando a classe Serviços
class Servicos:
    #inserindo os atributos de Serviços
    def __init__ (self,nome,custo):
        self.nome=nome
        self.custo=int(custo)

    def cadastrar_servicos (self):
        #chamando a classe conect/aquivo conexao;a função conecta para retorna a conexão
        con=conect.conecta(self)
        #cursor para executar query
        cursor=con.cursor()
        #valores que foram inseridos nos atributos da classe
        cursor.execute(f"insert into Servicos values(default,'{self.nome}','{self.custo}')")
        #commit para efetivar a query
        con.commit()
        #rowcount para mostrar o número de linhas afetadas com a query
        row=cursor.rowcount
        #se o resultado for maior que 0, significa q foi inserido
        if(row>0):
            #print mostra a mensagem se der tudo certo
            print('Inserido com sucesso!')
        #caso contrário, aparecerá essa outra mensagem
        else:
            print('Erro!')

    #listando os atributos da classe
    def Listar (self):
        print(self.nome, self.custo) 
