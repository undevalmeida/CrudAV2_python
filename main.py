import sqlite3 as bancoDados
from modelo import *

bancoDados = bancoDados.connect("bancoDados.db")
bancoDados.execute("PRAGMA foreign_keys = ON")
cursor = bancoDados.cursor()

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
menu(["HOSPITAL", "MÉDICO", "ENFERMEIRA", "PACIENTE","\033[35mRELATÓRIO\033[m", "SAIR"])


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

while True:
    try:
        opcao = int(input("DIGITE SUA ESCOLHA: "))
        if opcao == 1:
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
                especialidade = input("\033[1;34mESPECIALIDADE:\033[m ")
                endereco()
                contato1 = input("\033[1;34mCONTATO 1:\033[m ")
                contato2 = input("\033[1;34mCONTATO 2:\033[m ")
                insertMedico = """INSERT INTO medico(crm, cpfMedico, especialidade, nome, rua, bairro, cidade, cep)
                                VALUES(:crm, :cpfMedico, :especialidade, :nome, :rua, :bairro, :cidade, :cep);"""
                insertContatoMedico = """INSERT INTO telefone(contato1, contato2, crm)
                                        VALUES(:contato1, :contato2, :crm);"""
                telMed = telefone(contato1, contato2, crm)
                med = medico(crm, cpfMedico, especialidade, nome, rua, bairro, cidade, cep)
                cursor.execute(insertMedico, {"crm": med.crm,
                                            "cpfMedico": med.cpfMedico,
                                            "especialidade": med.especialidade,
                                            "nome": med.nome,
                                            "rua": med.rua,
                                            "bairro": med.bairro,
                                            "cidade": med.cidade,
                                            "cep": med.cep})
                cursor.execute(insertContatoMedico, {"contato1": telMed.contato1,
                                                    "contato2": telMed.contato2,
                                                    "crm": telMed.crm})
                bancoDados.commit()
                cadastrado()
            except:
                print("\n\033[1;31mNÃO FOI POSSÍVEl, POR FAVOR, FAZER NOVAMENTE.\033[m")
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

            insertPaciente = """INSERT INTO paciente(cpfPaciente, rg, nome, rua, bairro, cidade, cep)
                                VALUES(:cpfPaciente, :rg, :nome, :rua, :bairro, :cidade, :cep);"""

            pacien = paciente(cpfPaciente, rg, nome, rua, bairro, cidade, cep)
            cursor.execute(insertPaciente, {"cpfPaciente": pacien.cpfPaciente,
                                            "rg": pacien.rg,
                                            "nome": pacien.nome,
                                            "rua": pacien.rua,
                                            "bairro": pacien.bairro,
                                            "cidade": pacien.cidade,
                                            "cep": pacien.cep})
            
            bancoDados.commit()
            cadastrado()

        elif opcao == 5:
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

            elif opcao == 2: #listar médicos e seus telefones
                cabecalho("RELATÓRIOS")
                relatorioMedico = """SELECT * FROM medico md
                                    LEFT JOIN telefone tl
                                    ON (md.crm = tl.crm)"""
                cursor.execute(relatorioMedico)

                listaMedico = cursor.fetchall()
                
                if len(listaMedico) == 0:
                    listaVazia()
                for lista in listaMedico:
                    print(f"CRM: {lista[0]} \nCPF: {lista[1]} \nNOME: {lista[2]} \nCONTATO 1: {lista[9]} \nCONTATO 2: {lista[10]}")
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
                    print(f"CÓDIGO: {lista[0]} \nTRATAMENTO: {lista[1]} \nCRM DO MEDICO: {lista[2]}")
                    linha()

        elif opcao == 6:
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
        menu(["HOSPITAL", "MÉDICO", "ENFERMEIRA", "PACIENTE", "\033[35mRELATÓRIO\033[m", "SAIR"])

# cursor.close()
# bancoDados.close()