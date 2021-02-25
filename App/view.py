"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
import time


"""
La vista se encarga de la interacción con el usuari
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("0- Cargar información en el catálogo")
    print("1- Cargar Videos por Views")
    print("2- Encontrar videos Tendencia por pais")
    print("3- Encontrar videos Tendencia por categoria")
    print("4- Buscar  videos con mas likes")

def initCatalog(opcion):
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog(opcion)


def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)

"""
def printChannel_titleData(channel_title):
    if author:
        print('Autor encontrado: ' + author['name'])
        print('Promedio: ' + str(author['average_rating']))
        print('Total de libros: ' + str(lt.size(author['books'])))
        for book in lt.iterator(author['books']):
            print('Titulo: ' + book['title'] + '  ISBN: ' + book['isbn'])
    else:
        print('No se encontro el autor')
"""

def printBestVideos(videos):
    size = lt.size(videos)
    if size:
        print(' Estos son los mejores videos: ')
        for video in lt.iterator(videos):
            print('Titulo: ' + video['title'] + '  views: ' +
                  video['views'] + ' Likes: ' + video['likes'])
    else:
        print('No se encontraron videos')

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 0:
        opcion = str(input("Con que tipo quiere abrir los datos... ARRAY_LIST o LINKED_LIST\n"))
        print("Cargando información de los archivos ....")
        catalog = initCatalog(opcion)
        loadData(catalog)
        print('Videos cargados: ' + str(lt.size(catalog['title'])))
        "print('Nombres de canales cargados: ' + str(lt.size(catalog['channel_title'])))"

    elif int(inputs[0]) == 1:
        t1 = time.process_time()
        size = int(input("Indique tamaño de la muestra: "))
        #n_datos = int(input("Seleccione el numero de datos: "))
        ordena = input("Elija entre shell sort, insertion sort y selection sort: ")
        result = controller.ordenamiento(size, catalog, ordena)
        print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                                          str(result[0]))
        print("Se ejecuto el Requerimiento 1")
        t2 = time.process_time()
        print("El proceso ha durado", t2 - t1, "segundos\n")
    
    elif int(inputs[0]) == 2:
        t1 = time.process_time()
        print("Se ejecuto el Requerimiento 2")
        t2 = time.process_time()
        print("El proceso ha durado", t2 - t1, "segundos\n")
    
    elif int(inputs[0]) == 3:
        t1 = time.process_time()
        print("Se ejecuto el Requerimiento 3")
        t2 = time.process_time()
        print("El proceso ha durado", t2 - t1, "segundos\n")
    
    elif int(inputs[0]) == 4:
        t1 = time.process_time()
        print("Se ejecuto el Requerimiento 4")
        t2 = time.process_time()
        print("El proceso ha durado", t2 - t1, "segundos\n")

    else:
        sys.exit(0)
sys.exit(0)
