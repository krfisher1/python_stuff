import turtle

start_positions = input("Enter a starting position: ") 
width = int(input("Enter your width "))
height = int(input("Enter the height: "))
pos = start_positions.split(",")
startX = int(pos[0])
startY = int(pos[1])


def big_box():

    height_of_each_box = height / 8
    width_of_each_box = width / 8

    turtle.penup()
    turtle.goto(startX, startY) 
    turtle.pendown()
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height) 
    turtle.done()

def box_8():
    turtle.penup()
    turtle.goto(startX, startY)
    turtle.done()

big_box()
box_8()




