# class Krzeslo():
# #     def __init__(self):
# #         # print ("Tworzę obiekt")
# #         self.kolor_siedziska = 'czerwony'
# #         self.ilosc_kol = 5
# #         self.wysokosc = '90'
# #         self.szerokosc = '40'
# #         self.glebokosc = '30'
# #         self.regulacja_wysokosci = True
# #         self.regulacja_podlokietnika = False
# #         self.material = '100% cotton'
# #         pass
# #
# # obiekt = Krzeslo()
# #
# # print (obiekt)
# # print (obiekt.material)
# #
# # obiekt = Krzeslo()
# #
# # print (obiekt)
# # print (obiekt.material)

class Krzeslo():
    def __init__(self, kolor_siedziska = "czerwony"):
        # print ("Tworzę obiekt")
        self.kolor_siedziska = kolor_siedziska
        self.ilosc_kol = 5
        self.wysokosc = '90'
        self.szerokosc = '40'
        self.glebokosc = '30'
        self.regulacja_wysokosci = True
        self.regulacja_podlokietnika = False
        self.material = '100% cotton'
        pass
    def __str__(self):
      return f'Krzesło koloru: {self.kolor_siedziska}'
obiekt = Krzeslo()
print (obiekt)
print (obiekt.kolor_siedziska)

obiekt = Krzeslo('niebieski')
print (obiekt)
print (obiekt.kolor_siedziska)