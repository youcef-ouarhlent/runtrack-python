nombres = [10,20,30,20,10,50,60,40,80,50,40]
nombres_unique = []
for nombres in nombres:
  if nombres not in nombres_unique:
    nombres_unique.append(nombres)

print(nombres_unique)
