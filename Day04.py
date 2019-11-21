# lista = [1, 2, 3]
#
# nowa_lista = lista
# lista [0] = 'X'
#
# print(lista)
# print(nowa_lista)
# ===============

# lista = [1, 2, 3]
# nowa_lista = lista
# kopia_listy = lista.copy()
#
# lista [0] = 'X'
#
# print(lista)
# print(nowa_lista)
# print(kopia_listy)
# # ===============
# lista = [1,
#          2,
#          3,
#          ['A', 'B', 'C']
#     ]
# nowa_lista = lista
# lista[0] = 'X'
# lista [3][0] = 'Y'
#
# print(lista)
# print(nowa_lista)
# # print(kopia_listy)
# # ===============
# lista = [1,
#          2,
#          3,
#          ['A', 'B', 'C']
#     ]
# nowa_lista = lista
# kopia_listy = lista.copy() # Nie robi kopi listy zagnieżdżonej
# lista[0] = 'X'
# lista [3][0] = 'Y'
#
# print(lista)
# print(nowa_lista)
# print(kopia_listy)
# ===============
# import copy # !!! Import
# lista = [1,
#          2,
#          3,
#          ['A', 'B', 'C']
#     ]
# nowa_lista = lista
# kopia_listy = lista.copy() # Nie robi kopi listy zagnieżdżonej
# gleboka_kopia_listy = copy.deepcopy(lista) # robi kopię listy na wszystkich poziomach
# lista[0] = 'X'
# lista [3][0] = 'Y'
#
# print(lista)
# print(nowa_lista)
# print(kopia_listy)
# print(gleboka_kopia_listy)
# # ===============
# def witaj():
#     print('Cześć, jestm Twoim nowym programem')
# witaj()
#
# hi = witaj
# hi()
# ===============
# def witaj():
#     print('Cześć, jestm Twoim nowym programem')
#
# hi = witaj()
# print (hi)
# ===============
# def witaj():
#     print('Cześć, jestm Twoim nowym programem')
#
# hi = witaj
# print (hi)
# ===============
# def do_nothing (x, y, imie = "Ola", wiek=22):
#     pass
#
# # do_nothing(1)
# # do_nothing(1, 2, "iza")
# # do_nothing(1, 2, "iza", 22)
# # do_nothing(1, 2, imie="iza", 22)
# # do_nothing(1, 2, imie="iza", wiek=22)
# do_nothing(wiek=22, imie="Iza", x=1, y=2)
# ===============

# imie = "Jola"
# def zmien_imie():
#     imie = "Teresa"
# print (imie)
# zmien_imie()
# print(imie)
# ===============
# imie = "Jola"
# def zmien_imie():
#     imie = "Teresa"
#     return imie
# print (imie)
# zmien_imie()
# print(imie)
# ===============
# imie = "Jola"
# def zmien_imie():
#     imie = "Teresa"
#     return imie
# print (imie)
# imie = zmien_imie()
# print(imie)
# ===============
# imie = "Jola"
# def zmien_imie():
#     imie = "Teresa"
#     return [imie, "jan"]
# print (imie)
# imie = zmien_imie()
# print(imie)
# ===============

# def zmien_imie(imie):
#     if imie == "Teresa":
#         return 'To twoje imie'
#     else:
#         return False
# imie = zmien_imie('Teresa')
# print(imie)

# ===============

dane = "215021482120211921002076207620502065202020152010200520002001199319901950183417501744186019462010"
for godzina in range (0,24):
    poczatek_zakresu = godzina * 4
    koniec_zakresu = godzina + 4
    print(poczatek_zakresu)
    print(koniec_zakresu)
    temp = int(dane [poczatek_zakresu:koniec_zakresu])/100
    tab = ""

    if temp <= 20:
        tab = "\t!"
    elif temp <= 18.5:
        tab = "\t!!"
    wiersz_sting = f"{godzina}:00:\t {temp} \u00b0C{tab}"
    print (godzina)

    print (wiersz_sting)