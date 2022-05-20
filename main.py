def linha(tam=42):
    print("_" * tam, end="")
    print("\n")

def cabecalho(txt):
    linha()
    print(txt.center(42))
    linha()

def menu(listOpcoes):
    cabecalho("CADASTRO")
    cont = 1
    for item in listOpcoes:
        print(f"{cont} - \033[1;34m{item}\033[m", end="")
        print("\n")
        cont += 1

menu(["HOSPITAL", "MÉDICO", "PACIENTE"])

# INTERAÇÃO COM USUÁRIO PARA CADASTRO DE HOSPITAL
linha()

opcao = int(input("DIGITE SUA ESCOLHA: "))

if opcao == 1:
    cnpj = int(input("\033[1;34mNÚMERO DO CNPJ:\033[m "))
    nomeHospital = input("\033[1;34mNOME DO HOSPITAL:\033[m ")
    ruaHospital = input("\033[1;34mRUA:\033[m ")
    bairroHospital = input("\033[1;34mBAIRRO:\033[m ")
    cidadeHospital = input("\033[1;34mCIDADE:\033[m ")
    cepHospital = input("\033[1;34mCEP:\033[m ")
elif opcao == 2:
    crm = int(input("CRM: "))
    cpfMedico = int(input("CPF: "))
    nomeMedico = input("NOME: ")
    ruaMedico = input("RUA: ")
    bairroMedico = input("BAIRRO: ")
    cidadeMedico = input("CIDADE: ")
    cepMedico = input("CEP: ")

