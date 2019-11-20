import os
import random

Continue = True
Bourse =1000

while Continue:
    numero_mise = 0
    while mise <0 or mise > 49:
        numero_mise= input("choisi entre 0 et 49 le numero ou tu mise")
        numero_mise=int(numero_mise)
        if numero_mise < 0 or numero_mise > 49:
            print("ce nombre n'est pas compris entre 0 et 49")
    mise = 0
    while mise <= 0 or mise > Bourse:
        mise = input("mettez le montant à parié")
        mise = int(mise)

        if mise <= 0 or mise > Bourse:
            print("vous ne pouvez pas miser plus que vous avez et la maison ne fait pas credit !!!")
        
