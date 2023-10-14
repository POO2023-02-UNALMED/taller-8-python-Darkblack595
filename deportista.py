class Deportista:
    def __init__(self,deporte = "Futbol",añosPracticando = None):
        self._deporte = deporte
        self._añosPracticando = añosPracticando

    def getDeporte(self):
      return self._deporte
    def setDeporte(self, new_deporte):
      self._deporte = new_deporte
  
    def getAñosPracticando(self):
      return self._añosPracticando
    def setAñosPracticando(self, new_añosPracticando):
      self._añosPracticando = new_añosPracticando
  
    
    