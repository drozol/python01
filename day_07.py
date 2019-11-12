# import myModule
# myModule.hello()

# ---------------

# import myModule
# from myModule import hello
# myModule.hello()
# hello()
#########################

# import myModule
# from myModule import hello
# def hello():
#     print("Dzień dobry")
#
# myModule.hello()
# hello()
#############################

# import myModule
# from myModule import hello as helloFromModule
# def hello():
#     print("Dzień dobry")
#
# myModule.hello()
# hello()
# helloFromModule()

#########################

#
# import modules.otherModule as otherModule
# otherModule.add(1,2,45,12)
# print(otherModule.add(1,2,45,12))

# -------------------



# import os
# import send2trash
# filename = os.getcwd()+"\\file2bedeleted2.txt"
# print(filename)
# with open(filename, 'w+') as book_file:
#     print("File was created")
# send2trash.send2trash(filename)

# import os
# os.system('notepad.exe') #uruchomienie programu

#
# login: isapy@int.pl
# pass: isapython;
# serwer: poczta.int.pl
# uwierzytelnianie: SSL

#######################

# wysyałka maila
# 1. import bibliotek

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

subject = input("Podaj temat: ")
body = input("Podaj treść maila: ")
recipient = input("Podaj adresata: ")
mail_body = MIMEText(body)
mail = MIMEMultipart()
mail["Subject"] = subject
mail["From"] = "isapy@int.pl"
mail["To"] = recipient
mail.attach(mail_body)

server = smtplib.SMTP("poczta.int.pl")
server.starttls()
server.login("isapy@int.pl", "isapython;")
server.send_message(mail)
server.quit()
