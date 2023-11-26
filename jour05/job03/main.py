def triangle(hauteur):
    for i in range(1, hauteur + 1):
        espaces = ' ' * (hauteur - i)
        if i == 1:
            print(espaces + '_')
        else:
            ligne = espaces + '/' + '_' * (2 * i - 3) + '\\'
            print(ligne)
hauteur = int(input("Tapez la hauteur du triangle : "))
triangle(hauteur)