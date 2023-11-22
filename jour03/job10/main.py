def nombre_pair_impair(nombre):
    if not isinstance(nombre, int) or nombre < 0:
        print("Veuillez entrer un nombre entier positif.")
        return
    
    if nombre % 2 == 0:
        print(f"Le nombre {nombre} est pair.")
    else:
        print(f"Le nombre {nombre} est impair.")
nombre_pair_impair(9)
nombre_pair_impair(22)
nombre_pair_impair(-14)
nombre_pair_impair(19.5)