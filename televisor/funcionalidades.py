class Televisor:

    def __init__(self, fab, modelo):
        
        self.fabricante = fab
        self.modelo = modelo
        self.canal_atual = None
        self.lista_de_canais = []
        self.volume = 20

    def aumentarVolume(self,valor):

        if self.volume + valor <= 100:
            self.volume += valor
        else:
            self.volume = 100
    
    def diminuirVolume(self,valor):

        if self.volume - valor >= 0:
            self.volume -= valor
        else:
            self.volume = 0

    def trocarCanal(self,canal):

        if canal in self.lista_de_canais:
            self.canal_atual = canal
    
    def sintonizarCanal(self,canal):

        if canal not in self.lista_de_canais:
            self.lista_de_canais.append(canal)

class ControleRemoto:


    def __init__(self,tv):


        self.tv = tv


    def aumentarVolume(self):

        self.tv.aumentarVolume(20)
    

    def diminuirVolume(self):

        self.tv.diminuirVolume(20)
    

    def trocarCanal(self,canal):

        self.tv.trocarCanal(canal)
    

    def sintonizarCanal(self,canal):

        self.tv.sintonizarCanal(canal)

