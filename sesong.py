from kamp import Partido
from tabell import TablaClasificacion
from lagliste import listaEquipos

class Sesong:
    def __init__(self, listaEquipos):
        self.listaEquipos = listaEquipos
        self.rondas = []
        self.tablaClasificacion = TablaClasificacion(self.listaEquipos)
        
    def getTablaClasificacion(self):
        return self.tablaClasificacion.getClasificacion()

    def simuler(self):
        nrondas = (len(self.listaEquipos) - 1) * 2
        nPartidos = len(self.listaEquipos) // 2

        equipos_local = self.listaEquipos[:nPartidos]
        equipos_visitanteAux = self.listaEquipos[nPartidos:]
        equipos_visitante = []
        for i in equipos_visitanteAux:
            equipos_visitante.append(i)
        equipos_visitante.reverse()

        for ronda in range(nrondas):
            rondasunde = []

            for i in range(nPartidos):
                equipo_local = equipos_local[i]
                equipo_visitante = equipos_visitante[i]

                if equipo_local is None or equipo_visitante is None:
                    continue

                partido = Partido(equipo_local, equipo_visitante)
                rondasunde.append(partido)
                self.tablaClasificacion.agregarResultadoPartido(partido)

            aux =equipos_local[-1]
            equipos_local = [equipos_local[0]] + [equipos_visitante[0]] + equipos_local[1:-1]
            equipos_visitante = [equipos_visitante[1]] + equipos_visitante[2:] + [aux]

            self.rondas.append(rondasunde)

            clasificacion_actual = self.getTablaClasificacion()
            yield clasificacion_actual

    def imprimirRondas(self):
        for i, ronda in enumerate(self.rondas):
            print(f"ronda {i+1}\n{'-'*8}")
            for partido in ronda:
                print(f"{partido.equipoLocal} - {partido.equipoVisitante} ({partido.getGolLocal()} - {partido.getGolVisitante()})")
            print()