def time_to_text(minutes):
    if  minutes < 0:
        print("Veuillez entrer un nombre entier positif de minutes.")
        return
    heures = minutes // 60
    minutes_restantes = minutes % 60
    if heures == 0:
        print(f"{minutes} minutes")
    elif minutes_restantes == 0:
        print(f"{heures} heures")
    else:
        print(f"{heures} heures et {minutes_restantes} minutes")
time_to_text(120)
time_to_text(70)
time_to_text(55)
time_to_text(0)
time_to_text(-100)