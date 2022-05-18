import sqlite3 as bancoDados

#  CRIANDO CAMINHO PARA O BANCO E PRAGMA SERVE PARA ATIVAR A FK(CHAVE ESTRANGEIRA)
bancoDados = bancoDados.connect("bancoDados.db")
bancoDados.execute("PRAGMA foreign_keys=on")
cursor = bancoDados.cursor()

createTable = """CREATE TABLE hospital(
                cnpj VARCHAR(11) NOT NULL,
                nome VARCHAR(20) NOT NULL,
                rua VARCHAR(50) NOT NULL,
                bairro VARCHAR(20) NOT NULL,
                cidade VARCHAR(20) NOT NULL,
                cep VARCHAR(8) NOT NULL,
                telefone VARCHAR(10),
                PRIMARY KEY(cnpj)
            );
            
            """