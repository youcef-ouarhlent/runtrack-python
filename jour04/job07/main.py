L = [8, 24, 48, 2, 16]
longueur = len(L)
multiplicationde3 = 0
for i in range (longueur) :
     if L[i] %3 == 0 :
          multiplicationde3 = multiplicationde3 + 1
print ("Nombre de multiples de 3 : ", multiplicationde3)