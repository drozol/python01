# 1. Napisz program do przeliczania stopni Celsjusza na Fahrenheita i odwrotnie (wyświetlając wzór i kolejne obliczenia)

rodzaj = input ("Jakie stopnie będziesz podqwał do przeliczenia Fahrenheit / Celsjusz wpisz F lub C - ")
temperatura =  float(input ("Podaj liczbę stopni: "))

if rodzaj == 'F' or rodzaj =='f':
    print("Przeliczamy stopnie Farenhaita na Celsjusza")
    print("Konwersja z Fahrenheita do Celsjusza ℃ = ((℉ - 32) / 1.8) ")
    wynik = float ((temperatura - 32) /1.8)
    print (str(temperatura) + " stopni Farenhaita to " + str(wynik) + " stopni Celsjusza")
elif rodzaj == 'C' or rodzaj =='c':
    print("Przeliczamy stopnie Celsjusza na Farenhaita")
    print("Konwersja z Celsjusza do  ℉ =((℃ *1.8) + 32)")
    wynik = float ((temperatura * 1.8) + 32)
    print(str(temperatura) + " stopni Celsjusza to " + str(wynik) + " stopni Farenhaita")
else:
    print ("Podałeś błędnie parametry")