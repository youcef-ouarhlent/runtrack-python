def my_long_word(chiffre, chaine_de_caractere):
    phrases = chaine_de_caractere.split()
    phrases_filtres = [phrase for phrase in phrases if len(phrase) > chiffre]
    exemple = ' '.join(phrases_filtres)
    return exemple
exemple = my_long_word(3, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance")
print("Output :", exemple)
