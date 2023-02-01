from Conta import Conta
from Cliente import Cliente

class Main:
    pass

c1 = Cliente("João",'(85) 98936-5813')

conta = Conta(c1.nome,6565,200)

print("Nome do Cliente:",c1.nome, "Numero do Cliente:",c1.telefone)

conta.deposita(100)
conta.saque(50)
conta.extrato()
