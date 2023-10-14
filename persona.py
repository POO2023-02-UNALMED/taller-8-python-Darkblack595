class Persona:
    def __init__(self,nombre,edad,altura,sexo):
        self._nombre = nombre
        self._edad = edad
        self._altura = altura
        self._sexo = sexo
    
    def getNombre(self):
      return self._nombre
    def setNombre(self, new_nombre):
      self._nombre = new_nombre
  
    def getEdad(self):
      return self._edad
    def setEdad(self, new_edad):
      self._edad = new_edad
  
    def getAltura(self):
      return self._altura
    def setAltura(self, new_altura):
      self._altura = new_altura
  
    def getSexo(self):
      return self._sexo
    def setSexo(self, new_sexo):
      self._sexo = new_sexo


    