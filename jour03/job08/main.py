def types_saisons(type,saison):
    if type == "fruits" and saison == "hiver" :
        print("orange, mandarine et kiwi")
    elif type == "fruits" and saison == "ete" :
        print("Poire, fraise, cassis")
    elif type == "legume" and saison == "hiver" :
        print("carotte, topinambour, endive")
    elif type == "legume" and saison == "ete" :
        print("artichaut, aubergine,navet")
    else :
        print("Fruits et légumes différents")      
types_saisons("fruits","hiver")   
types_saisons("fruits","ete") 
types_saisons("legume","hiver") 
types_saisons("legume","ete") 
types_saisons("fruits","printemps")      