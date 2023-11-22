def calcule(num1, operator, num2):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    elif operator == "%":
        result = num1 % num2    
    else:
        result = "Opérateur non valide"
    
    print(f"{num1} {operator} {num2} = {result}")

calcule(7, "+", 8)
calcule(6,"-", 3)
calcule(12,"/", 6)
calcule(6,"%", 70)