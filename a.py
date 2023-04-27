a = ['A','B','C','D','E','F','G','H']
b = ['P','O','N','M','L','K','J','I']
x = a.pop()
print(x)


    def simuler(self):
        nrondas = (len(listaEquipos) - 1)*2 
        nPartidos = len(listaEquipos)//2 

        listaEquipos1 = self.listaEquipos[:nPartidos]
        listaEquipos2aux = self.listaEquipos[nPartidos:]
        listaEquipos2 = []
        for i in listaEquipos2aux:
            listaEquipos2.append(i)
        listaEquipos2.reverse()
        nEquipo1Local = len(listaEquipos1) - 1
        nEquipo2Visitante = len(listaEquipos2)

        for ronda in range(nrondas):
            rondasunde = []
            for partido in range(nPartidos):
                equipo1 = listaEquipos1[partido % nEquipo1Local]
                equipo2 = listaEquipos2[partido % nEquipo2Visitante]

                if ronda % 2 == 1 and equipo1 is not None and equipo2 is not None:
                    partido = Partido(equipo2, equipo1)
                    
                else:
                    partido = Partido(equipo1, equipo2)

                rondasunde.append(partido)

            aux =listaEquipos1[-1]
            listaEquipos1 = [listaEquipos1[0]] + [listaEquipos2[0]] + listaEquipos1[1:-1]
            listaEquipos2 = [listaEquipos2[1]] + listaEquipos2[2:] + [aux]

            self.rondas.append(rondasunde)

    # for key, datos in self.tablaClasificacion.items():
        #     if datos["nombre"] == equipoLocal:
        #         datos["partidosJugados"] += 1
        #         if golLocal > golVisitante:
        #             datos["ganado"] += 1
        #         elif golLocal == golVisitante:
        #             datos["empatado"] += 1
        #         else:
        #             datos["perdido"] += 1
        #         datos["golesAfavor"] += golLocal
        #         datos["golesEnContra"] += golVisitante
        #         datos["puntos"] = 3*datos["ganado"] + datos["empatado"]


        #     if datos["nombre"] == equipoVisitante:
        #         datos["partidosJugados"] += 1
        #         if golLocal < golVisitante:
        #             datos["ganado"] += 1
        #         elif golLocal == golVisitante:
        #             datos["empatado"] += 1
        #         else:
        #             datos["perdido"] += 1
        #         datos["golesAfavor"] += golVisitante
        #         datos["golesEnContra"] += golLocal
        #         datos["puntos"] = 3*datos["ganado"] + datos["empatado"]

        
        #self.actualizarClasificacion()