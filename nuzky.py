import random
import os

bodyHrac = 0

bodyPc = 0

while True:

    volby = ['kámen','nůžky','papír']
    nahodne_cislo = random.randint(0,2)

    vstup_uzivatele = input("Zadejte vaší volbu")


    if volby[nahodne_cislo] == vstup_uzivatele.lower():
        print("Nerozhodné")
        pass
    elif volby[nahodne_cislo] == "nůžky" and vstup_uzivatele.lower() == "papír":
        bodyPc = bodyPc+1
        pass