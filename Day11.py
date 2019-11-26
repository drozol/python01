# import datetime
# import pprint
# class Pizza():
#     stawka_vat=23
#     __marza = 1.05
#     def __init__(self, skladnik_glowny = None):
#         self.skladnik_glowny = skladnik_glowny
#         self.rozmiar_cm = 30
#         self.ciasto = 'cienkie'
#         self.cena = 23 * self.__marza
#     @classmethod
#     def Hawajska(cls):
#         return cls('ananas')
#
#     @classmethod
#     def Farmerska(cls):
#         return cls('kielbasa')
#
#     @classmethod
#     def podaj_stawke_vat(cls):
#         return cls('23')
#
#     @staticmethod
#     def podaj_date():
#         return datetime.datetime.now().strftime('%Y-%d-%m')
# # hawajska = Pizza('ananas')
# # print (hawajska.skladnik_glowny)
# # hawajska = Pizza.Hawajska()
# # print(hawajska.skladnik_glowny)
# # inna_pizza = Pizza.Farmerska()
# # print(inna_pizza.skladnik_glowny)
# # print(Pizza.podaj_stawke_vat())
# # print(Pizza.stawka_vat)
# # print(Pizza.podaj_date())
#
# # print(Pizza.stawka_vat)
# # # print(Pizza.cena)
# # pizza = Pizza()
# # print(pizza.cena)
# # print(Pizza.__dict__)
#
#
# class Student():
#     def __init__(self):
#         self.__imie = None
#         self.nazwisko = None
#         self.data_dodania = None
#         self.data_usuniecia = None
#         self.skasowany = False
#
#     @property
#     def imie(self):
#         print('org: ' + self.__imie)
#         return self.__imie.capitalize()
#     @imie.setter
#     def imie(self, wartosc):
#         self.__imie = wartosc
#     @imie.deleter
#     def imie(self):
#         self.skasowany = True
#         self.data_usuniecia = self.pobierz_date()
#     @staticmethod
#     def pobierz_date():
#         return datetime.datetime.now().strftime('%Y-%d-%m')
# student = Student()
# student.imie = 'daniel'
# student.nazwisko = 'drozd'
# student.data_dodania = Student.pobierz_date()
#
# print(student.imie)
# print(student.nazwisko)
# print(student.data_dodania)
# print(student.data_usuniecia)
# del (student.imie)
# print(student.data_usuniecia)
#
# ###################################