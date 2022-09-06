#importado a conexão
from conexao import conect
##criando a classe Reserva
class Reserva:
    #inserindo os atributos de Reserva
    def __init__(self,responsavel, data_entrada, data_saida, valor):
        self.responsavel=responsavel
        self.data_entrada=(data_entrada)
        self.data_saida=(data_saida)
        self.valor=float(valor)

    def cadastrar_reserva (self):
        #chamando a classe conect/aquivo conexao;a função conecta para retorna a conexão
        con=conect.conecta(self)
        #cursor para executar query
        cursor=con.cursor()
        #valores que foram inseridos nos atributos da classe
        cursor.execute(f"insert into Reserva values(default,'{self.responsavel}','{self.data_entrada}','{self.data_saida}','{self.valor}')")
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
        print(self.responsavel,self.data_entrada, self.data_saida, self.valor)  