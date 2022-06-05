import sqlite3 as bancoDados
from modelo import *
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
                CREATE TABLE especialidade(
                    idEspecialidade INTEGER NOT NULL,
                    especialidade TEXT NOT NULL,
                    medico_crm INTEGER NOT NULL,
                    PRIMARY KEY(idEspecialidade AUTOINCREMENT),
                    FOREIGN KEY(medico_crm)
                        REFERENCES medico(crm)
                );
                CREATE TABLE tratamento(
                    cod_tratamento INTEGER NOT NULL,
                    nomeTratamento VARCHAR(20),
                    PRIMARY KEY(cod_tratamento AUTOINCREMENT)
                );
                CREATE TABLE hospitalMedico(
                    idHospMed INTEGER NOT NULL,
                    cnpj VARCHAR(11) NOT NULL,
                    medico_crm INTEGER NOT NULL,
                    PRIMARY KEY(idHospMed AUTOINCREMENT),
                    FOREIGN KEY(cnpj)
                        REFERENCES hospital(cnpj),
                    FOREIGN KEY(medico_crm) 
                        REFERENCES medico(crm)
                );"""

    bancoDados.executescript(createTable)
    bancoDados.commit()
    print("\n\033[1;32mTABELAS FORAM CRIADAS COM SUCESSO\033[m\n")
except bancoDados.DatabaseError or bancoDados.OperationalError as erro:
    print(f"\n\033[1;31mERRO AO CRIAR TABELAS. ERRO:{erro}\033[m\n")

def linha(tam=42):
    print("_" * tam, end="")
    print("\n")

def cabecalho(txt):
    linha()
    print(txt.center(42))
    linha()

def menu(listOpcoes):
    cont = 1
    for item in listOpcoes:
        print(f"{cont} - \033[1;34m{item}\033[m", end="")
        print("\n")
        cont += 1
    linha()

cabecalho("CADASTRO")
menu(["HOSPITAL", "MÉDICO", "ENFERMEIRA", "PACIENTE", "ALTERAR", "\033[31mDELETAR\033[m", "\033[35mRELATÓRIO\033[m", "SAIR"])

def endereco():
    global nome
    nome = input("\033[1;34mNOME:\033[m ")
    global rua
    rua = input("\033[1;34mRUA:\033[m ")
    global bairro
    bairro = input("\033[1;34mBAIRRO:\033[m ")
    global cidade
    cidade = input("\033[1;34mCIDADE:\033[m ")
    global cep
    cep = input("\033[1;34mCEP:\033[m ")

def listaVazia():
    listaVazia = "LISTA VAZIA"
    print(f"\033[35m{listaVazia.center(42)}\033[m")
    linha()

def cadastrado():
    print("\n\033[32mCADASTRADO COM SUCESSO!\033[m")

def alterado():
    print("\n\033[1;32mALTERADO COM SUCESSO!\033[m")
    linha()
while True:
    try:
        opcao = int(input("DIGITE SUA ESCOLHA: "))
        if opcao == 1: #INSERT
            try:
                cnpj = int(input("\033[1;34mNÚMERO DO CNPJ:\033[m "))
                endereco()

                insertHospital = """INSERT INTO hospital(cnpj, nome, rua, bairro, cidade, cep)
                                    VALUES(:cnpj, :nome, :rua, :bairro, :cidade, :cep);"""
                
                hosp = hospital(cnpj, nome, rua, bairro, cidade, cep)
                cursor.execute(insertHospital, {"cnpj": hosp.cnpj,
                                                "nome": hosp.nome,
                                                "rua": hosp.rua,
                                                "bairro": hosp.bairro,
                                                "cidade": hosp.cidade,
                                                "cep": hosp.cep})
                bancoDados.commit()
                cadastrado()
            except:
                print("\n\033[1;31mNÃO FOI POSSÍVEL ATRIBUIR, POR FAVOR, FAZER NOVAMENTE.\033[m")           
        elif opcao == 2:
            try:
                crm = int(input("\033[1;34mCRM:\033[m "))
                cpfMedico = int(input("\033[1;34mCPF:\033[m "))
                espec = input("\033[1;34mESPECIALIDADE:\033[m ")
                endereco()
                contato1 = input("\033[1;34mCONTATO 1:\033[m ")
                contato2 = input("\033[1;34mCONTATO 2:\033[m ")

                cnpj = int(input("\033[1;34mCNPJ DO HOSPITAL QUE TRABALHA:\033[m "))
                
                insertMedico = """INSERT INTO medico(crm, cpfMedico, nome, rua, bairro, cidade, cep)
                                VALUES(:crm, :cpfMedico, :nome, :rua, :bairro, :cidade, :cep);"""
                insertContatoMedico = """INSERT INTO telefone(contato1, contato2, crm)
                                        VALUES(:contato1, :contato2, :crm);"""
                insertHospMed = """INSERT INTO hospitalMedico(cnpj, medico_crm)
                                VALUES(:cnpj, :medico_crm);"""
                insertEspecilidade = """INSERT INTO especialidade(especialidade, medico_crm)
                                    VALUES(:especialidade, :medico_crm);"""
                
                med = medico(crm, cpfMedico, nome, rua, bairro, cidade, cep)
                telMed = telefone(contato1, contato2, crm)
                hospMed = hospitalMedico(cnpj, crm)
                especialidade_ = especialidade(espec, crm)
                cursor.execute(insertMedico, {"crm": med.crm,
                                            "cpfMedico": med.cpfMedico,
                                            "nome": med.nome,
                                            "rua": med.rua,
                                            "bairro": med.bairro,
                                            "cidade": med.cidade,
                                            "cep": med.cep})
                cursor.execute(insertContatoMedico, {"contato1": telMed.contato1,
                                                    "contato2": telMed.contato2,
                                                    "crm": telMed.crm})
                cursor.execute(insertHospMed, {"cnpj": hospMed.cnpj,
                                            "medico_crm": hospMed.crm})
                cursor.execute(insertEspecilidade, {"especialidade": especialidade_.especialidade,
                                                    "medico_crm": especialidade_.crm})
                bancoDados.commit()
                cadastrado()
            except:
                print(f"\n\033[1;31mNÃO FOI POSSÍVEl, CONFIRME O QUE FOI DIGITADO E TENTE NOVAMENTE.\033[m")
        elif opcao == 3:
            try:
                coren = int(input("\033[1;34mCOREM:\033[m "))
                cpfEnfermeira = input("\033[1;34mCPF:\033[m ")
                endereco()
                
                insertEnfermeira = """INSERT INTO enfermeira(coren, cpfEnfermeira, nome, rua, bairro, cidade, cep)
                                    VALUES(:coren, :cpfEnfermeira, :nome, :rua, :bairro, :cidade, :cep);"""
                
                enfermei = enfermeira(coren, cpfEnfermeira, nome, rua, bairro, cidade, cep)
                cursor.execute(insertEnfermeira, {"coren": enfermei.coren,
                                                "cpfEnfermeira": enfermei.cpfEnfermeira,
                                                "nome": enfermei.nome,
                                                "rua": enfermei.rua,
                                                "bairro": enfermei.bairro,
                                                "cidade": enfermei.cidade,
                                                "cep": enfermei.cep})
                
                bancoDados.commit()
                cadastrado()
            except:
                print("\n\033[1;31mNÃO FOI POSSÍVEl, POR FAVOR, FAZER NOVAMENTE.\033[m")
        elif opcao == 4:
            cpfPaciente = int(input("\033[1;34mCPF:\033[m "))
            rg = int(input("\033[1;34mRG:\033[m "))
            endereco()
            nomeTratamento = input("\033[1;34mTRATAMENTO:\033[m ")
            crmMedico = input("\033[1;34mCRM DO MÉDICO:\033[m ")
            insertPaciente = """INSERT INTO paciente(cpfPaciente, rg, nome, rua, bairro, cidade, cep)
                                VALUES(:cpfPaciente, :rg, :nome, :rua, :bairro, :cidade, :cep);"""
            insertTratamento = """INSERT INTO tratamento(nomeTratamento)
                                VALUES(:nomeTratamento)"""
            
            pacien = paciente(cpfPaciente, rg, nome, rua, bairro, cidade, cep)
            cursor.execute(insertPaciente, {"cpfPaciente": pacien.cpfPaciente,
                                            "rg": pacien.rg,
                                            "nome": pacien.nome,
                                            "rua": pacien.rua,
                                            "bairro": pacien.bairro,
                                            "cidade": pacien.cidade,
                                            "cep": pacien.cep})
            tratament = tratamento(nomeTratamento)
            cursor.execute(insertTratamento, {"nomeTratamento": tratament.nomeTratamento})
            bancoDados.commit()
            cadastrado()
        elif opcao == 5: #UPDATE
            cabecalho("ALTERAÇÃO")
            menu(["HOSPITAIS", "MÉDICOS", "ENFERMEIRA", "PACIENTES"])
            opcao = int(input("DIGITE SUA ESCOLHA: "))
            if opcao == 1:
                cabecalho("ALTERAÇÃO")
                menu(["NOME", "RUA", "BAIRRO", "CIDADE", "CEP"])
                opcao = int(input("DIGITE SUA ESCOLHA: "))
                if opcao == 1:
                    alterarNome = input("\033[1;34mNOME:\033[m ")
                    alterarCnpj = int(input("\033[34mCNPJ:\033[m "))
                    update = """UPDATE hospital SET nome= :nome WHERE cnpj= :cnpj;"""
                    cursor.execute(update, {"nome": alterarNome,
                                            "cnpj": alterarCnpj})
                    bancoDados.commit()
                    alterado()
                elif opcao == 2:
                    alterarRua = input("\033[1;34mRUA:\033[m ")
                    alterarCnpj = int(input("\033[34mCNPJ:\033[m "))
                    update = """UPDATE hospital SET rua= :rua WHERE cnpj= :cnpj;"""
                    cursor.execute(update, {"rua": alterarRua,
                                            "cnpj": alterarCnpj})
                    bancoDados.commit()
                    alterado()
                elif opcao == 3:
                    alterarBairro = input("\033[1;34mBAIRRO:\033[m ")
                    alterarCnpj = int(input("\033[34mCNPJ:\033[m "))
                    update = """UPDATE hospital SET bairro= :bairro WHERE cnpj= :cnpj;"""
                    cursor.execute(update, {"bairro": alterarBairro,
                                            "cnpj": alterarCnpj})
                    bancoDados.commit()
                    alterado()
                elif opcao == 4:
                    alterarCidade = input("\033[1;34mCIDADE:\033[m ")
                    alterarCnpj = int(input("\033[34mCNPJ:\033[m "))
                    update = """UPDATE hospital SET cidade= :cidade WHERE cnpj= :cnpj;"""
                    cursor.execute(update, {"cidade": alterarCidade,
                                            "cnpj": alterarCnpj})
                    bancoDados.commit()
                    alterado()
                elif opcao == 5:
                    alterarCep = input("\033[1;34mCEP:\033[m ")
                    alterarCnpj = int(input("\033[34mCNPJ:\033[m "))
                    update = """UPDATE hospital SET cep= :cep WHERE cnpj= :cnpj;"""
                    cursor.execute(update, {"cep": alterarCep,
                                            "cnpj": alterarCnpj})
                    bancoDados.commit()
                    alterado()
                else:
                    print("\n\033[31mERRO! OPÇÃO INVÁLIDA...\033[m\n")
                    linha()
            elif opcao == 2:
                cabecalho("ALTERAÇÃO")
                menu(["NOME", "RUA", "BAIRRO", "CIDADE", "CEP"])
                opcao = int(input("DIGITE SUA ESCOLHA: "))
                if opcao == 1:
                    alterarNome = input("\033[1;34mNOME:\033[m ")
                    alterarCrm = int(input("\033[34mCRM:\033[m "))
                    update = """UPDATE medico SET nome= :nome WHERE crm= :crm;"""
                    cursor.execute(update, {"nome": alterarNome,
                                            "crm": alterarCrm})
                    bancoDados.commit()
                    alterado()
                elif opcao == 2:
                    alterarRua = input("\033[1;34mRUA:\033[m ")
                    alterarCrm = int(input("\033[34mCRM:\033[m "))
                    update = """UPDATE medico SET rua= :rua WHERE crm= :crm;"""
                    cursor.execute(update, {"rua": alterarRua,
                                            "crm": alterarCrm})
                    bancoDados.commit()
                    alterado()
                elif opcao == 3:
                    alterarBairro = input("\033[1;34mBAIRRO:\033[m ")
                    alterarCrm = int(input("\033[34mCRM:\033[m "))
                    update = """UPDATE medico SET bairro= :bairro WHERE crm= :crm;"""
                    cursor.execute(update, {"bairro": alterarBairro,
                                            "crm": alterarCrm})
                    bancoDados.commit()
                    alterado()
                elif opcao == 4:
                    alterarCidade = input("\033[1;34mCIDADE:\033[m ")
                    alterarCrm = int(input("\033[34mCRM:\033[m "))
                    update = """UPDATE medico SET cidade= :cidade WHERE crm= :crm;"""
                    cursor.execute(update, {"cidade": alterarCidade,
                                            "crm": alterarCrm})
                    bancoDados.commit()
                    alterado()
                elif opcao == 5:
                    alterarCep = input("\033[1;34mCEP:\033[m ")
                    alterarCrm = int(input("\033[34mCRM:\033[m "))
                    update = """UPDATE medico SET cep= :cep WHERE crm= :crm;"""
                    cursor.execute(update, {"cep": alterarCep,
                                            "crm": alterarCrm})
                    bancoDados.commit()
                    alterado()
                else:
                    print("\n\033[31mERRO! OPÇÃO INVÁLIDA...\033[m\n")
                    linha()
            elif opcao == 3:
                cabecalho("ALTERAÇÃO")
                menu(["NOME", "RUA", "BAIRRO", "CIDADE", "CEP"])
                opcao = int(input("DIGITE SUA ESCOLHA: "))
                if opcao == 1:
                    alterarNome = input("\033[1;34mNOME:\033[m ")
                    alterarCoren = int(input("\033[34mCOREN:\033[m "))
                    update = """UPDATE enfermeira SET nome= :nome WHERE coren= :coren;"""
                    cursor.execute(update, {"nome": alterarNome,
                                            "coren": alterarCoren})
                    bancoDados.commit()
                    alterado()
                elif opcao == 2:
                    alterarRua = input("\033[1;34mRUA:\033[m ")
                    alterarCoren = int(input("\033[34mCOREN:\033[m "))
                    update = """UPDATE enfermeira SET rua= :rua WHERE coren= :coren;"""
                    cursor.execute(update, {"rua": alterarRua,
                                            "coren": alterarCoren})
                    bancoDados.commit()
                    alterado()
                elif opcao == 3:
                    alterarBairro = input("\033[1;34mBAIRRO:\033[m ")
                    alterarCoren = int(input("\033[34mCOREN:\033[m "))
                    update = """UPDATE enfermeira SET bairro= :bairro WHERE coren= :coren;"""
                    cursor.execute(update, {"bairro": alterarBairro,
                                            "coren": alterarCoren})
                    bancoDados.commit()
                    alterado()
                elif opcao == 4:
                    alterarCidade = input("\033[1;34mCIDADE:\033[m ")
                    alterarCoren = int(input("\033[34mCOREN:\033[m "))
                    update = """UPDATE enfermeira SET cidade= :cidade WHERE coren= :coren;"""
                    cursor.execute(update, {"cidade": alterarCidade,
                                            "coren": alterarCoren})
                    bancoDados.commit()
                    alterado()
                elif opcao == 5:
                    alterarCep = input("\033[1;34mCEP:\033[m ")
                    alterarCoren = int(input("\033[34mCOREN:\033[m "))
                    update = """UPDATE enfermeira SET cep= :cep WHERE coren= :coren;"""
                    cursor.execute(update, {"cep": alterarCep,
                                            "coren": alterarCoren})
                    bancoDados.commit()
                    alterado()
                else:
                    print("\n\033[31mERRO! OPÇÃO INVÁLIDA...\033[m\n")
                    linha()   
            elif opcao == 4: 
                cabecalho("ALTERAÇÃO")
                menu(["NOME", "RUA", "BAIRRO", "CIDADE", "CEP"])
                opcao = int(input("DIGITE SUA ESCOLHA: "))
                if opcao == 1:
                    alterarNome = input("\033[1;34mNOME:\033[m ")
                    alterarCpf = int(input("\033[34mCPF:\033[m "))
                    update = """UPDATE paciente SET nome= :nome WHERE cpfPaciente= :cpfPaciente;"""
                    cursor.execute(update, {"nome": alterarNome,
                                            "cpfPaciente": alterarCpf})
                    bancoDados.commit()
                    alterado()
                elif opcao == 2:
                    alterarRua = input("\033[1;34mRUA:\033[m ")
                    alterarCpf = int(input("\033[34mCPF:\033[m "))
                    update = """UPDATE paciente SET rua= :rua WHERE cpfPaciente= :cpfPaciente;"""
                    cursor.execute(update, {"rua": alterarRua,
                                            "cpfPaciente": alterarCpf})
                    bancoDados.commit()
                    alterado()
                elif opcao == 3:
                    alterarBairro = input("\033[1;34mBAIRRO:\033[m ")
                    alterarCpf = int(input("\033[34mCPF:\033[m "))
                    update = """UPDATE paciente SET bairro= :bairro WHERE cpfPaciente= :cpfPaciente;"""
                    cursor.execute(update, {"bairro": alterarBairro,
                                            "cpfPaciente": alterarCpf})
                    bancoDados.commit()
                    alterado()
                elif opcao == 4:
                    alterarCidade = input("\033[1;34mCIDADE:\033[m ")
                    alterarCpf = int(input("\033[34mCPF:\033[m "))
                    update = """UPDATE paciente SET cidade= :cidade WHERE cpfPaciente= :cpfPaciente;"""
                    cursor.execute(update, {"cidade": alterarCidade,
                                            "cpfPaciente": alterarCpf})
                    bancoDados.commit()
                    alterado()
                elif opcao == 5:
                    alterarCep = input("\033[1;34mCEP:\033[m ")
                    alterarCpf = int(input("\033[34mCPF:\033[m "))
                    update = """UPDATE paciente SET cep= :cep WHERE cpfPaciente= :cpfPaciente;"""
                    cursor.execute(update, {"cep": alterarCep,
                                            "cpfPaciente": alterarCpf})
                    bancoDados.commit()
                    alterado()
                else:
                    print("\n\033[31mERRO! OPÇÃO INVÁLIDA...\033[m\n")
                    linha()
            else:
                print("\n\033[31mERRO! OPÇÃO INVÁLIDA...\033[m\n")
                linha()
        elif opcao == 6: #DELETE
            cabecalho("DELETAR")
            menu(["HOSPITAL", "HOISPITAL/MEDICO", "MEDICO", "ESPECIALIDADE", "TELEFONE", "ENFERMEIRA", "PACIENTE"])
            opcao = int(input("DIGITE SUA ESCOLHA: "))
            if opcao == 1: #hospital
                try:
                    deleteCnpj = int(input("CNPJ PARA EXCLUIR: "))
                    deleteHospital = """DELETE FROM hospital WHERE cnpj= :cnpj;"""
                    cursor.execute(deleteHospital, {"cnpj": deleteCnpj})
                    bancoDados.commit()
                    print("\n\033[1;32mDELETADO COM SUCESSO!\033[m")
                    
                    linha()
                except bancoDados.IntegrityError as erro:
                    print(f"\n\033[31mNÃO FOI POSSÍVEL EXCLUIR, EXISTE UMA TABELA VINCULADA. TABELA HOSPITAL/MEDICO ERRO {erro}.\033[m")
            elif opcao == 2: #hospital/medico
                deleteId = int(input("ID: "))
                deleteHospitalMedico = """DELETE FROM hospitalMedico WHERE idHospMed= :idHospMed;"""
                cursor.execute(deleteHospitalMedico, {"idHospMed": deleteId})
                bancoDados.commit()
                print("\n\033[1;32mDELETADO COM SUCESSO!\033[m")
                print("\n\033[1;32mAGORA SERÁ POSSÍVEL DELETAR O HOSPITAL\033[m")
                linha()
            elif opcao == 3: #medico
                try:
                    deleteCrm = int(input("CRM: "))
                    deleteMedico = """DELETE FROM medico WHERE crm= :crm;"""
                    cursor.execute(deleteMedico, {"crm": deleteCrm})
                    bancoDados.commit()
                    print("\n\033[1;32mDELETADO COM SUCESSO!\033[m")
                    linha()
                except bancoDados.IntegrityError as erro:
                    print(f"\n\033[31mNÃO FOI POSSÍVEL EXCLUIR, EXISTE UMA TABELA VINCULADA. TABELA HOSPITAL/MEDICO, ESPECIALIDADE, TELEFONE. DELETE TODAS ANTES DE TENTAR NOVAMENTE. ERRO {erro}.\033[m")
            elif opcao == 4: #especialidade
                deleteId = int(input("ID: "))
                deleteEspecialidade = """DELETE FROM especialidade WHERE idEspecialidade= :idEspecialidade;"""
                cursor.execute(deleteEspecialidade, {"idEspecialidade": deleteId})
                bancoDados.commit()
                print("\n\033[1;32mDELETADO COM SUCESSO!\033[m")
                linha()
            elif opcao == 5: #telefone
                deleteId = int(input("COD: "))
                deleteCod_tel = """DELETE FROM telefone WHERE cod_tel= :cod_tel;"""
                cursor.execute(deleteCod_tel, {"cod_tel": deleteId})
                bancoDados.commit()
                print("\n\033[1;32mDELETADO COM SUCESSO!\033[m")
                linha()
            elif opcao == 6: #enfermeira
                deleteCoren = int(input("COREN: "))
                deleteEnfermeira = """DELETE FROM enfermeira WHERE coren= :coren;"""
                cursor.execute(deleteEnfermeira, {"coren": deleteCoren})
                bancoDados.commit()
                print("\n\033[1;32mDELETADO COM SUCESSO!\033[m")
                linha()
            elif opcao == 7: #paciente
                deleteCpf = int(input("CPF: "))
                deletePaciente = """DELETE FROM paciente WHERE cpfPaciente= :cpfPaciente;"""
                cursor.execute(deletePaciente, {"cpfPaciente": deleteCpf})
                bancoDados.commit()
                print("\n\033[1;32mDELETADO COM SUCESSO!\033[m")
                linha()
        elif opcao == 7: #SELECT
            cabecalho("RELATÓRIOS")
            menu(["HOSPITAIS", "MÉDICOS", "PACIENTES", "TRATAMENTO"])
            opcao = int(input("DIGITE SUA ESCOLHA: "))
            if opcao == 1:
                cabecalho("RELATÓRIOS")
                relatorioHospitais = """SELECT * FROM hospital"""
                cursor.execute(relatorioHospitais)
                
                listaHospital = cursor.fetchall()
                if len(listaHospital) == 0:
                    listaVazia()
                for lista in listaHospital:
                    print(f"CNPJ: {lista[0]} \nNOME: {lista[1]} \nRUA: {lista[2]} \nBAIRRO: {lista[3]} \nCIDADE: {lista[4]} \nCEP: {lista[5]}")
                    linha()

            elif opcao == 2: #listar médicos, seus telefones e especialidade.
                cabecalho("RELATÓRIOS")
                relatorioMedico = """SELECT * FROM medico md
                                    LEFT JOIN telefone tl
                                    ON (md.crm = tl.crm)
                                    LEFT JOIN especialidade es
                                    ON (md.crm = medico_crm)"""
                cursor.execute(relatorioMedico)

                listaMedico = cursor.fetchall()
                
                if len(listaMedico) == 0:
                    listaVazia()
                for lista in listaMedico:
                    print(f"CRM: {lista[0]} \nCPF: {lista[1]} \nNOME: {lista[2]}  \nCONTATO 1: {lista[9]} \nCONTATO 2: {lista[10]} \nESPECIALIDADE: {lista[12]}")
                    linha()
            elif opcao == 3:
                cabecalho("RELATÓRIO")
                relatorioPaciente = """SELECT * FROM paciente"""
                cursor.execute(relatorioPaciente)
                listaPaciente = cursor.fetchall()
                
                if len(listaPaciente) == 0:
                    listaVazia()
                for lista in listaPaciente:
                    print(f"CPF: {lista[0]} \nRG: {lista[1]} \nNOME: {lista[2]} \nRUA: {lista[3]} \nBAIRRO: {lista[4]} \nCIDADE: {lista[5]} \nCEP: {lista[6]}")
                    linha()
            elif opcao == 4:
                cabecalho("RELATÓRIO")
                relatorioPacienteTratamento = """SELECT * FROM tratamento"""
                cursor.execute(relatorioPacienteTratamento)
                listaPacienteTratamento = cursor.fetchall()
                
                if len(listaPacienteTratamento) == 0:
                    listaVazia()
                for lista in listaPacienteTratamento:
                    print(f"CÓDIGO: {lista[0]} \nTRATAMENTO: {lista[1]}")
                    linha()
        elif opcao == 8:
            print("\n\033[1;31mSISTEMA ESTÁ SENDO ENCERRADO... ATÉ MAIS!\033[m\n")
            linha()
            break
        else:
            print("\n\033[31mERRO! OPÇÃO INVÁLIDA...\033[m\n")
            linha()
    except ValueError as erro:
        print(f"\n\033[31mVERIFIQUE O QUE FOI DIGITADO, ERRO: {erro}...\033[m")
    
    sair = input("\nDESEJA SAIR? (S)SIM OU (N)NÃO: ").upper()
    if sair == 'S':
        print("\n\033[1;31mSISTEMA ESTÁ SENDO ENCERRADO... ATÉ MAIS!\033[m\n")
        break
    else: 
        cabecalho("CADASTRO")
        menu(["HOSPITAL", "MÉDICO", "ENFERMEIRA", "PACIENTE", "ALTERAR", "\033[31mDELETAR\033[m", "\033[35mRELATÓRIO\033[m", "SAIR"])

cursor.close()
bancoDados.close()