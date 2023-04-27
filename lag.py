class Lag:
    
    def __init__(self, nombre: str, golesAnotadosProm: float, golesRecibidosProm: float):
        self.nombre = nombre
        self.golesAnotadosProm = golesAnotadosProm
        self.golesRecibidosProm = golesRecibidosProm

    def getNombre(self):
        return self.nombre
    
    def getGolesAnotadosProm(self):
        return self.golesAnotadosProm
    
    def getGolesRecibidosProm(self):
        return self.golesRecibidosProm
    
    def __gt__(self, other: 'Lag'):
        return len(self.getNombre()) > len(other.getNombre())
        
    def __lt__(self, other: 'Lag'):
        return len(self.getNombre()) < len(other.getNombre())