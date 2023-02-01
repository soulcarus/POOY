class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def identificacao(self):
        return self.__cpf


class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, cpf,  codigo):
        super().__init__(nome,sobrenome,cpf)
        self.__codigo = codigo
    
    def identificacao(self):
        return self.__codigo
    

class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def identificacao(self):
        return self.__matricula

cliente1 = Cliente('Jose','Silva','123.456.789-90','xxxx-09')
funcionario1 = Funcionario('Pedro','Souza','234.444.555-99','3456.90')

print(cliente1.nome_completo())
print(cliente1.identificacao())

print('----------')

print(funcionario1.nome_completo())
print(funcionario1.identificacao())