import turtle

start_positions = input("Enter a starting position: ") 
width = int(input("Enter your width "))
height = int(input("Enter the height: "))
pos = start_positions.split(",")
startX = int(pos[0])
startY = int(pos[1])
hoeb = height / 8
woeb = width / 8




turtle.penup()
turtle.goto(startX, startY) 
turtle.pendown()
turtle.right(270)
turtle.forward(width)
turtle.right(270)
turtle.forward(height)
turtle.right(270)
turtle.forward(width)
turtle.right(270)
turtle.forward(height) 

    
    
turtle.penup()
turtle.goto(startX, startY)
turtle.right(270)
turtle.pendown()

box_count = 0
while box_count <= 3:
   
    turtle.begin_fill()
    turtle.forward(woeb)
    turtle.right(270)
    turtle.forward(hoeb)
    turtle.right(270)
    turtle.forward(woeb)
    turtle.right(270)
    turtle.forward(hoeb)
    turtle.end_fill()
    turtle.right(180)
    turtle.forward(2 * woeb)
    box_count += 1

rows = 0
while rows <= 3:

    turtle.right(270)
    turtle.forward(2 * hoeb)
    box_count = 0
    while box_count <= 3:
   
        turtle.begin_fill()
        turtle.forward(hoeb)
        turtle.right(270)
        turtle.forward(woeb)
        turtle.right(270)
        turtle.forward(hoeb)
        turtle.right(270)
        turtle.forward(woeb)
        turtle.end_fill()
        turtle.right(270)
        turtle.forward(2 * woeb)
        box_count += 1

turtle.done()






