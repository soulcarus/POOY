from Funcionarios import Funcionario

funcionario = Funcionario('Joao Icaro', 'joaoicaromoreira@gmail.com')

funcionario.cadastro_hora('Jan', 300)
funcionario.cadastro_hora('Fev', 200)
funcionario.cadastro_salario_hora('Jan', 30)
funcionario.cadastro_salario_hora('Fev', 30)
print(funcionario)
print(funcionario.calcular_salario('Jan'))
print(funcionario.calcular_salario('Fev'))