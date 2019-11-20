import os
from random import randrange
from math import ceil

Continue = True
Bourse =1000

while Continue:
    numero_mise = 0
    while numero_mise <=0 or numero_mise > 49:
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

    ballhasard = randrange(50)
    print("....rien ne va plus...le numero gagnant et le ... ", ballhasard)

    if ballhasard == numero_mise:
        print("YYYYYYEESSSsssssssss !!!! les", mise,"que vous avez misé sont multipliez par trois. soit: ",mise * 3)
        Bourse += mise * 3
    elif ballhasard%2 == numero_mise %2:
        mise = ceil(mise/2)
        print("Couleur !!! vous ne recuperer que 50% de votre mise soit: ", mise )
        Bourse += mise
    else:
        print("bouhou !!! Ta perdu, rejoue encore si tes pas fauché tu va te refaire !!!")
        Bourse -= mise


    if Bourse <= 0:
        print("les jeux de hasard provoque des addiction,veuillez consultez ou en parlez a votre medecin. ah accessoirement vous etes fauchez ")

    else:
        print("money money money actuel :", Bourse)
        exit = input("allez !! on peut ce faire du bif appuie o pour continuer ou n'importe quel lettre pour prendre tes bifton chez toi ")
        if exit == "o" or exit == "O":
            Continue = False
os.system("pause")
