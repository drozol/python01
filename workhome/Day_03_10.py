# 10. Zmienna dane zawiera 24 odczyty temperatury z 24 godzin. Każde 4 znaki to jeden odczyt w setnych stopni Celsjusza, tzn "2150" to 21.50°C Pomiary są dokonane o pełnych godzinach od 00:00 do 23:00. Wypisz do konsoli raport w formacie:
#
# <godzina>:<tabulator><stopnie z dokładnością do drugiego miejsca po przecinku><znak stopni>C
#
# Dla odczytów niższych niż lub równych 20°C dodaj "<tabulator>!" Dla odczytów niższych niż lub równych 18,5°C dodaj dodatkowy wykrzyknik. Nie kopiuj proszę znaku stopni. Spróbuj użyć znaku unicode \u00b0.
#
# dane = "215021482120211921002076207620502065202020152010200520002001199319901950183417501744186019462010"
# Przykład wyniku:
# (...)
# 20:00:  17.44°C    !!
# 21:00:  18.60°C    !
# 22:00:  19.46°C    !
# 23:00:  20.10°C
# (...)

dane = "215021482120211921002076207620502065202020152010200520002001199319901950183417501744186019462010"
odczyty = ['00:00','01:00','02:00','03:00','04:00','05:00','06:00','07:00','08:00','09:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','18:00','19:00','20:00','21:00','22:00','23:00']
dlugosc = len(dane)
ilosc_pomiarow = dlugosc/4
licznik = 0
licznik_godzin = 0
temperatura = 0
while licznik != dlugosc:
    temperatura = float (((dane[licznik:(licznik+2)]) + "." + (dane[(licznik+2):(licznik+4)])))
    if temperatura <= 18.5:
        print(((odczyty [(licznik_godzin)]) + ":" + "\t" +((dane[licznik:(licznik+2)]) + "." + (dane[(licznik+2):(licznik+4)]))) + "\u00b0C\t!!" )
    elif temperatura >18.5 and temperatura <= 20:
        print(((odczyty [(licznik_godzin)]) + ":" + "\t" +((dane[licznik:(licznik+2)]) + "." + (dane[(licznik+2):(licznik+4)]))) + "\u00b0C\t!" )
    else:
        print(((odczyty [(licznik_godzin)]) + ":" + "\t" +((dane[licznik:(licznik+2)]) + "." + (dane[(licznik+2):(licznik+4)]))) + "\u00b0C\t" )

    licznik = licznik + 4
    licznik_godzin = licznik_godzin + 1


