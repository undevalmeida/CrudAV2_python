import sqlite3 as bancoDados
from modelo import hospital, medico, enfermeira


bancoDados = bancoDados.connect("bancoDados.db")
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
menu(["HOSPITAL", "MÉDICO", "ENFERMEIRA","RELATÓRIO", "SAIR"])

# INTERAÇÃO COM USUÁRIO PARA CADASTRO DE HOSPITAL

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

while True:
    try:
        opcao = int(input("DIGITE SUA ESCOLHA: "))
        if opcao == 1:
            cnpj = int(input("\033[1;34mNÚMERO DO CNPJ:\033[m "))
            endereco()

            insertHospital = """INSERT INTO hospital(cnpj, nome, rua, bairro, cidade, cep)
                                VALUES(:cnpj, :nome, :rua, :bairro, :cidade, :cep);"""
            
            hospital = hospital(cnpj, nome, rua, bairro, cidade, cep)
            cursor.execute(insertHospital, {"cnpj": hospital.cnpj,
                                            "nome": hospital.nome,
                                            "rua": hospital.rua,
                                            "bairro": hospital.bairro,
                                            "cidade": hospital.cidade,
                                            "cep": hospital.cep})
            bancoDados.commit()
            print("\n\033[32mCADASTRADO COM SUCESSO!\033[m")
                                
        elif opcao == 2:
            crm = int(input("\033[1;34mCRM:\033[m "))
            cpfMedico = int(input("\033[1;34mCPF:\033[m "))
            especialidade = input("\033[1;34mESPECIALIDADE:\033[m ")
            endereco()
            insertMedico = """INSERT INTO medico(crm, cpfMedico, especialidade, nome, rua, bairro, cidade, cep)
                            VALUES(:crm, :cpfMedico, :especialidade, :nome, :rua, :bairro, :cidade, :cep);"""
            
            medico = medico(crm, cpfMedico, especialidade, nome, rua, bairro, cidade, cep)
            cursor.execute(insertMedico, {"crm": medico.crm,
                                        "cpfMedico": medico.cpfMedico,
                                        "especialidade": medico.especialidade,
                                        "nome": medico.nome,
                                        "rua": medico.rua,
                                        "bairro": medico.bairro,
                                        "cidade": medico.cidade,
                                        "cep": medico.cep})
            bancoDados.commit()
            print("\n\033[32mCADASTRADO COM SUCESSO!\033[m")
        elif opcao == 3:
            coren = int(input("\033[1;34mCOREM:\033[m "))
            cpfEnfermeira = input("\033[1;34mCPF:\033[m ")
            endereco()
            
            insertEnfermeira = """INSERT INTO enfermeira(coren, cpfEnfermeira, nome, rua, bairro, cidade, cep)
                                VALUES(:coren, :cpfEnfermeira, :nome, :rua, :bairro, :cidade, :cep);"""
            
            enfermeira = enfermeira(coren, cpfEnfermeira, nome, rua, bairro, cidade, cep)
            cursor.execute(insertEnfermeira, {"coren": enfermeira.coren,
                                            "cpfEnfermeira": enfermeira.cpfEnfermeira,
                                            "nome": enfermeira.nome,
                                            "rua": enfermeira.rua,
                                            "bairro": enfermeira.bairro,
                                            "cidade": enfermeira.cidade,
                                            "cep": enfermeira.cep})
            
            bancoDados.commit()
            print("\n\033[32mCADASTRADO COM SUCESSO!\033[m")
        elif opcao == 4:
            cabecalho("RELATÓRIOS")
            menu(["HOSPITAIS", "MÉDICOS", "PACIENTES", "TRATAMENTO"])
            opcao = int(input("DIGITE SUA ESCOLHA: "))
            if opcao == 1:
                cabecalho("RELATÓRIOS")
                relatorioHospitais = """SELECT * FROM hospital"""
                cursor.execute(relatorioHospitais)
                
                listaHospital = cursor.fetchall()
                for lista in listaHospital:
                    print(f"CNPJ: {lista[0]} \nNOME: {lista[1]} \nRUA: {lista[2]} \nBAIRRO: {lista[3]} \nCIDADE: {lista[4]} \nCEP: {lista[5]}")
                    linha()

            elif opcao == 2: #listar médicos e seus telefones
                cabecalho("RELATÓRIOS")

            elif opcao == 3:
                cabecalho("RELATÓRIO")
                print("A FAZER...")

        elif opcao == 5:
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
        menu(["HOSPITAL", "MÉDICO", "ENFERMEIRA", "RELATÓRIO", "SAIR"])

cursor.close()
bancoDados.close()