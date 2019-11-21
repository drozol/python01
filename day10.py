class A():
   def hi(self):
       print('A')
class B(A):
    def hi(self):
        print('B')
class C(A):
    def hi(self):
        print('C')
class D(B,C):
    def hi(self):
        print('D')

D().hi()
B().hi()
C().hi()
A().hi()


# class Zwierze():
#     def __init__(self):
#         self.oczy = 2
#         self.wlosy = True
#     def __str__(self):
#         return f'Oczy: {self.oczy}, wlosy: {self.wlosy}'
#     pass
# class Czlowiek(Zwierze):
#     def dajglos(self):
#         print("HAHA")
# class Kot(Zwierze):
#     def dajglos(self):
#         print("Mial")
# class Pies(Zwierze):
#     def dajglos(self):
#         print("HAUHAU")
# class Student(Czlowiek):
#     def dajglos(self):
#         print("Siema daj piataka")
# class Bokser(Pies):
#     pass
# class Jamnik(Pies):
#     pass
# class Dresiarz (Czlowiek):
#     def __init__(self):
#         super().__init__()
#     def dajglos(self):
#         super().dajglos()
#         print('Masz jakis prolem?')
#
# # zwierze = Zwierze()
# # czlowiek = Czlowiek()
# # czlowiek.dajglos()
# # pies = Pies()
# # pies.dajglos()
# # kot = Kot()
# # kot.dajglos()
# # jamnik = Jamnik()
# # jamnik.dajglos()
# # print(jamnik.oczy)
#
# dresiarz = Dresiarz()
# dresiarz.dajglos()
# print("Nie mam:P")
# print(dresiarz)
# # class Stol():
# #     def __init__(self):
# #         self.ilosc_nog = 4
# #     def __add__(self, other):
# #         return self.ilosc_nog + other.ilosc_nog
# #
# # class Krzeslo():
# #     def __init__(self, kolor_siedziska = "czerwony"):
# #         self.kolor_siedziska = kolor_siedziska
# #         self.ilosc_kol = 5
# #         self.wysokość = 90
# #         self.szerokosc = 40
# #         self.glebokosc = 40
# #         self.regulacja_wyskosci = True
# #         self.regulacja_podlokietnikow = False
# #         self.cena = 111
# #         self.vat = 23
# #         self.material = '100% cotton'
# #         self.ilosc_nog = 5
# #
# #     def __str__(self):
# #         return f'Krzesło koloru: {self.kolor_siedziska}'
# #
# #     def __len__(self):
# #         return self.wysokość * self.szerokosc * self.glebokosc
# #
# #     def pobierz_cene_netto(self):
# #         return self.cena
# #
# #     def pobierz_cene_brutto(self):
# #         return self.cena * (1 + self.vat/100)
# #
# # krzeslo = Krzeslo()
# # print(krzeslo)
# # stol = Stol()
# # print(Stol)
# #
# # print (stol + krzeslo)
# # # obiekt = Krzeslo('niebieski')
# # # print(obiekt)
# # # print(len(obiekt))
# # # print(obiekt.kolor_siedziska)
# # # print (obiekt.pobierz_cene_netto())
# # # print (obiekt.pobierz_cene_brutto())