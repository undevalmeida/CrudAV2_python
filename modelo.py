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
class enfermeira:
    def __init__(self, coren, cpfEnfermeira, nome, rua, bairro, cidade, cep):
        self.coren = coren
        self.cpfEnfermeira = cpfEnfermeira
        self.nome = nome
        self.rua = rua
        self.bairro = bairro
        self.cidade = cidade
        self.cep = cep