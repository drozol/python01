# 8. Program rysujący piramidę o określonej wysokości, np dla 3
      #
     ###
    #####

wysokosc = int(input ("Podaj liczbę stopni piramidy piramidy : "))
licznik = 1
liczba_spacji = wysokosc
liczba_hashy = licznik

# print ((((wysokosc-1)*" 7")+"#"))
while licznik != wysokosc:
    liczba_spacji = liczba_spacji - 1
    # print((((liczba_spacji) * " ") + ((liczba_hashy) * "#")) + str(liczba_hashy) + str(liczba_spacji))
    print((((liczba_spacji) * " ") + ((liczba_hashy) * "#")))
    licznik = licznik+1
    liczba_hashy = liczba_hashy + 2
liczba_spacji = liczba_spacji - 1
print((((liczba_spacji) * " ") + ((liczba_hashy) * "#")))