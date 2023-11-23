L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
longueur = len(L)
somme = 0
for i in range (longueur) :
     if L[i] %2 == 0 :
          somme = somme + L[i]
print ("Somme des valeurs paires : ", somme)