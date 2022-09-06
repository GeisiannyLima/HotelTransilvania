#importado a conexão
from conexao import conect
##criando a classe Quarto
class Quarto:
    #inserindo os atributos de Quarto
    def __init__ (self, tipo,numero,padrao,qtde_pessoas,valor):
        self.tipo=tipo
        self.numero=numero
        self.padrao=padrao
        self.qtde_pessoas=int(qtde_pessoas)
        self.valor=float(valor)

    def cadastrar_quarto (self):
        #chamando a classe conect/aquivo conexao;a função conecta para retorna a conexão
        con=conect.conecta(self)
        #cursor para executar query
        cursor=con.cursor()
        #valores que foram inseridos nos atributos da classe
        cursor.execute(f"insert into Quarto values(default,'{self.tipo}','{self.numero}','{self.padrao}','{self.qtde_pessoas}','{self.valor}')")
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
        print(self.tipo, self.numero,self.padrao,self.qtde_pessoas,self.valor)   