def arrondir_notes(notes):
    arrondies = []
    for note in notes:
        if note >= 40 and note < 97:
            next_multiple_of_5 = round(note / 5) * 5 + (5 if note % 5 >= 3 else 0)
            arrondies.append(next_multiple_of_5)
        else:
            arrondies.append(note)
    return arrondies
liste_notes = [32, 45, 83, 72, 91]
resultat = arrondir_notes(liste_notes)
print(resultat)