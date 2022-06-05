class hospital:
    def __init__(self, cnpj, nome, rua, bairro, cidade, cep):
        self.cnpj = cnpj
        self.nome = nome
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.cep = cep
class medico:
    def __init__(self, crm, cpfMedico, especialidade, nome, rua, bairro, cidade, cep):
        self.crm = crm
        self.cpfMedico = cpfMedico
        self.especialidade = especialidade
        self.nome = nome
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.cep = cep
class telefone:
    def __init__(self, contato1, contato2, crm):
        self.contato1 = contato1
        self.contato2 = contato2
        self.crm = crm
class enfermeira:
    def __init__(self, coren, cpfEnfermeira, nome, rua, bairro, cidade, cep):
        self.coren = coren
        self.cpfEnfermeira = cpfEnfermeira
        self.nome = nome
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.cep = cep
class paciente:
    def __init__(self, cpfPaciente, rg, nome, rua, bairro, cidade, cep):
        self.cpfPaciente = cpfPaciente
        self.rg = rg
        self.nome = nome
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.cep = cep
class tratamento:
    def __init__(self, nomeTratamento, crmMedico):
        self.nomeTratamento = nomeTratamento
        self.crmMedico = crmMedico
class hospitalMedico:
    def __init__(self, cnpj, crm):
        self.cnpj = cnpj
        self.crm = crm
