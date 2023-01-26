class Cliente:
    def __init__(self,nome,fone):

        self.nome = nome
        self.telefone = fone

    #metodo get -> lê valores internos e os envia no retorno de uma função
    def get_nome(self):
        return self._nome

    #metodo set -> recebem argumentos que serão atribuídos a membros internos do projeto
    def set_nome(self, nome):
        self._nome = nome