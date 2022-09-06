-- Banco de dados: `hoteltranssilvania`
--

-- --------------------------------------------------------
CREATE DATABASE hoteltranssilvania;
--
-- Estrutura da tabela `Hospede`
CREATE TABLE Hospede (
    id_hospede INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255), 
    email VARCHAR(255), 
    cpf VARCHAR(20), 
    rg VARCHAR(20),
    data_nasc VARCHAR(20));
    
-- Estrutura da tabela `Funcionario`
CREATE TABLE Funcionario (
    id_funcionario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255), 
    email VARCHAR(255), 
    cpf VARCHAR(20), 
    rg VARCHAR(20), 
    data_nasc VARCHAR(20),
    data_admissao VARCHAR(20),
    remuneracao VARCHAR(20),
    senha varchar(255)
    );
    
-- Estrutura da tabela `Quarto`
CREATE TABLE Quarto (
    id_quarto INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(255), 
    numero VARCHAR(255), 
    padrao VARCHAR(255), 
    qtde_pessoas VARCHAR(20),
    valor VARCHAR(20));
    
-- Estrutura da tabela `Servicos`
    CREATE TABLE Servicos (
    id_serviços INT AUTO_INCREMENT PRIMARY KEY,
    nome_servicos VARCHAR(255), 
    custo VARCHAR(255));
  
 -- Estrutura da tabela `Reserva`   
    CREATE TABLE Reserva ( 
    id_reserva INT AUTO_INCREMENT PRIMARY KEY,
    responsavel VARCHAR(255), 
    data_entrada VARCHAR(255), 
    data_saida VARCHAR(20), 
    valor VARCHAR(20),
    fk_idfuncionario int,
    fk_idhospede int,
    CONSTRAINT FK_reserva_hospede FOREIGN KEY (fk_idhospede)
    REFERENCES Hospede(id_hospede),
     CONSTRAINT FK_reserva_funcionario_id FOREIGN KEY(fk_idfuncionario) REFERENCES Funcionario(id_funcionario)
    );

