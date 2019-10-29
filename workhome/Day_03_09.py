# 9. Kalkulator do wyliczania wieku psa.
#    Przez pierwsze dwa lata, każdy psi rok to 10,5 ludzkiego roku, przez reszte lat psi rok to 4 ludzkie lata
#    Np: 15 ludzkich lat to 73 psie lata


dog_age = int(input ("Podaj wiek psa : "))
human_age = 0
if dog_age <= 2:
    print("Wiek psa " + str(dog_age) +" w ludzkich latach wynosi: "+ str(dog_age*10.5 ))

else:
    human_age=(21+ (dog_age-2)*4)
    print("Wiek psa " + str(dog_age) + " w ludzkich latach wynosi: " + str(human_age))