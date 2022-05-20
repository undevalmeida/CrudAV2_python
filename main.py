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
        print(f"{cont} - \033[1;33m{item}\033[m", end="")
        print("\n")
        cont += 1

menu(["HOSPITAL", "MÉDICO", "PACIENTE"])

# INTERAÇÃO COM USUÁRIO PARA CADASTRO DE HOSPITAL
linha()

opcao = int(input("DIGITE SUA ESCOLHA: "))

if opcao == 1:
    cnpj = int(input("\033[1;33mNÚMERO DO CNPJ:\033[m] "))
    nome = input("NOME DO HOSPITAL: ")
    rua = input("RUA: ")
    bairro = input("BAIRRO: ")
    cidade = input("CIDADE: ")
    cep = input("CEP: ")

