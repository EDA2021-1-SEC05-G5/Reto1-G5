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
import sys
default_limit = 1000000
sys.setrecursionlimit(default_limit*10) 

"""
La vista se encarga de la interacción con el usuari
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("\nBienvenido")
    print("0- Cargar datos del .csv")
    print("1- Req 1 - Videos con más views (categoría, país y n)")
    print("2- Req 2 - Video tendencia (país)")
    print("3- Req 3 - Video tendencia (categoría)")
    print("4- Req 4 - Videos con más likes (tag, país y n)")

def initCatalog():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog()


def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)

"""
def printChannel_Data(channel_title):
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

        #opcion = "ARRAY_LIST"
        #ordena = 'merge' 

        print("Cargando información de los archivos...")
        catalog = initCatalog()
        loadData(catalog)

        print('Videos cargados: ' + str(lt.size(catalog['videos'])))

        print('\nInfo del primer video:\n',
        "Título del video: ",(lt.firstElement(catalog['videos']))['title'], 
        "\nTítulo del canal del video: ",(lt.firstElement(catalog['videos']))['channel_title'], 
        "\nFecha de tendencia del video: ",str((lt.firstElement(catalog['videos']))['trending_date']),
        "\nPaís del video: ",(lt.firstElement(catalog['videos']))['country'],
        "\nViews del video: ",(lt.firstElement(catalog['videos']))['views'],
        "\nLikes del video: ",(lt.firstElement(catalog['videos']))['likes'],
        "\nDislikes del video: ",(lt.firstElement(catalog['videos']))['dislikes'])

        print('\nId y categorías: ')
        for c in lt.iterator(catalog['category']):
            print(c['id'],c["name"])
    
    elif int(inputs[0]) == 1:

        categoria = input('Ingrese la categoría: ')
        pais = input('Ingrese el país: ')
        cantidad = int(input('Ingrese el número de videos: '))

        respuesta = controller.requerimiento_1(categoria, pais, cantidad, catalog)
        lista = respuesta["elements"]

        for v in lista:
            print("\nFecha de tendencia: ",v['trending_date'])
            print("Nombre del video: ", v['title'])
            print("Nombre del canal: ", v['channel_title'])
            print("Fecha de publicación : ", v['publish_time'])
            print("Reproducciones: ", v['views'])
            print("Likes: ", v['likes'])
            print("Dislikes: ", v['dislikes'])

    elif int(inputs[0]) == 2:

        pais = input("Ingrese el país: ")
        respuesta = controller.requerimiento_2(pais, catalog)
        print(respuesta)

    elif int(inputs[0]) == 3:

        categoria = input('Ingrese la categoría: ')
        respuesta = controller.requerimiento_3(categoria, catalog)
        print(respuesta)
        #for book in lt.iterat
        # or(respuesta):
        #    print(book['video_id']+"/",book['trending_date'],"/"+book['title'])

    elif int(inputs[0]) == 4:

        tag = input('Ingrese el tag: ')
        pais = input('Ingrese el país: ')
        cantidad = int(input('Ingrese el número de videos: '))

        respuesta = controller.requerimiento_4(tag, pais, cantidad, catalog)
        print(respuesta)

    else:
        sys.exit(0)
sys.exit(0)