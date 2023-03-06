import turtle 

#Draw head and body(circles)#
turtle.penup()
turtle.goto(50, -200)
turtle.pendown()
turtle.circle("75")



turtle.done()



"""
snowman
Kylee Fisher
"""
color("#D3D3D3")
speed("10")
#head 
penup()
goto(50, -200)
pendown()
begin_fill()
circle("75")
end_fill()
#body
penup()
goto(50, -60)
pendown()
begin_fill()
circle("62.5")
end_fill()
penup()
#bottom
goto(50, 55)
pendown()
begin_fill()
circle("50")
end_fill()
#smile
#eye 1
penup()
goto(40, 120)
pendown()
begin_fill()
color("black")
circle("6.5")
end_fill()
#eye 2
penup()
goto(60, 120)
begin_fill()
circle("6.5")
end_fill()
#nose
penup()
goto(50, 110)
begin_fill()
circle("5")
end_fill()
#smile
penup()
goto(30, 95)
pendown()
forward("40")
#hat
penup()
goto(10, 150)
pendown()
begin_fill()
forward("80")
left(90)
forward("20")
left(90)
forward("80")
left(90)
forward("20")
#hat part 2

end_fill()
left(90)
color("red")
begin_fill()
forward("10")
left(90)
forward("50")
left(270)
forward("60")
left(270)
forward("50")
end_fill()
#buttons
color("blue")
penup()
goto(50, 50)
begin_fill()
pendown()
circle("5")
end_fill()

penup()
forward("30")
begin_fill()
pendown()
circle("5")
end_fill()

penup()
forward("30")
begin_fill()
pendown()
circle("5")
end_fill()

#arms
color("brown")
penup()
goto(100,30)
pendown()
begin_fill()
left(100)
forward(80)
circle("5")
end_fill()

penup()
goto(0, 30)
pendown()
left(100)
forward(80)
begin_fill()
circle("3")
end_fill()


