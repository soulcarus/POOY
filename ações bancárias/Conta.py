class Conta:
    def __init__(self,titular,numero, saldo):
        self.saldo = saldo
        self.numero = numero
        self.titular = titular

    #vamos fazer o saldo não poder ser negativo

    #alterar a classe Conta utilizando Property
    
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter   
    def set_saldo(self,saldo):
        if (saldo<0):
            print("O saldo não pode ser negativo")
        else:
            self._saldo = saldo
    
    #adicionar método de saque na conta

    def saque(self,valor):
        if (self.saldo >= valor):
            self.saldo -= valor
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente!")
    
    #adicionar método deposita

    def deposita(self,valor):
        self.valor += valor

    def extrato(self):
        print(f"Cliente: {self._titular}, Saldo: {self._saldo}")