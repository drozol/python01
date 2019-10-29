# 4. Napisz program do przeliczania liczby zapisanej w formacie binarnym na system dziesiętny.
podana_liczba =  input ("Podaj liczbę binarna: ")
dlugosc_liczby=len(podana_liczba)
# print(dlugosc_liczby)
licznik = 0
wynik = 0

while licznik != dlugosc_liczby:
    licznik1 = str(licznik)
    wynik = (2 ** licznik) + wynik
    licznik = licznik+1


print ("Liczba binarna " + str(podana_liczba) + " to dziesiętnie: " + str(wynik))