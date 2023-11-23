nombres = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

def arrondir(nombre):
    partie_entiere = 0
    while partie_entiere <= nombre:
        partie_entiere += 1
    return partie_entiere - 1

liste_arrondie = [arrondir(nombre) for nombre in nombres]

taille_liste_nombre = 0
for elem in liste_arrondie:
    taille_liste_nombre += 1

i = 0
while i < taille_liste_nombre:
    j = 0
    while j < taille_liste_nombre - i - 1:
        if liste_arrondie[j] > liste_arrondie[j + 1]:
            liste_arrondie[j], liste_arrondie[j + 1] = liste_arrondie[j + 1], liste_arrondie[j]
            nombres[j], nombres[j + 1] = nombres[j + 1], nombres[j]
        j += 1
    i += 1

print("Liste arrondie de nombres triée en ordre croissant :", nombres)