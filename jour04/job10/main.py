L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
longueur = len(L)
produit = 1
for i in range (0, longueur) :
     if 25 <= L[i] <= 90 :
          produit = produit*L[i]
print ("Le produit des valeurs comprises entre 50 et 70 est :", produit)