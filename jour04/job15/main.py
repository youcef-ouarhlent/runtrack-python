nombres = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
def arrondir(nombre):
    partie_entiere = int(nombre)
    partie_decimale = nombre - partie_entiere
    if partie_decimale >= 0.5:
        return partie_entiere + 1
    else:
        return partie_entiere

liste_arrondie = [arrondir(nombre) for nombre in nombres]
taille_liste_nombre = len(liste_arrondie)
for i in range(taille_liste_nombre):
    for j in range(0, taille_liste_nombre - i - 1):
        if liste_arrondie[j] > liste_arrondie[j + 1]:
            liste_arrondie[j], liste_arrondie[j + 1] = liste_arrondie[j + 1], liste_arrondie[j]
            nombres[j], nombres[j + 1] = nombres[j + 1], nombres[j]
print("Liste arrondie de nombres qui est triée en ordre croissant : ", nombres)