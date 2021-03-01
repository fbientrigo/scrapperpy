# Libreria de Busqueda
# Fabian Trigo, @fbientrigo en Github


import requests                 # Para obtener datos de la pagina _____
from bs4 import BeautifulSoup as bs

# Descargar la pagina web ______________________________________________________
def get_page(aniurl, return_soup = False):
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
        page = str(soup).split("\n")

        return page

# Buscador de palabras ________________________________________________________

# Buscador de palabras ________________________________________________________
def grep(texto, buscar, imprimir = False, counter = 0, sep = False):
    """
    #Comparador de Lineas
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