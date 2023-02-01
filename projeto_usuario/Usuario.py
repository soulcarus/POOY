from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:

    def __init__(self,nome,sobrenome,email,senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha,rounds=1000,salt_size=10)
    
    def nome_completo(self):
        return f'Nome completo: {self.__nome}{self.__sobrenome}'
    
    def checar_senha(self,senha):
        if cryp.verify(senha,self.__senha):
            return True
        else:
            return False

while True:
    nome = input('Nome: ')
    sobrenome = input('Sobrenome: ')
    email = input('Email: ')
    senha = input('Senha: ')
    conf_senha = input('Conf Senha: ')

    if senha == conf_senha:
        user = Usuario(nome,sobrenome,email,senha)
        break
    else:
        print('As senhas nao conferem!')

print("Usuario criado com sucesso!")

senha = input('Informe a senha para acesso: ')

if user.checar_senha(senha):
    print("Acesso garantido!")
else:
    print("Acesso Negado!")