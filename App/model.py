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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'title': None,
               'channel_title': None,
               'tags': None,
               'video_tags': None}

    catalog['title'] = lt.newList()
    catalog['channel_title'] = lt.newList('ARRAY_LIST',
                                    cmpfunction=comparechannel_titles)
    catalog['tags'] = lt.newList('ARRAY_LIST',
                                 cmpfunction=comparetagnames)
    catalog['videos_tags'] = lt.newList('ARRAY_LIST')

    return catalog



# Funciones para agregar informacion al catalogo 

def addVideo(catalog, video):
    # Se adiciona el libro a la lista de libros
    lt.addLast(catalog['title'], video)
    # Se obtienen los autores del libro
    channel_titles = video['channel_title'].split(",")
    # Cada autor, se crea en la lista de libros del catalogo, y se
    # crea un libro en la lista de dicho autor (apuntador al libro)
    for channel_title in channel_titles:
        addVideoChannel_title(catalog, channel_title.strip(), video)


def addVideoChannel_title(catalog, authorname, video):
    """
    Adiciona un autor a lista de autores, la cual guarda referencias
    a los libros de dicho autor
    """
    channel_titles = catalog['channel_title']
    poschannel_title = lt.isPresent(channel_titles, authorname)
    if poschannel_title > 0:
        channel_title = lt.getElement(channel_titles, poschannel_title)
    else:
        channel_title = newchannel_title(authorname)
        lt.addLast(channel_titles, channel_title)
    lt.addLast(channel_title['title'], video)

"""
def addTag(catalog, tag):
    
    #Adiciona un tag a la lista de tags
    
    t = newTag(tag['tag_name'], tag['tag_id'])
    lt.addLast(catalog['tags'], t)
"""
"""
def addVideoTag(catalog, videotag):
    
    #Adiciona un tag a la lista de tags
    
    t = newVideoTag(videotag['tag_id'], videotag['video_id'])
    lt.addLast(catalog['video_tags'], t)
"""


# Funciones para creacion de datos

def newchannel_title(name):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    channel_title = {'name': "", "video": None,  "likes": 0}
    channel_title['name'] = name
    channel_title['title'] = lt.newList('ARRAY_LIST')
    return channel_title


def newTag(name, id):
    """
    Esta estructura almancena los tags utilizados para marcar libros.
    """
    tag = {'name': '', 'tag_id': ''}
    tag['name'] = name
    tag['tag_id'] = id
    return tag


def newBookTag(tag_id, video_id):
    """
    Esta estructura crea una relación entre un tag y
    los libros que han sido marcados con dicho tag.
    """
    videotag = {'tag_id': tag_id, 'video_id': video_id}
    return videotag



# Funciones de consulta

def getVideosByChannel_title(catalog, authorname):
    """
    Retorna un autor con sus libros a partir del nombre del autor
    """
    poschannel_title = lt.isPresent(catalog['channel_title'], authorname)
    if poschannel_title > 0:
        channel_title = lt.getElement(catalog['channel_title'], poschannel_title)
        return channel_title
    return None


def getBestVideos(catalog, number):
    """
    Retorna los mejores videos
    """
    videos = catalog['title']
    bestvideos = lt.newList()
    for cont in range(1, number+1):
        video = lt.getElement(videos, cont)
        lt.addLast(bestvideos, video)
    return bestvideos


def countVideosByTag(catalog, tag):
    """
    Retorna los libros que fueron etiquetados con el tag
    """
    tags = catalog['tags']
    videocount = 0
    pos = lt.isPresent(tags, tag)
    if pos > 0:
        tag_element = lt.getElement(tags, pos)
        if tag_element is not None:
            for video_tag in lt.iterator(catalog['video_tags']):
                if tag_element['tag_id'] == video_tag['tag_id']:
                    videocount += 1
    return videocount



# Funciones utilizadas para comparar elementos dentro de una lista

def comparechannel_titles(channel_titlename1, channel_title):
    if (channel_titlename1.lower() in channel_title['name'].lower()):
        return 0
    return -1


def comparelikes(video1, video2):
    return (float(video1['likes']) > float(video2['likes']))


def comparetagnames(name, tag):
    return (name == tag['name'])



# Funciones de ordenamiento

def sortVideos(catalog):
    sa.sort(catalog['title'], comparelikes)
