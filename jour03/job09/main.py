def moyenne(note1, note2, note3):
    return((note1+note2+note3)/3)
note1=(float(input("Veuillez saisir une première note:")))
note2=(float(input("Veuillez saisir une seconde note:")))
note3=(float(input("Veuillez saisir une troisième note:")))
moyenne_etudiant = moyenne(note1, note2, note3)

print("La moyenne de l'étudiant est :", moyenne_etudiant)

if 15 <= moyenne_etudiant <= 20:
    print("Très bon élève")
elif 11 <= moyenne_etudiant <= 14:
    print("Bon élève")
elif 8 <= moyenne_etudiant <= 10:
    print("Élève moyen")
elif 0 <= moyenne_etudiant <= 7:
    print("Élève devant faire des efforts")
else:
    print("La moyenne n'est pas compris à l'intérieur ")
