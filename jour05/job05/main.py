def cesar(msg="", clé=0): 
	alphabet="abcdefghijklmnopqrstuvwxyz" 
	chiffre="" 
  
	# On prend chaque lettre du mot (converti en minuscules) 
	for l in msg.lower(): 
		# On recherche la position de la lettre dans l'alphabet 
		pos=alphabet.find(l) 
  
		# Si la lettre est présente 
		if pos != -1: 
			# On récupère la lettre décalée dans l'alphabet (on boucle si dépassement) 
			chiffre+=alphabet[(pos+clé) % len(alphabet)] 
		else: 
			# Sinon on prend la lettre originelle 
			chiffre+=l 
		# if 
	# for 
	return chiffre 
# cesar() 
  
message="Bonjour" 
chiffre=cesar(message, 5) 
dechiffre=cesar(chiffre, -5) 
print(message, "=>", chiffre, "=>", dechiffre)