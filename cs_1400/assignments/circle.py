#This code makes circles#

def main():

    from random import randint 
    center = str(input("Enter in your center point: "))
    offset = int(input("Enter your offset: "))
    radius = int(input("Enter a radius "))
    count = int(input("Enter your count: "))

    pos = center.split(",")
    startX = int(pos[0])
    startY = int(pos[1])


    loopcount = 0


    anglesep = 360 / count
    import turtle as t
    t.speed(0)
    while loopcount < count:
        colornum = randint(1,4)
        if colornum == 1:
            color = "blue"
        elif colornum == 2:
            color = "red"
        elif colornum == 3:
            color = "yellow" 
        else:
            color = "green" 
        t.color(color)           
        t.penup()
        t.goto(startX, startY)
        
        t.forward(offset + radius)
        
                
        t.pendown()
        t.circle(radius)
        if loopcount >= 1:
            t.right(anglesep)

        loopcount += 1
    