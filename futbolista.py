from deportista import Deportista
from persona import Persona
class Futbolista(Persona,Deportista):
    _listaFutbolista = []
    def __init__(self,nombre,edad,altura,sexo,añosPracticando,golesMarcados,tarjetasRojas,piernaHabil):
        Persona.__init__(self,nombre,edad,altura,sexo)
        Deportista.__init__(self,"Futbol",añosPracticando)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista._listaFutbolista += 1

    def getGolesMarcados(self):
      return self._golesMarcados
    def setGolesMarcados(self, new_golesMarcados):
      self._golesMarcados = new_golesMarcados
  
    def getTarjetasRojas(self):
      return self._tarjetasRojas
    def setTarjetasRojas(self, new_tarjetasRojas):
      self._tarjetasRojas = new_tarjetasRojas
  
    def getPiernaHabil(self):
      return self._piernaHabil
    def setPiernaHabil(self, new_piernaHabil):
      self._piernaHabil = new_piernaHabil
    
    def __str__(self):
       return "Mi nombre es "+self.getNombre()+" soy profesional en el deporte "+self.getDeporte()+". Tengo "+self.getEdad()+" años de edad y llevo "+self.setAñosPracticando()+" años en el deporte."

