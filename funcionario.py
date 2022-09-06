#importado a conexão
from conexao import conect
##criando a classe Funcionário
class Funcionario:
    #inserindo os atributos de Funcionário
    def __init__ (self, nome,email,cpf,rg,data_nasc,data_admissao,remuneracao):
        self.nome=nome
        self.email=email
        self.cpf=cpf
        self.rg=rg
        self.data_nasc=data_nasc
        self.data_admissao=data_admissao
        self.remuneracao=remuneracao

    def cadastrar_funcionario (self):
        #chamando a classe conect/aquivo conexao;a função conecta para retorna a conexão
        con=conect.conecta(self)
        #cursor para executar query
        cursor=con.cursor()
        #valores que foram inseridos nos atributos da classe
        cursor.execute(f"insert into Funcionario values(default,'{self.nome}','{self.email}','{self.cpf}','{self.rg}','{self.data_nasc}','{self.data_admissao}','{self.remuneracao}')")
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

    #criando uma fução para listar os atributos da classe
    def Listar (self):
        print(self.nome, self.email,self.cpf,self.rg,self.data_nasc,self.data_admissao,self.remuneracao)   