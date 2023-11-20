montant_investissement_initial=1500
taux_de_rendement_annuel=1.5
print(montant_investissement_initial*taux_de_rendement_annuel-montant_investissement_initial)
montant_investissement_initial+=5000
taux_de_rendement_annuel+=0.02
print (montant_investissement_initial * taux_de_rendement_annuel -montant_investissement_initial)
montant_investissement_initial *= 0.9
taux_de_rendement_annuel -= 0.01
print("Le montant final de l'investissement est de",montant_investissement_initial)
print ("Le gain final en fonction du taux de rendement est de",montant_investissement_initial *taux_de_rendement_annuel - montant_investissement_initial)