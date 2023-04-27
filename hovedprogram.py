from sesong import Sesong
from lagliste import listaEquipos
from statistikk import Statistikk

antall_simuleringer = 5   
statistikk = Statistikk(listaEquipos)
season = Sesong(listaEquipos)

for i in range(antall_simuleringer):

    clasificacion_final = list(season.simuler())[-1]
    statistikk.guardarPoscicion(clasificacion_final)

print(statistikk.print_posciciones())