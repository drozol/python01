# days = ['poniedzielek','wtorek','sroda','czwartek','piatek','sobota','niedziela']
# weekend = ('sobota','niedziela')
#
# for day in days:
#     if day in weekend:
#         print ('Jest weekend')
#     else:
#         print ("Trzeba pracować")
#####################################

# from PIL import Image
#
# image : Image.Image = Image.open ('sheet.jpg')
#
# # image.show()
# image = image.resize ((4400,4200))
# image = image.rotate(90)
# image.save('sheet2.jpg')

import requests
# wp_page = requests.get('https://wp.pl')
# print (wp_page.text)

# api_key = '800101cc05e0bcd5b88c816246c988ff'
# api_host = 'http://api.openweathermap.org/data/2.5/weather'
# city = 'Gdańsk'
#
# results = requests.get(f'{api_host}?appid={api_key}&q={city}')
#
# dict = results.json()
# print(f"temperatura: {dict['main']['temp']}")
# print (f"wiatr: {dict['wind']['speed']} m/s")

######################################


# from bs4 import BeautifulSoup
# import requests
#
# page = requests.get('https://wallpaperlist.com/')
# # print(page.content)
#
# parser = BeautifulSoup(page.content, 'html.parser')
# images = parser.find_all('img')
# for image in images:
#     print (image['src'])

# zadanie
# 1. Sciagnij wszystkie obrazki ze strony glownej wallpapetlist.com do katalogu images
# 2. Zrob miniaturki obrazów w katalogu images/thumbs os szerokości  64px szerowkosci (wysokosc proporcjonalna)
# 3. policz ile jest zdjec na stronie
# 4. wyslij maila z informacja ile zdjec sciagnieto, jaki jest sumaryczny rozmiar zdjec w MB (i ile MB zaoszczedzilem robiac miniaturki)
# 6. dopisz w mailu jaka jest pogoda w Gdansku


#1.

from bs4 import BeautifulSoup
import requests
import os
pageurl = 'https://wallpaperlist.com/'
page = requests.get(pageurl)

parser = BeautifulSoup(page.content, 'html.parser')
images = parser.find_all('img')
licznik = 0
listaobr = []
for image in images:

    listaobr.append('https://wallpaperlist.com/' + image['src'])
    # print (image['src'])
    # print (licznik)
    print (listaobr[licznik])
    with open(where2save + image_name, 'wb') as file:
        file.write(img.content)
    licznik = licznik + 1

# print (listaobr)

