nombres = [10,20,30,20,10,50,60,40,80,50,40]
nombres_unique = []
for nombre in nombres:
  if nombre not in nombres_unique:
    nombres_unique += [nombre]
nombres = nombres_unique
print(nombres)
