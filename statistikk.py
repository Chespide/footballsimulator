class Statistikk:
    def __init__(self, listaEquipos):
        self.posciciones = {}

        for lag in listaEquipos:
            # til å begynne med er listen [0, 0, 0, ..., 0]
            self.posciciones[lag] = [0]*len(listaEquipos)

    def guardarPoscicion(self, rangering):    
        for j in range(len(rangering)):     # for hver plassering:
            lag = rangering[j]                  # finn ut hvilket lag som fikk denne plasseringen
            self.posciciones[lag][j] += 1     # registrer at dette laget fikk en slik plassering denne sesongen

    # Skriver ut statistikken etter at alle sesongene er spilt
    def print_posciciones(self):
        print()
        for lag in self.posciciones: # for hvert lag
            print()
            print(lag.getNombre())    # skriv ut lagets nombre
            print("-"*len(lag.getNombre()))
            plasseringsliste = self.posciciones[lag] # hent listen med posciciones for dette laget
            # bruker indeksen j som løkkevariabel slik at vi også kan skrive ut
            # hvilken plass det er snakk om (0 = 1.plass, 1 = 2.plass, osv.)
            for j in range(len(plasseringsliste)):
                antall = plasseringsliste[j] # antall posciciones av denne typen
                print(str(j + 1).ljust(2), str(antall).rjust(5))