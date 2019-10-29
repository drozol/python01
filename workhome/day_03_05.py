# 5. Napisz program do sprawdzania czy podany rok jest rokiem przestępnym


rok = int(input ("Podaj rok w celu sprawdzenia czy jest rokiem przestępnym: "))

if (((rok % 4 == 0) and (rok % 100 != 0)) or (rok % 400 == 0)):
      print("Rok " + str(rok) + " jest rokiem przestępnym")
else:
    print("Rok " + str(rok) + " nie jest rokiem przestępnym")