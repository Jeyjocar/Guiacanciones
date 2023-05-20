"""
16-02-2023
Lista de canciones
Programación Orientada a Objetos - POO
Jeyfrey Calero
"""

class listaCanciones():
    def __init__(self, nombre = "", artista = None, genero = ""):
        self._nombre = nombre
        self._artista = artista
        self._genero = genero

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
    
    @nombre.deleter
    def nombre(self):
        del self._nombre
    
    @property
    def artista(self):
        return self._artista
    
    @artista.setter
    def artista(self, valor):
        self._artista = valor

    @artista.deleter
    def artista(self):
        del self._artista

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, valor):
        self._genero = valor

    @genero.deleter
    def genero(self):
        del self._genero

    def __str__(self):
        return f''' Canción {self._nombre}, {self._artista}, {self._genero}'''


