#criando um Menu
opcao=int(input('''''
1.cadastrar quarto
2.cadastrar hóspede
3.cadastrar serviço
4.cadastrar funcionário
5.cadastrar reserva
'''''))
#Criando as opções
if(opcao==1):
    #importar, classe Hospede/arquivo hospede
    from quarto import Quarto
    #solicitando ao usúario para inserir os dados
    tipo=str(input('Informe o tipo do quarto: '))
    numero=str(input('Informe o número do quarto: '))
    padrao=str(input('Informe o padrão do quarto: '))
    qtde_pessoas=str(input('Informe a capacidade de pessoas para o quarto: '))
    valor=str(input('Informe o valor da diária: '))
    #instanciando a classe Quarto
    qua1=Quarto(tipo,numero,padrao,qtde_pessoas,valor)
    #depois chama o método para inserir os dados enviados acima
    qua1.cadastrar_quarto()

elif(opcao==2):
    #importando a classe Hospede do arquivo hospede 
    from hospede import Hospede
    #pedindo para o usuário informar os dados
    nome=str(input('Informe o nome do hóspede: '))
    email=str(input('Informe o E-mail do hóspede: '))
    cpf=str(input('Informe o CPF do hóspede: '))
    rg=str(input('Informe o RG do hóspede: '))
    data_nasc=str(input('Informe a data de nascimento(AAAA-mm-dd) do hóspede: '))
    #instanciando classe Hospede, esse é o momento que inicializamos os atrbutos do 
    #self
    hos1=Hospede(nome,email,cpf,rg,data_nasc)
    #depois chama o método para inserir os dados enviados acima
    hos1.cadastrar_hospede()
    
elif(opcao==3):
    #importar, classe Hospede/arquivo hospede
    from servicos import Servicos
    #solicitando ao usúario para inserir os dados
    Nome=str(input('Informe o nome do serviço: '))
    custo=str(input('Informe o valor do serviço: '))
    #instanciando a classe Quarto
    ser1=Servicos(nome, custo)
    #depois chama o método para inserir os dados enviados acima
    ser1.cadastrar_servicos()

elif(opcao==4):
    #importar, classe Hospede/arquivo hospede
    from funcionario import Funcionario
    #solicitando ao usúario para inserir os dados
    nome=str(input('Informe o tipo do quarto: '))
    email=str(input('Informe o número do quarto: '))
    cpf=str(input('Informe o padrão do quarto: '))
    rg=str(input('Informe a capacidade de pessoas para o quarto: '))
    data_nasc=str(input('Informe o valor da diária: '))
    data_admissao=str(input('Informe a capacidade de pessoas para o quarto: '))
    remuneracao=str(input('Informe o valor da diária: '))
    #instanciando a classe Quarto
    fun1=Funcionario(nome, email, cpf, rg, data_nasc, data_admissao, remuneracao)
    #depois chama o método para inserir os dados enviados acima
    fun1.cadastrar_funcionario()

elif(opcao==5):
    #importar, classe Hospede/arquivo hospede
    from reserva import Reserva
    #solicitando ao usúario para inserir os dados
    responsavel=str(input('Informe o nome do reponsável: '))
    data_entrada=str(input('Informe a data de entrada: '))
    data_saida=str(input('Informe a data de saída: '))
    valor=str(input('Informe o valor: '))
    #instanciando a classe Quarto
    res1= Reserva (responsavel, data_entrada, data_saida, valor)
    #depois chama o método para inserir os dados enviados acima
    res1.cadastrar_reserva()   