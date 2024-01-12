import bs4
import requests

#Crear url sin numero de paginas
url_base = "https://books.toscrape.com/catalogue/page-{}.html"


#listas de titulos con 4 o 5 estrellas
titulos_rating_alto = []

#iterar paginas
for pagina in range(1, 51):
    
    # crear sopa en cada pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
    
    # seleccionar datos de los libros
    libros = sopa.select('.product_pod')
    
    for libro in libros:
        
        #revisar que tengan 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')):
            
            #guardar el titulo en variable
            titulo_libro = libro.select('a')[1]['title']
            
            #agregar el libro a la lista
            titulos_rating_alto.append(titulo_libro)
            
#ver libros 4 u 5 estrellas en consola
for t in titulos_rating_alto:
    print(t)