def count_elements(array):
    count = 0
    for _ in array:
        count += 1
    return count

def tri_insertion(nombres):
    i = 1
    array_length = count_elements(nombres)
    while i < array_length:
        valeur_actuelle = nombres[i]
        position = i

        while position > 0:
            if nombres[position - 1] > valeur_actuelle:
                nombres[position] = nombres[position - 1]
                position -= 1
            else:
                break

        nombres[position] = valeur_actuelle
        i += 1
nombres = [3, 5, 4, 2, 1]
tri_insertion(nombres)
print(nombres)