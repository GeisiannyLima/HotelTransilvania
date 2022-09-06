#importando o banco de dados
import mysql.connector
#criando a classe de conexõ
class conect:
    def conecta(self):
        #conectando com banco de dados mysql
        con=mysql.connector.connect(host='localhost', user='root', password='', db='hoteltransilvania')
        #retornando conexão
        return con
