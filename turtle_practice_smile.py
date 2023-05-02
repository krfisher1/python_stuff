import turtle as t


t.speed(0)

t.penup()
t.goto(0,0)
t.color("yellow")
t.begin_fill() 
t.pendown()
t.circle(100)
t.end_fill()
t.penup()  

t.penup()
t.goto(-25,115)
t.color("black")
t.begin_fill() 
t.pendown()
t.circle(15)
t.end_fill()
t.penup() 

         
t.penup()
t.goto(25,115)
t.color("black")
t.begin_fill() 
t.pendown()
t.circle(15)
t.end_fill()
t.penup()   


t.goto(0,0)
t.pensize(5)
t.circle(25,180)

t.done()