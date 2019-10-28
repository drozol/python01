# 3. Napisz program, który rysuje prostokąt o zadanych rozmiarach (wysokość i szerokość) za pomocą znaków | (bok) - (góra/dół) + (wierzchołek)

wysokosc = int(input ("Podaj wysokość prostokąta : "))
szerokosc = int(input ("Podaj szerokość prostokąta : "))
licznik = 0



print ("+"+((szerokosc-2)*"-")+"+")
while licznik != wysokosc:
    print ("|" + ((szerokosc - 2) * " ") + "|")
    # print (szerokosc*"-")
    licznik = licznik+1
print ("+"+((szerokosc-2)*"-")+"+")
