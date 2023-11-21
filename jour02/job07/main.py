chaine = "abcdefghijklmnopqrstuvwxyz" * 10

longueur_ligne = 1

while longueur_ligne <= len(chaine):

    print(chaine[:longueur_ligne])

    longueur_ligne += 2

    if longueur_ligne > len(chaine):
        break