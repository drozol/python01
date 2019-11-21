# contacts = {"names": ['Ala','Ola','Jan'],
#             "surnames": ['Kowalska','Malinowsk','Igrekowski'],
#             "cities": ['Gdańsk', 'Sopot', 'Gdynia']
#             }
# print(contacts)
# print(type(contacts))
# print(contacts['cities'])
# ===============
# print(contacts['cities'])
# contacts['cities'].append("Rumia")
# print(contacts['cities'])
#
# contacts.update({'countries': ['Polska', 'USA', 'Dania']})
# contacts['countries'] = ['Polska', 'USA', 'Dania']
#
# print(contacts.keys)
# print(contacts.values())
# print(contacts.items())
# print(list(contacts))
# ============
# "Ala Kowalska mieszka w Gdańsk (Polska)
# "Ola Malinowska mieszka w Sopot (USA)
# "Jan Igrekowski mieszka w Gdynia (Dania)

# for key, value in contacts.items():


# print (len(contacts))
# print (contactsw[1][2])

# for key, value in enumerate(contacts['names']):
#     # print(key)
#     # print(value)
#     name = value
#     surname = contacts['surnames'][key]
#     city = contacts['cities'][key]
#     country = contacts['countries'][key]
#     print (f"{name} {surname} mieszka w {city} ({country})")


# contacts ={
#         '0': {"name": "Ala", "surname": "Kowlaska", "cities": "Gdańsk"},
#         '1': {"name": "Ola", "surname": "Malinowska", "cities": "Gdynia"},
#         '2': {"name": "Jan", "surname": "Igrekowski", "cities": "Rumia"}
# }
#
# for key in (contacts):
#     # print (key)
#     # print(contacts[key]["name"])
#     # print(contacts[key]["surname"])
#     # print(contacts[key]["cities"])
#
#     imie = contacts[key]["name"]
#     nazwisko = contacts[key]["surname"]
#     miasto = contacts[key]["cities"]
#
#     print (f"{imie} {nazwisko} mieszka w {miasto}")
# ======
# contacts = [
#     {"name": "Ala", "surname": "Kowlaska", "cities": "Gdańsk"},
#     {"name": "Ola", "surname": "Malinowska", "cities": "Gdynia"},
#     {"name": "Jan", "surname": "Igrekowski", "cities": "Rumia"}
# ]
#
# for rows in contacts:
#     # print (rows)
#     # print (rows["name"])
#     name = rows ['name']
#     surname = rows ["surname"]
#     city = rows ['cities']
#     print(f"{name} {surname} mieszka w {city}")
# ============

# file = open ('file.txt', 'r') # otwrie istniejącego pliku do odczytu
# file = open ('file.txt', 'w') # 'w' czysi plik i go otwiera, 'a' dodaje do pliku
# file.write("Zapisz do pliku jeszcze raz i jeszcze raz")
# file.writelines(['wiersz1' , 'wiersz2'])
# file.writelines(['\nwiersz1' , '\nwiersz2'])
# print(file.tell()) #pokazuje wertość kursora w pliku
# file.seek(10) #ustawienie kursora
#
# file.close()

# ============

# with open ('file1.txt', 'a+', encoding="utf8") as file:
#     file.write('Zapisz proszę.\n')
#     file.write('I jeszcze raz.\n')
#     file.write('I kolejny raz\n')
#===================================

with open ('file1.txt', 'w+', encoding="utf8") as file:
file
