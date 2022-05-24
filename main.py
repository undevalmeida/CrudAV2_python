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
    linha()

menu(["HOSPITAL", "MÉDICO", "ENFERMEIRA","RELATÓRIO", "SAIR"])

# INTERAÇÃO COM USUÁRIO PARA CADASTRO DE HOSPITAL
linha()

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
        elif opcao == 2:
            crm = int(input("\033[1;34mCRM:\033[m "))
            cpfMedico = int(input("\033[1;34mCPF:\033[m "))
            endereco()
        elif opcao == 3:
            coren = int(input("\033[1;34mCOREM:\033[m "))
            cpfEnfermeira = input("\033[1;34mCPF:\033[m ")
            endereco()
        elif opcao == 4:
            cabecalho("RELATÓRIO")
            menu(["HOSPITAIS", "MÉDICOS", "PACIENTES"])
            opcao = int(input("DIGITE SUA ESCOLHA: "))
            if opcao == 1:
                menu(["TRATAMENTOS", "PACIENTES", "MÉDICOS", "ENFERMEIRAS"])
            elif opcao == 2:
                menu(["TELEFONE", "ESPECIALIDADE"])
            elif opcao == 3:
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
        menu(["HOSPITAL", "MÉDICO", "ENFERMEIRA", "RELATÓRIO", "SAIR"])