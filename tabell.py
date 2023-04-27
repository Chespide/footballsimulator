from kamp import Partido

class TablaClasificacion:
    def __init__(self, listaEquipos):
        self.listaEquipos = listaEquipos
        self.tablaClasificacion = {}
        
        for lag in self.listaEquipos:
            self.tablaClasificacion[lag] = {}
            self.tablaClasificacion[lag]["nombre"] = lag.getNombre()
            self.tablaClasificacion[lag]["partidosJugados"] = 0
            self.tablaClasificacion[lag]["ganado"] = 0
            self.tablaClasificacion[lag]["empatado"] = 0
            self.tablaClasificacion[lag]["perdido"] = 0
            self.tablaClasificacion[lag]["golesAfavor"] = 0
            self.tablaClasificacion[lag]["golesEnContra"] = 0
            self.tablaClasificacion[lag]["puntos"] = 0
            
        self.clasificacion = sorted(self.listaEquipos)

    # Este método agrega el resultado de un partido a la tablaClasificación
    def agregarResultadoPartido(self, resultadoPartido):
        equipoLocal = resultadoPartido.getEquipoLocal()
        equipoVisitante = resultadoPartido.getEquipoVisitante()
        golLocal = resultadoPartido.getGolLocal()
        golVisitante = resultadoPartido.getGolVisitante()

        self.tablaClasificacion[equipoLocal]["partidosJugados"] += 1
        self.tablaClasificacion[equipoVisitante]["partidosJugados"] += 1
        # oppdater antall ganado/empatado/perdido
        if golLocal > golVisitante:      # equipoLocalet vant
            self.tablaClasificacion[equipoLocal]["ganado"] += 1
            self.tablaClasificacion[equipoVisitante]["perdido"] += 1
        elif golLocal == golVisitante:   # empatado
            self.tablaClasificacion[equipoLocal]["empatado"] += 1
            self.tablaClasificacion[equipoVisitante]["empatado"] += 1
        else:                           # equipoVisitanteet vant
            self.tablaClasificacion[equipoLocal]["perdido"] += 1
            self.tablaClasificacion[equipoVisitante]["ganado"] += 1
        # oppdater golesAfavor begge lag
        self.tablaClasificacion[equipoLocal]["golesAfavor"] += golLocal
        self.tablaClasificacion[equipoVisitante]["golesAfavor"] += golVisitante
        # oppdater mål imot begge lag
        self.tablaClasificacion[equipoLocal]["golesEnContra"] += golVisitante
        self.tablaClasificacion[equipoVisitante]["golesEnContra"] += golLocal
        # oppdater puntos (3 for seier, 1 for empatado)
        self.tablaClasificacion[equipoLocal]["puntos"] = 3*self.tablaClasificacion[equipoLocal]["ganado"] + self.tablaClasificacion[equipoLocal]["empatado"]
        self.tablaClasificacion[equipoVisitante]["puntos"] = 3*self.tablaClasificacion[equipoVisitante]["ganado"] + self.tablaClasificacion[equipoVisitante]["empatado"]
        
    def actualizarClasificacion(self):
        clasificacionAntigua = self.clasificacion
        self.clasificacion = []
        while len(clasificacionAntigua) > 0: 
            maxpuntos = -1
            mejorEquipo = [] 
            for i in range(len(clasificacionAntigua)):
                lag = clasificacionAntigua[i]
                puntos = self.tablaClasificacion[lag]["puntos"]
                if puntos == maxpuntos:
                    mejorEquipo.append(i)
                elif puntos > maxpuntos: 
                    mejorEquipo = [i]
                    maxpuntos = puntos

            listaMejoresEquipos = []
            for j in mejorEquipo[::-1]:
                listaMejoresEquipos.append(clasificacionAntigua.pop(j)) 

            while len(listaMejoresEquipos) > 0: 
                diferenciaGolesMaxima = -9999
                listaTodosMejoresEquipos = []
                for lag in listaMejoresEquipos:
                    diferenciaGoles = self.tablaClasificacion[lag]["golesAfavor"] - self.tablaClasificacion[lag]["golesEnContra"]
                    if diferenciaGoles == diferenciaGolesMaxima:
                        listaTodosMejoresEquipos.append(lag)
                    elif diferenciaGoles > diferenciaGolesMaxima:
                        listaTodosMejoresEquipos = [lag]
                        diferenciaGolesMaxima = diferenciaGoles
                
                for lag in sorted(listaTodosMejoresEquipos):
                    self.clasificacion.append(lag)
                    listaMejoresEquipos.remove(lag)

    def getClasificacion(self):
        return self.clasificacion

    def print_tablaClasificacion(self):
        print()
        print()
        gol = 0 
        partidosJugados = 0 
        for lag in self.getClasificacion():
            gol += self.tablaClasificacion[lag]["golesAfavor"]
            partidosJugados += self.tablaClasificacion[lag]["partidosJugados"] // 2 

            print(self.tablaClasificacion[lag]["nombre"].ljust(14),
                  str(self.tablaClasificacion[lag]["partidosJugados"]).ljust(2),
                  str(self.tablaClasificacion[lag]["ganado"]).ljust(2),
                  str(self.tablaClasificacion[lag]["empatado"]).ljust(2),
                  str(self.tablaClasificacion[lag]["perdido"]).ljust(2),
                  str(self.tablaClasificacion[lag]["golesAfavor"]).rjust(3),
                  "-",
                  str(self.tablaClasificacion[lag]["golesEnContra"]).ljust(3),
                  str(self.tablaClasificacion[lag]["puntos"]).ljust(3)
            )
        print()
        print("Gjennomsnittlig antall gol:", round(gol/partidosJugados, 2)) # runder av til 2 desimaler