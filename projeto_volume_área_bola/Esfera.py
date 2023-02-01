import math

class Esfera:

    def __init__(self,cor,raio):
        
        self.cor = cor
        self.raio = raio
    
    def volume(self):

        vol = (4/3)*math.pi*(self.raio**3) #volume é igual a divisão de 4 por 3
        #multiplicado por pi, que multiplica o raio da esfera elevado à 3
        return vol

    def area(self):

        ar = 4*math.pi*(self.raio**2)
        return ar

bola1 = Esfera('vermelha', 4)
bola1 = Esfera('azul', 7)

print(f'O volume da bola 1 é {bola1.volume()}cm³')
print(f'A área superficial da bola 1 é {bola1.area()}cm²')

print(bola1.volume())
print(Esfera.volume(bola1))