import turtle 


turtle.pencolor("black")
turtle.fillcolor("white")
turtle.speed(0)
#head 
turtle.penup()
turtle.goto(50, -200)
turtle.pendown()

turtle.circle(75)

#body
turtle.penup()
turtle.goto(50, -60)
turtle.pendown()

turtle.begin_fill()

turtle.circle(62.5)
turtle.end_fill()
turtle.penup()
#bottom
turtle.goto(50, 55)
turtle.pendown()
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()
#smile
#eye 1
turtle.penup()
turtle.goto(40, 120)
turtle.pendown()
turtle.begin_fill()
turtle.color("black")
turtle.circle(6.5)
turtle.end_fill()
#eye 2
turtle.penup()
turtle.goto(60, 120)
turtle.begin_fill()
turtle.circle(6.5)
turtle.end_fill()
#nose
turtle.penup()
turtle.goto(50, 110)
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()
#smile
turtle.penup()
turtle.goto(30, 95)
turtle.pendown()
turtle.forward(40)
#hat
turtle.penup()
turtle.goto(10, 150)
turtle.pendown()
turtle.begin_fill()
turtle.forward(80)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(80)
turtle.left(90)
turtle.forward(20)
#hat part 2

turtle.end_fill()
turtle.left(90)
turtle.color("black")
turtle.begin_fill()
turtle.forward(10)
turtle.left(90)
turtle.forward(50)
turtle.left(270)
turtle.forward(60)
turtle.left(270)
turtle.forward(50)
turtle.end_fill()
#buttons
turtle.color("blue")
turtle.penup()
turtle.goto(50, 50)
turtle.begin_fill()
turtle.pendown()
turtle.circle(5)
turtle.end_fill()

turtle.penup()
turtle.forward(30)
turtle.begin_fill()
turtle.pendown()
turtle.circle(5)
turtle.end_fill()

turtle.penup()
turtle.forward(30)
turtle.begin_fill()
turtle.pendown()
turtle.circle(5)
turtle.end_fill()

#arms
turtle.width(7)
turtle.color("brown")
turtle.penup()
turtle.goto(100,30)
turtle.pendown()
turtle.begin_fill()
turtle.left(100)
turtle.forward(80)
turtle.end_fill()
turtle.penup()
turtle.goto(170, 40)
turtle.pendown()
turtle.right(45)
turtle.forward(10)
turtle.penup()
turtle.goto(170, 40)
turtle.pendown()
turtle.right(225)
turtle.forward(10)




turtle.penup()
turtle.goto(0, 30)
turtle.pendown()
turtle.left(90)
turtle.forward(80)
turtle.penup()
turtle.goto(-70, 20)
turtle.pendown()
turtle.right(45)
turtle.forward(10)
turtle.penup()
turtle.goto(-70, 20)
turtle.pendown()
turtle.right(225)
turtle.forward(10)

turtle.done()

