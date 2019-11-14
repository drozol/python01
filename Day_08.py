# days = ['poniedzielek','wtorek','sroda','czwartek','piatek','sobota','niedziela']
# weekend = ('sobota','niedziela')
#
# for day in days:
#     if day in weekend:
#         print ('Jest weekend')
#     else:
#         print ("Trzeba pracować")
#####################################

from PIL import Image

image : Image.Image = Image.open ('sheet.jpg')

# image.show()
image = image.resize ((4400,4200))
image = image.rotate(90)
image.save('sheet2.jpg')

import requests
# wp_page = requests.get('https://wp.pl')
# print (wp_page.text)

api_key = '800101cc05e0bcd5b88c816246c988ff'
api_host = 'http://api.openweathermap.org/data/2.5/weather'
city = 'Gdansk'

results = requests.get(f'{api_host}?appid={api_key}&q={city}')

dict = results.json()
print(f"temperatura: {dict['main']['temp']}")
print (f"wiatr: {dict['wind']['speed']} m/s")