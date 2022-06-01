import sqlite3 as bancoDados

#  CRIANDO CAMINHO PARA O BANCO E PRAGMA SERVE PARA ATIVAR A FK(CHAVE ESTRANGEIRA)
bancoDados = bancoDados.connect("bancoDados.db")
bancoDados.execute("PRAGMA foreign_keys=on")
cursor = bancoDados.cursor()

try:
    createTable = """CREATE TABLE IF NOT EXISTS hospital(
                    cnpj VARCHAR(11) NOT NULL,
                    nome VARCHAR(20) NOT NULL,
                    rua VARCHAR(50) NOT NULL,
                    bairro VARCHAR(20) NOT NULL,
                    cidade VARCHAR(20) NOT NULL,
                    cep VARCHAR(8) NOT NULL,
                    PRIMARY KEY(cnpj)
                );
                CREATE TABLE medico(
                    crm INTEGER NOT NULL,
                    cpfMedico VARCHAR(11) NOT NULL,
                    nome VARCHAR(50) NOT NULL,
                    rua VARCHAR(50) NOT NULL,
                    bairro VARCHAR(20) NOT NULL,
                    cidade VARCHAR(20),
                    cep VARCHAR(8) NOT NULL,
                    especialidade TEXT NOT NULL,
                    PRIMARY KEY(crm)
                );
                CREATE TABLE telefone(
                    cod_tel INTEGER NOT NULL,
                    contato1 VARCHAR(10),
                    contato2 VARCHAR(10),
                    crm INTEGER,
                    PRIMARY KEY(cod_tel AUTOINCREMENT),
                    FOREIGN KEY(crm) 
                        REFERENCES medico(crm)
                );
                CREATE TABLE enfermeira(
                    coren VARCHAR(10),
                    cpfEnfermeira VARCHAR(11),
                    nome VARCHAR(50),
                    rua VARCHAR(50),
                    bairro VARCHAR(20),
                    cidade VARCHAR(20),
                    cep VARCHAR(8),
                    PRIMARY KEY(coren)
                );
                    CREATE TABLE paciente(
                    cpfPaciente VARCHAR(11) NOT NULL,
                    rg VARCHAR(10) NOT NULL,
                    nome VARCHAR(50) NOT NULL,
                    rua VARCHAR(50) NOT NULL,
                    bairro VARCHAR(20) NOT NULL,
                    cidade VARCHAR(20) NOT NULL,
                    cep VARCHAR(8) NOT NULL,
                    PRIMARY KEY(cpfPaciente)
                );
                    CREATE TABLE tratamento(
                    cod_tratamento INTEGER NOT NULL,
                    nomeTratamento VARCHAR(20),
                    crm VARCHAR(10),
                    PRIMARY KEY(cod_tratamento AUTOINCREMENT),
                    FOREIGN KEY(crm)
                        REFERENCES medico(crm)
                );"""

    bancoDados.executescript(createTable)
    bancoDados.commit()
    print("\n\033[1;32mTABELAS FORAM CRIADAS COM SUCESSO\033[m\n")
    cursor.close()
    bancoDados.close()

except bancoDados.DatabaseError or bancoDados.OperationalError as erro:
    print(f"\n\033[1;31mERRO AO CRIAR TABELAS. ERRO:{erro}\033[m\n")