nom="baguette"
prix=1
quantité_en_stock=1000
print("Le prix de la",nom,"est de",prix,"€","et il reste",quantité_en_stock,nom,".")
quantité_en_stock+=10
print("Après ajout on a maintenant",quantité_en_stock,nom,"en stock.")
quantite_achetee = int(input("Combien de baguette souhaitez-vous acheter ? "))
quantité_en_stock-=quantite_achetee
print(f"Vous avez acheté {quantite_achetee} unité(s) de {nom}.")
print("Ils nous restent",quantité_en_stock,nom,"en stock.")
prix*=1.1
print("Avec l'inflation de 10% le prix est passé à",prix,"€")
print("Le prix de la",nom,"est de",prix,"€","et il reste",quantité_en_stock,nom,".")
