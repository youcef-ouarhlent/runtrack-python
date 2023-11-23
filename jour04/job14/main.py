def my_long_word(nombre,  chaine_de_caractere):
    mots =  chaine_de_caractere.split()
    resultat = ""
    for mot in mots:
        mot_length = 0
        for char in mot:
            if char.isalpha():  
                mot_length += 1
        
        if mot_length > nombre:
            resultat += mot + " "
    return resultat.strip()  

output = my_long_word(3, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance")
print("Output:", output)