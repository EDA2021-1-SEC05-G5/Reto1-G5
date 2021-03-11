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
from DISClib.Algorithms.Sorting import insertionsort
from DISClib.Algorithms.Sorting import selectionsort
from DISClib.Algorithms.Sorting import mergesort
from DISClib.Algorithms.Sorting import quicksort
import time
assert cf
import time
 
"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, 
otra para las categorias de los mismos.
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'videos': None,
               'views': None,
               'category': None
                }

    catalog['videos'] = lt.newList("ARRAY_LIST", cmpfunction = comparevideo_id1)
    catalog['category'] = lt.newList("ARRAY_LIST", cmpfunction = comparevideo_id1)

    return catalog




# Funciones para agregar informacion al catalogo 

def addVideo(catalog, video):
    # Se adiciona el libro a la lista de libros
    lt.addLast(catalog['videos'], video)
    # Se obtienen los autores del libro
    #channel_titles = video['channel_title'].split(",")
    # Cada autor, se crea en la lista de libros del catalogo, y se
    # crea un libro en la lista de dicho autor (apuntador al libro)
    #for channel_title in channel_titles:
    #    addVideoChannel_title(catalog, channel_title.strip(), video)

def addCategory(catalog, category):
    lt.addLast(catalog['category'], category)

    


# Funciones para creacion de datos
"""
def newchannel_title(name):

    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings

    channel_title = {'name': "", "video": None,  "likes": 0}
    channel_title['name'] = name
    channel_title['title'] = lt.newList('ARRAY_LIST')
    return channel_title


def newTag(name, id):

    Esta estructura almancena los tags utilizados para marcar libros.

    tag = {'name': '', 'tag_id': ''}
    tag['name'] = name
    tag['tag_id'] = id
    return tag



def newBookTag(tag_id, video_id):

    Esta estructura crea una relación entre un tag y
    los libros que han sido marcados con dicho tag.
 
    videotag = {'tag_id': tag_id, 'video_id': video_id}
    return videotag
"""



# Funciones de consulta

#1 y 3
def get_id_categoria (categoria, catalog):

    id_categoria = None

    for cate in lt.iterator(catalog['category']):
        if cate['name'].strip() == categoria: 
            id_categoria = int(cate['id'])
            break

    return id_categoria

#1
def filtrar_pais_categoria (id_categoria, pais, catalog):

    nueva_lista = lt.newList("ARRAY_LIST", cmpfunction = comparevideo_id1)

    for x in lt.iterator(catalog['videos']):
        if int(x['category_id']) == id_categoria and str(x['country'].strip()) == pais:
            lt.addLast(nueva_lista, x)

    return nueva_lista

#2
def filtrar_pais (pais, catalog):
    lista_pais = lt.newList("ARRAY_LIST", cmpfunction = comparevideo_id1)

    for x in lt.iterator(catalog['videos']):
        if str(x['country'].strip()) == pais:
            lt.addLast(lista_pais, x)
        
    return lista_pais

#2
def getTendencia2(sorted_list):

    mayor = lt.firstElement(sorted_list)
    conteo = 0

    sig = None
    conteo_sig = 0

    for x in lt.iterator(sorted_list):
        if x['video_id'] == mayor["video_id"]:
            conteo += 1
 
        elif sig == None: 
            sig = x
            conteo_sig += 1

        elif x['video_id'] == sig["video_id"]:
                conteo_sig += 1
                
        else:
            if conteo_sig > conteo:
                mayor = sig
                conteo = conteo_sig
            sig = x
            conteo_sig = 1

    return mayor, conteo

#3
def filtrar_categoria (id_categoria, catalog):

    nueva_lista = lt.newList("ARRAY_LIST", cmpfunction = cmpVideosByID_date)

    for x in lt.iterator(catalog['videos']):
        if x['video_id'] == '#NAME?':
            pass        
        else:
            if int(x['category_id']) == id_categoria:
                lt.addLast(nueva_lista, x)

    return nueva_lista   

#3
def getTendencia3 (sorted_list):

    mayor = lt.firstElement(sorted_list)
    conteo = 1

    sig = None
    conteo_sig = 1

    for x in lt.iterator(sorted_list):
        if x['video_id'] == mayor["video_id"]:
            if x['trending_date'] != mayor["trending_date"]:
                conteo += 1
 
        elif sig == None: 
            sig = x
            conteo_sig += 1

        elif x['video_id'] == sig["video_id"]:
            if x['trending_date'] != sig["trending_date"]:
                conteo_sig += 1
                
        else:
            if conteo_sig > conteo:
                mayor = sig
                conteo = conteo_sig
            sig = x
            conteo_sig = 1

    return mayor, conteo

#4
def filtrar_pais_tag (tag, pais, catalog):
    nueva_lista = lt.newList("ARRAY_LIST", cmpfunction = cmpVideosByLikes)

    for x in lt.iterator(catalog['videos']):
        if str(x['country'].strip()) == pais:
            lista_tags = (x['tags'].split("|"))
            for y in lista_tags:
                if tag in str(y):
                    lt.addLast(nueva_lista, x)

    return nueva_lista

#4
def acortar_lista (sorted_list, cantidad):

    lista_final = lt.newList("ARRAY_LIST", cmpfunction = cmpVideosByLikes)
    
    for x in lt.iterator(sorted_list):
        if lt.isEmpty(lista_final):
            lt.addLast(lista_final, x)
        else:
            cond = True
            for y in lt.iterator(lista_final):
                if y['title'] == x['title']:
                    cond = False
            if cond == True:
                lt.addLast(lista_final, x)
                if lt.size(lista_final) == cantidad: 
                    break
        if lt.size(lista_final) == cantidad:
            break

    return lista_final


"""
def getVideosByChannel_title(catalog, authorname):
    
    Retorna un autor con sus libros a partir del nombre del autor
    
    poschannel_title = lt.isPresent(catalog['channel_title'], authorname)
    if poschannel_title > 0:
        channel_title = lt.getElement(catalog['channel_title'], poschannel_title)
        return channel_title
    return None


def getBestVideos(catalog, number):
    
    Retorna los mejores videos
    videos = catalog['videos']
    bestvideos = lt.newList()
    for cont in range(1, number+1):
        video = lt.getElement(videos, cont)
        lt.addLast(bestvideos, video)
    return bestvideos


def countVideosByTag(catalog, tag):
    
    Retorna los libros que fueron etiquetados con el tag
    
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
"""







# Funciones utilizadas para comparar elementos dentro de una lista

def comparevideo_id1(video1, video2):
    return video1["video_id"] < video2["video_id"]

def cmpVideosByID_date (video1, video2):
    if video1['video_id'] != video2['video_id']:
        return video1["video_id"] < video2["video_id"]   
    else:
        return video1["trending_date"] < video2["trending_date"]

def cmpVideosByViews(video1, video2):
    """
    Devuelve verdadero (True) si los 'views' de video1 son menores que los del video2
    Args:
    video1: informacion del primer video que incluye su valor 'views'
    video2: informacion del segundo video que incluye su valor 'views'
    """
    return (float(video1['views']) > float(video2['views']))

def cmpVideosByLikes(video1, video2):

    return (float(video1['likes']) > float(video2['likes']))








# Funciones de ordenamiento

#1
def sortVideosByViews (lista_filtros, cantidad):

    sorted_list = mergesort.sort(lista_filtros, cmpVideosByViews)

    sub_list = lt.subList(sorted_list, 1, cantidad)
    sub_list = sub_list.copy()

    return sub_list

#2
def sortVideosByID (filtro_pais):

    sorted_list = mergesort.sort(filtro_pais, comparevideo_id1)

    return sorted_list 

#3
def sortVideosByID_date (filtro_categoria):
    
    sorted_list = mergesort.sort(filtro_categoria, cmpVideosByID_date)

    return sorted_list

#4
def sortVideosByLikes (lista_filtros):

    sorted_list = mergesort.sort(lista_filtros, cmpVideosByLikes)
    
    return sorted_list







"""DE AQUI PARA ABAJO NO VA"""

#1 viejo
def id_categoria (categoria, catalog):

    id_categoria = None

    for cate in lt.iterator(catalog['category']):
        if cate['name'].strip() == categoria: 
            id_categoria = int(cate['id'])
            break

    return id_categoria

def sortVideos(lista_filtros, cantidad):

    sorted_list = mergesort.sort(lista_filtros, cmpVideosByViews)

    sub_list = lt.subList(sorted_list, 1, cantidad)
    sub_list = sub_list.copy()

    return sub_list




#2 viejo
def filtro_pais (pais, catalog):
    lista_pais = lt.newList("ARRAY_LIST", cmpfunction = comparevideo_id1)

    for x in lt.iterator(catalog['videos']):
        if str(x['country'].strip()) == pais:
            lt.addLast(lista_pais, x)
        
    return lista_pais

def sortVideoID (lista_pais):

    sorted_list = mergesort.sort(lista_pais, comparevideo_id1)

    return sorted_list 

def tendencia (sorted_list):

    mayor = lt.firstElement(sorted_list)
    conteo = 0

    sig = None
    conteo_sig = 0

    for x in lt.iterator(sorted_list):
        if x['video_id'] == mayor["video_id"]:
            conteo += 1
 
        elif sig == None: 
            sig = x
            conteo_sig += 1

        elif x['video_id'] == sig["video_id"]:
                conteo_sig += 1
                
        else:
            if conteo_sig > conteo:
                mayor = sig
                conteo = conteo_sig
            sig = x
            conteo_sig = 1

    return mayor, conteo







#3 viejo
def filtro_categoria (id_categoria, catalog):

    nueva_lista = lt.newList("ARRAY_LIST", cmpfunction = cmpVideoID_date)

    for x in lt.iterator(catalog['videos']):
        if x['video_id'] == '#NAME?':
            pass        
        else:
            if int(x['category_id']) == id_categoria:
                lt.addLast(nueva_lista, x)

    return nueva_lista

def sortVideoID_date (filtro_categoria):

    sorted_list = mergesort.sort(filtro_categoria, cmpVideoID_date)

    return sorted_list
    
def tendencia_categoria (sorted_list):
    """
    mayor = lt.firstElement(sorted_list)
    
    lista_sin_reps = lt.newList("ARRAY_LIST", cmpfunction = cmpVideoID_date)


    for x in lt.iterator(sorted_list):
        if x == lt.firstElement(sorted_list):
            lt.addLast(lista_sin_reps, x)
        else:
            if mayor['video_id'] == x['video_id']:
                if mayor['trending_date'] == x['trending_date']:
                    pass
                else:
                    lt.addLast(lista_sin_reps, x)
                    mayor = x
    """


    mayor = lt.firstElement(sorted_list)
    conteo = 1

    sig = None
    conteo_sig = 1

    for x in lt.iterator(sorted_list):
        if x['video_id'] == mayor["video_id"]:
            if x['trending_date'] != mayor["trending_date"]:
                conteo += 1
 
        elif sig == None: 
            sig = x
            conteo_sig += 1

        elif x['video_id'] == sig["video_id"]:
            if x['trending_date'] != sig["trending_date"]:
                conteo_sig += 1
                
        else:
            if conteo_sig > conteo:
                mayor = sig
                conteo = conteo_sig
            sig = x
            conteo_sig = 1

    return mayor, conteo





#4 viejo
def cortar2 (tag, pais, catalog):
    nueva_lista = lt.newList("ARRAY_LIST", cmpfunction = cmpVideosByLikes)

    for x in lt.iterator(catalog['videos']):
        if str(x['country'].strip()) == pais:
            lista_tags = (x['tags'].split("|"))
            for y in lista_tags:
                if tag in str(y):
                    lt.addLast(nueva_lista, x)

    return nueva_lista

def ordenar2(nueva_lista):

    sorted_list = mergesort.sort(nueva_lista, cmpVideosByLikes)
    
    return sorted_list

def cantidad2 (sorted_list, cantidad):

    lista_final = lt.newList("ARRAY_LIST", cmpfunction = cmpVideosByLikes)
    
    for x in lt.iterator(sorted_list):
        if lt.isEmpty(lista_final):
            lt.addLast(lista_final, x)
        else:
            cond = True
            for y in lt.iterator(lista_final):
                if y['title'] == x['title']:
                    cond = False
            if cond == True:
                lt.addLast(lista_final, x)
                if lt.size(lista_final) == cantidad: 
                    break
        if lt.size(lista_final) == cantidad:
            break

    return lista_final











#10/03

"""
Basura model

def newCatalog:
    
        #catalog['channel_title'] = lt.newList('ARRAY_LIST',
                                    #cmpfunction=comparechannel_titles)
        #catalog['views'] = lt.newList('ARRAY_LIST',
                                 #cmpfunction=cmpVideosByViews)
        #catalog['videos_tags'] = lt.newList('ARRAY_LIST')


#Funciones para añadir info al catalogo

def addVideo(catalog, video):
    # Se adiciona el libro a la lista de libros
    lt.addLast(catalog['videos'], video)
    # Se obtienen los autores del libro
    #channel_titles = video['channel_title'].split(",")
    # Cada autor, se crea en la lista de libros del catalogo, y se
    # crea un libro en la lista de dicho autor (apuntador al libro)
    #for channel_title in channel_titles:
    #    addVideoChannel_title(catalog, channel_title.strip(), video)

def addVideoChannel_title(catalog, authorname, video):
    
    #Adiciona un autor a lista de autores, la cual guarda referencias
    #a los libros de dicho autor
    
    channel_titles = catalog['channel_title']
    poschannel_title = lt.isPresent(channel_titles, authorname)
    if poschannel_title > 0:
        channel_title = lt.getElement(channel_titles, poschannel_title)
    else:
        channel_title = newchannel_title(authorname)
        lt.addLast(channel_titles, channel_title)
    lt.addLast(channel_title['title'], video)
"""

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


# Funciones para creacion de datos

def newchannel_title(name):

    #Crea una nueva estructura para modelar los libros de
    #un autor y su promedio de ratings


    channel_title = {'name': "", "video": None,  "likes": 0}
    channel_title['name'] = name
    channel_title['title'] = lt.newList('ARRAY_LIST')
    return channel_title


def newTag(name, id):
    #Esta estructura almancena los tags utilizados para marcar libros.

    tag = {'name': '', 'tag_id': ''}
    tag['name'] = name
    tag['tag_id'] = id
    return tag


def newBookTag(tag_id, video_id):
    #Esta estructura crea una relación entre un tag y
    #los libros que han sido marcados con dicho tag.

    videotag = {'tag_id': tag_id, 'video_id': video_id}
    return videotag



# Funciones de consulta

def getVideosByChannel_title(catalog, authorname):
    
    #Retorna un autor con sus libros a partir del nombre del autor
    
    poschannel_title = lt.isPresent(catalog['channel_title'], authorname)
    if poschannel_title > 0:
        channel_title = lt.getElement(catalog['channel_title'], poschannel_title)
        return channel_title
    return None


def getBestVideos(catalog, number):
    
    #Retorna los mejores videos
    
    videos = catalog['videos']
    bestvideos = lt.newList()
    for cont in range(1, number+1):
        video = lt.getElement(videos, cont)
        lt.addLast(bestvideos, video)
    return bestvideos


def countVideosByTag(catalog, tag):

    Retorna los libros que fueron etiquetados con el tag

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


#


# Funciones utilizadas para comparar elementos dentro de una lista

def comparechannel_titles(channel_titlename1, channel_title):
    if (channel_titlename1.lower() in channel_title['name'].lower()):
        return 0
    return -1

"""