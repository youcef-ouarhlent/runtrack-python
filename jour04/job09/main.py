L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
longueur = len(L)


maximum = L[0]
minimum = L[0]
for i in range (longueur) :
     if L[i] > maximum :
          maximum = L[i]
     else :
          if L[i] < minimum :
               minimum = L[i]
print ("la valeur max est =", maximum)
print("la valeur min est = ", minimum)