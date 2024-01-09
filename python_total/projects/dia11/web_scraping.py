import bs4
import requests

resultado = requests.get('https://escueladirecta-blog.blogspot.com/')

sopa = bs4.BeautifulSoup(resultado.text, "lxml")

columna_lateral = sopa.select('.content')

if columna_lateral:
    # Process the elements found
    for element in columna_lateral:
        print(element)
else:
    print("No elements with class 'content' found on the page.")
