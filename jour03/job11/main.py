def time_to_text(minutes):
    if  minutes < 0:
        print("Veuillez entrer un nombre entier positif de minutes.")
        return
    heures = minutes // 60
    minutes_heures = minutes % 60
    if minutes_heures == 0:
        print(f"{heures} heures")
    elif heures == 0:
        print(f"{minutes} minutes")    
    else:
        print(f"{heures} heures et {minutes_heures} minutes")
time_to_text(120)
time_to_text(70)
time_to_text(55)
time_to_text(0)
time_to_text(-100)