def draw_rectangle(width, height): 
    rectangle=""
    for h in range(height):
        line="|"
        if h == 0 or h == height -1:
            line +="-" * (width-2) + "|"
        else:
            line += " " * (width-2) + "|"
        rectangle += line +"\n"
    print(rectangle)
draw_rectangle(10, 3)