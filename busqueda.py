# Libreria de Busqueda
# Fabian Trigo, @fbientrigo en Github


import requests                 # Para obtener datos de la pagina _____
from bs4 import BeautifulSoup as bs
import re

# Descargar la pagina web ______________________________________________________
def get_page(aniurl, return_soup = False, as_list = True):
    """
    Utilzamos beautiful soup y request para obtener la url y obtener la pagina
    como texto separado por linea dentro de una lista, esta funcion devuelve una
    lista

    >> get_page("https://github.com/fbientrigo/scrappypy")
        >> <!DOCTYPE html> == $0 \\n <html la...
    
    """
    #descargamos la pagina
    page = requests.get(aniurl)
    #la ordenamos
    soup = bs(page.content, 'html.parser')
    if return_soup:
        return soup
    else:
        # separamos cada linea en elementos de una lista
        page = str(soup)
        if as_list:
            return page.split("\n")
        else:
            return page

# Buscador de palabras ________________________________________________________

# Buscador de palabras ________________________________________________________
def grep(texto, buscar, imprimir = False, counter = 0, sep = False):
    """
    #Comparador de Lineas
    notese que el objeto texto es una lista, de hallar un elemento
    retornara el elemento lista que coincida
    ingrese string en el texto y buscar, en caso de que el texto contenga la palabra
    que reemplazo por buscar, se imprimira la linea donde aparecio

    >> grep("hola \\n como estas","estas") -> "como estas"


    la opcion counter se saltara tantos matches

    >> grep("hola caracola \\n hola tu","estas", counter = 0) -> "hola caracola"
    >> grep("hola caracola \\n hola tu","estas", counter = 1) -> "hola tu"

    """
    if sep:
        #Separamos el texto en lineas
        texto = str(texto).split("\n")

    for linea in texto:
        if buscar in linea: #de haber matche

            if counter == 0:        #revisamos el counter
                if imprimir:
                    print(linea)
                else:
                    return linea
            counter = counter - 1 # de haber visto un match, restamos uno al counter
                #de manera que el siguiente pueda caer con counter 0 y ser ejecutado
            print(linea)

#Uso de RegularExpression
# llamadas expresiones regulares, puedes investigar sobre como usarlas aqui:
# 
def regrep(patron, texto):
    """
    Return the Expression Found (return the grep)
    Toma el texto como una lista, la cual representara una linea
    luego retorna una lista de todos los matches realizados, no de las lineas que contienen     estos matches
    """
    nfound = []
    for line in texto:
        ff = re.findall(r".\d-\d.",line)
        if ff != []:
            nfound.append(ff)
    return nfound

def linegrep(patron, texto):
    """
    Line of Expression Found (line of grep)
    Toma el texto como una lista, la cual representara una linea
    luego retorna una lista de todos las lineas que contienen un match
    """
    found = []
    for line in texto:
        ff = re.search(patron,line)
        if ff != None:
            found.append(ff.string)

# Animeflv

# Para descargar de servidores ____________________________________________________________
def obtlinkser(url0, server = "zippy", debug= False, counter = 0):
    animesopa = get_page(url0,True) #descargamos la pagina como        una sopa
    #buscamos las referencias a links en la pagina:
    hrefs= []
    for a in animesopa.find_all('a', href=True):
        if debug:
            print("Found the URL:", a['href'])
        hrefs.append(a['href'])
    if debug:
        print(hrefs)

    animesopa = list(map(str, hrefs))

    if debug:
        print(animesopa) #sigue todo desordenado aqui

    # Pescamos el servidor
    link = grep(animesopa, server,counter = counter)
    if debug:
        print(link)
        print("Se obtuvo el link del servidor, hasta ahora todo bien")
    
    return link
    
#Esto es para loopear entre una lista de capitulos y obtener el link final
def loopearS(caps, server = "MEGA",debug=False, counter = 0):
    """
    Loopea atravez de los links de servidor buscado con grep
    """
    link = []
    for c in caps:
        if debug:
            print("Obteniendo link de Server___________ cap: ",c)
        linko = obtlinkser(c,server,debug, counter = counter)
        link.append(linko)
        if debug:
            print("Link agregado: ", linko)
            print("_______________________")
    return link