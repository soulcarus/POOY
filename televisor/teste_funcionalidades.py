from funcionalidades import *

tv = Televisor("Sony",'SONY-123')

controle = ControleRemoto(tv)

controle.sintonizarCanal('SBT')
controle.trocarCanal('SBT')

controle.aumentarVolume()
controle.diminuirVolume()

print(tv.canal_atual)
print(tv.volume)