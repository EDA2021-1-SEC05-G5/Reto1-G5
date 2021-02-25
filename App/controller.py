"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initCatalog(opcion):
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog(opcion)
    return catalog



# Funciones para la carga de datos

def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadVideos(catalog)
    #loadTags(catalog)
    #loadVideosTags(catalog)
    #sortVideos(size, catalog, ordena)


def loadVideos(catalog):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    videosfile = cf.data_dir + 'videos-large.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)

"""
def loadTags(catalog):
    
    #Carga todos los tags del archivo y los agrega a la lista de tags
    
    tagsfile = cf.data_dir + 'category-id.csv'
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    for tag in input_file:
        model.addTag(catalog, tag)
"""
"""
def loadVideosTags(catalog):
    
    #Carga la información que asocia tags con libros.
    
    booktagsfile = cf.data_dir + 'GoodReads/book_tags.csv'
    input_file = csv.DictReader(open(booktagsfile, encoding='utf-8'))
    for booktag in input_file:
        model.addBookTag(catalog, booktag)
"""


# Funciones de ordenamiento

def sortVideos(size, catalog, ordena):
    """
    Ordena los libros por average_rating
    """
    model.sortVideos(size, catalog, ordena)



# Funciones de consulta sobre el catálogo

def getVideosByChannel_title(catalog, authorname):
    """
    Retrona los libros de un autor
    """
    channel_title = model.getVideosByChannel_title(catalog, authorname)
    return channel_title


def getBestVideos(catalog, number):
    """
    Retorna los mejores libros
    """
    bestvideos = model.getBestVideos(catalog, number)
    return bestvideos


def countVideosByTag(catalog, tag):
    """
    Retorna los libros que fueron etiquetados con el tag
    """
    return model.countVideosByTag(catalog, tag)

def ordenamiento(n_datos, estructura, ordena):
    return model.sortVideos(n_datos, estructura, ordena)