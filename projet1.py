
'''
Author: MINOU
Date: Octobre 2022

But du jeu ?

Le jeu se joue avec des billes entre un joueur et un ordinateur doté d'une IA. Le nombre de billes
initial est déterminé par le joueur, à tour de rôle un nombre de bille de 1, 2, 3 ou 4 bille(s) va être retiré.
Celui qui retire la dernière bille du sac perd la partie.

'''


import sys
import messages
import random
from random import randint, seed


sys.path.append('/pub/code')

print(messages.message_1)
graine = int(input(messages.entree_1))
seed(graine)
replay = True  #Pour que la boucle se répète si le joueur veut rejouer

print(messages.message_2)
count_billes = int(input(messages.entree_2)) #Nombre de bille initial convenu par le joueur
print(messages.message_3)

while replay == True:
    round_player = 1 #Représente le tour du joueur 1 = Tour du joueur
    if round_player == 1: #Tour Joueur

        print(messages.message_4.format(count_billes))
        ball_player = int(input(messages.entree_3)) #Nombre de bille que le joueur veut retirer
        count_billes = count_billes - ball_player
        if count_billes !=1:
            print(messages.message_5.format(count_billes))
        round_player = 0 #Représente le tour de l'ordinateur 0 = Tour de l'ordinateur

        if count_billes == 1: #Nombre de bille = 1 la partie s'arrête et désigne un gagnant
            print(messages.message_8)
            again = input(messages.entree_4) #Volonté du joueur de rejouer une partie
            if again == "oui":
                print(messages.message_2)
                count_billes = int(input(messages.entree_2))
                print(messages.message_3)
                round_player = 1
            else:
                break

    if count_billes !=1 and round_player == 0:
        print(messages.message_6)

    if round_player == 0: #Tour de l'IA
        aleatoire = random.randint(1,100)
        if (count_billes - 1) % 5 ==0:
            if count_billes >= 7 and aleatoire <= 70:
                count_billes = count_billes - 1
                ia = 1
                print(messages.message_7.format(ia))
            elif count_billes >= 7 and aleatoire >70:
                count_billes= count_billes - 2
                ia = 2
                print(messages.message_7.format(ia))
            else:
                count_billes = count_billes - 1
                ia = 1
                print(messages.message_7.format(ia))

        else:
            ia = (count_billes - 1) % 5 #L'ordinateur va chercher un multiple de 5 + 1 grâce à cette opération
            count_billes = count_billes - ia
            print(messages.message_7.format(ia))

        if count_billes == 1: #Nombre de bille = 1 la partie s'arrête et désigne un gagnant
            print(messages.message_9)
            again = input(messages.entree_4) #Volonté du joueur de rejouer une partie
            if again == "oui":
                print(messages.message_2)
                count_billes = int(input(messages.entree_2))
                print(messages.message_3)
                round_player = 1
            else:
                break
