# Napisz program, który poda pierwszą i ostatnią cyfrę podanej liczby
podana_liczba =  input ("Podaj liczbę : ")
dlugosc_liczby=len(podana_liczba)
ostatni_znak=dlugosc_liczby-1
# print(dlugosc_liczby)
print ("Pierwszy znak liczby to: "+podana_liczba[0])
print ("Ostatni znak liczby to: "+podana_liczba[ostatni_znak])
