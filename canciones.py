"""
16-02-2023
canciones
Programación Orientada a Objetos - POO
Jeyfrey Calero
"""

from cancionero import listaCanciones
import os

class MiCancion:
    agregar_cancion = 1
    consultar_cancion = 2
    borrar_cancion = 3
    consultar_artista = 4
    salir = 0

    def __init__(self, nombreCancion = ""):
        self._nombreCancion = nombreCancion
        self._nombreArtista = []
        self._tipoGenero = []

    def __str__(self):
        texto = f'************{self._nombreCancion}************ \n'
        texto += "Canción: \n"
        for i,cancion in enumerate(self._nombreCancion):
            texto += f'{i+1}.{cancion}\n'
        for artista in self._nombreArtista:
            texto += f'{artista}\n'
        texto += 'Artista: \n'
        for genero in self._tipoGenero:
            texto += f'{genero}\n'
        return texto

    @property
    def nombreCancion(self):
        return self._nombreCancion

    @nombreCancion.setter
    def nombreCancion(self, valor):
        self._nombreCancion = valor
    
    @nombreCancion.deleter
    def nombreCancion(self):
        del self._nombreCancion

    @property
    def nombreArtista(self):
        return self._nombreArtista

    @nombreArtista.setter
    def nombreArtista(self, valor):
        self._nombreArtista = valor

    @nombreArtista.deleter
    def nombreArtista(self):
        del self._nombreArtista

    @property
    def tipoGenero(self):
        return self._tipoGenero

    @tipoGenero.setter
    def tipoGenero(self, valor):
        self._tipoGenero = valor
    
    @tipoGenero.deleter
    def tipoGenero(self):
        del self._tipoGenero
    
    def menu(self):
        ejecutar = True
        while ejecutar:
            os.system("cls")
            print(f'''Este es tu {self._nombreCancion}
            {self.agregar_cancion}) Agregar cancion
            {self.consultar_cancion}) Consultar cancion
            {self.borrar_cancion}) Borrar cancion
            {self.consultar_artista}) Consultar artista
            {self.salir}) Salir''')

            opcion = int(input("Por favor, ingrese alguna de las opciones anteriores: "))
            if opcion == self.agregar_cancion:
                self.AgregarCancion()
            elif opcion == self.consultar_cancion:
                self.ConsultarCancion()
            elif opcion == self.borrar_cancion:
                self.BorrarCancion()
            elif opcion == self.consultar_artista:
                self.ConsultarArtista()
            elif opcion == self.salir:
                ejecutar = False
            else:
                print('La opción ingresada no es válida')
            input("Presione ENTER para continuar...")


    def AgregarCancion(self):
        continuar = True
        while continuar:
            os.system("cls")
            print("Se agregará una nueva canción a la lista")
            nombre = input("¿Cuál es el NOMBRE de la canción?: ")
            artista =-1
            while artista <=0:
                artista = input("Por favor ingrese el nombre del ARTISTA o GRUPO:  ")
                try:
                    artista = int(artista)
                except:
                    artista =0
            genero = input("Ingrese el GÉNERO de la canción: ")
            melodia = listaCanciones(nombre, artista, genero)
            self.nombreArtista.append(melodia)
            agregarOtra = input("¿Desea agregar otra canción a la lista?: (S/N) ")
            if agregarOtra !="S" and agregarOtra !="s":
                continuar = False


    def ConsultarCancion(self):
        os.system("cls")
        print("Las canciones de la lista son los siguientes: ")
        if len(self.nombreCancion) == 0:
            print("El nombre de la cancion no está en la lista!!!")
        else:
            for i in self.nombreCancion:
                print(f'{i}')
    

    def BorrarCancion(self):
        print("La canción que usted seleccione, será borrada de la lista: ")
        if len(self.nombreCancion) == 0:
            for i in self.nombreCancion(len(self)):
                print(f'{i+1}. {self[i]}')
            print("Presione 0 si desea cancelar la ejecución")

            posicion = int(input(f'Ingrese la posicion de la canción que desea borrar: (1-{len(self)})'))
            if 0 < posicion <= len(self):
                self.pop(posicion - 1)
                print("La canción ha sido borrada con éxito de la lista")
            else:
                print("No es posible eliminar la canción de la lista")
        else:
            print("No hay canciones en la lista")

    def ConsultarArtista(self):
        os.system("cls")
        print("A continuación se muestran todos los artista de la lista")
        if len(self.consultar_artista) == 0:
            print("No existe ningún artista en la lista")
        else:
            for i,artista in self.consultar_artista:
                print(f'{artista}')