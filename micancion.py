"""
16-02-2023
micancion
Programación Orientada a Objetos - POO
Jeyfrey Calero
"""

from canciones import MiCancion

def main():
    miCancion = MiCancion("Listado de Canciones")
    miCancion.menu()
    print(MiCancion)

if __name__ == "__main__":
    main()

