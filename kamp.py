from random import randint
from lag import Lag
class Partido:
    def __init__(self):
        pass
    
    def __init__(self, equipoLocal: 'Lag',equipoVisitante: 'Lag'): 
        self.equipoLocal = equipoLocal
        self.equipoVisitante = equipoVisitante
        self.golLocal = 0
        self.golVisitante = 0
        self.habilidad()
            
    def getEquipoLocal(self):
        return self.equipoLocal
    
    def getEquipoVisitante(self):
        return self.equipoVisitante 

    def habilidad(self):
        self.golLocal = randint(0, 8)
        self.golVisitante = randint(0, 5)
        
    def getGolLocal(self):
        return self.golLocal

    def getGolVisitante(self):
        return self.golVisitante