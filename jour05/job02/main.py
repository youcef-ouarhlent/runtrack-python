def draw_rectangle(width, height):
    if width < 4 or height < 1:
        print("Pour dessiner correctement un rectangle la largeur et la hauteur doivent être en proportion l'une avec l'autre.")
        return
    horizontal_line = '-' * (width - 2)
    print('|' + horizontal_line + '|')  
    for _ in range(height - 2):
        print('|' + ' ' * (width - 2) + '|')  
    print('|' + horizontal_line + '|')  
draw_rectangle(10, 3)