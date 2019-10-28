# 1. Napisz program do przeliczania stopni Celsjusza na Fahrenheita i odwrotnie (wyświetlając wzór i kolejne obliczenia)

rodzaj = input ("Jakie stopnie będziesz podwał do przeliczenia Fahrenheit / Celsjusz wpisz F lub C - ")
temperatura =  float(input ("Podaj liczbę stopni: "))

if rodzaj == 'F':
    print("Przeliczamy stopnie Farenhaita na Celsjusza")
    print("Konwersja z Fahrenheita do Celsjusza ℃ = ((℉ - 32) / 1.8) ")
    wynik = float ((temperatura - 32) /1.8)
    print (wynik)

else:
    print("Przeliczamy stopnie Celsjusza na Farenhaita")
    print("Konwersja z Celsjusza do  ℉ =((℃ *1.8) + 32)")
    wynik = float ((temperatura * 1.8) + 32)
    print (wynik)