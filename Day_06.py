# import csv
#
# imie = 0
# nazwisko = 1
# adres = 2
# telefon = 3
# wiek = 4
#
# with open('test.csv', 'r+',  encoding="utf8") as csv_file:
#     csv_data = csv.reader(csv_file)
#     wiek_suma = 0
#     for row in csv_data:
#         if (row[4].isdigit()):
#         # print(row)
#         # print(csv_data)
#         # print(row [wiek])
#             wiek = int(row [4])
#             wiek_suma = wiek_suma + wiek
#     print(wiek_suma)
#
# # print ("1111".isdigit())
# # print ("11.11".isdigit())
# # print ("ala".isdigit())
#     csv_write = csv.writer(csv_file)
#     csv_write.writerow(['Łukasz', 'Falkowicz','Gdańsk', '12313213', '18'])
# # =============
#
# import pickle
# entries = [
#     {"title": "Pierwszy wpis", "body": "Treść pierwszego wpisu","author": "Łukasz", "date" : "2019-11-08"},
#     {"title": "Drugi wpis", "body":  "Treść pierwszego wpisu","author": "Kasia", "date" : "2019-11-08"}
# ]
#
# with open('book.pkl', 'rb+') as book_file:
#     # pickle.dump(entries, book_file)
#     data = pickle.load(book_file)
#     print (data)

# ++++++++++++++
# 1. Pobierz dane od użytkownika
# 2. Utwórz słownik z wpisem
# 3. Pobierz listę starych wpisów
# 4. Dodaj słownik z wpisem do listy
# 5. Policz ilosc wpisów
# 6. zapisz listę z nowym wpisem
# 7. wyswietl ilosc wpisów
# 8. podziękuj uzytkownikowi i zamknij program
#
# *    - dodawanie w pętli
# **   - auto uzupełnianie daty
# ***  - wyszukiwanie
# **** - sortowanie


# import pickle
# title = input("Podaj tytuł:  ")
# body = input("Podaj tresc:  ")
# author = input("Podaj autora:  ")
# date = input("Podaj date:  ")
#
# # wpis = {"title": title, "body": body,"author": author, "date" : date}
# wpis = dict()
# wpis['title'] = title
# wpis['body'] = body
# wpis['author'] = author
# wpis['date'] = date
#
# with open('book.pkl', 'rb+') as book_file:
#     data = pickle.load(book_file)
#     # print (data)
# # calosc = [data,wpis]
# # print (calosc)
# # print (wpis)
# data.append(wpis)
# print (data)
#
#
# with open('book.pkl', 'rb+') as book_file:
#     pickle.dump(data, book_file)
#
# print("Liczba wpisów: " + (str(len(data))))
#
# print ("Dziękuje za współpracę")
# exit()

# *************************
# import pickle
# #1
# title = input ('Podaj tytuł:')
# body = input('Podaj tresc:')
# author = input('Podaj autora: ')
# #2
# new_entry = {"title": title, "body": body, "author": author, "date": "2019-11-07"}
# #3
# with open('book.pkl', 'rb+') as book_file:
#     old_entries = pickle.load(book_file)
# #4
#     old_entries.append(new_entry)
# #5
#     counter = len(old_entries)
# #6
#     book_file.seek(0)
#     pickle.dump(old_entries,book_file)
# #7
#     print (counter)
# #8
#     print('Dzięki')

# ______________________________
try:
    divsion = 10/0
    print (unresolved_variable)
except ZeroDivisionError:
    print (
        Nie dziel przez zero)
except NameError:
    print ('Brakuje zmiennej')
except
    print ('Nie wiem co się stało')