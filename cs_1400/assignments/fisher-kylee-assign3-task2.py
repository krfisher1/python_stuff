import turtle

x = int(input("Please enter an x cordenent for the center of the circle "))
y = int(input("Please enter a y cordenent for the center of the circle "))




turtle.penup()
turtle.goto(x, (y - 140))
turtle.pendown()
turtle.begin_fill()
turtle.color("black")
turtle.circle(200)
turtle.end_fill()

turtle.penup()
turtle.goto(x , (y - 85))
turtle.pendown()
turtle.begin_fill()
turtle.color("blue")
turtle.circle(150)
turtle.end_fill()

turtle.penup()
turtle.goto(x, (y - 50))
turtle.pendown()
turtle.begin_fill()
turtle.color("red")
turtle.circle(100)
turtle.end_fill()

turtle.penup()
turtle.goto(x,y)
turtle.pendown()
turtle.begin_fill()
turtle.color("yellow")
turtle.circle(50)
turtle.end_fill()


turtle.done()

