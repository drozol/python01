contacts = {"names": ['Ala','Ola','Jan'],
            "surnames": ['Kowalska','Malinowsk','Igrekowski'],
            "cities": ['Gdańsk', 'Sopot', 'Gdynia']
            }
# print(contacts)
# print(type(contacts))
# print(contacts['cities'])
# ===============
# print(contacts['cities'])
# contacts['cities'].append("Rumia")
# print(contacts['cities'])
#
contacts.update({'countries': ['Polska', 'USA', 'Dania']})
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

for key, value in enumerate(contacts['names']):
    # print(key)
    # print(value)
    name = value
    surname = contacts['surnames'][key]
    city = contacts['cities'][key]
    country = contacts['countries'][key]
    print (f"{name} {surname} mieszka w {city} ({country})")