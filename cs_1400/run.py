'''
import random
i = 0
ele_in_same_room = 0
zookeeper_in_same_room_as_both_ele = 0
zookeeper_in_same_room_as_one_ele = 0
zookeeper_in_neither_rooms = 0
again = True




while i in range(100000):
    ele1 = random.randint(1,7)
    ele2 = random.randint(1,7)
    zookeeper = random.randint(1,7)
    if zookeeper == ele1 and zookeeper == ele2:
        zookeeper_in_same_room_as_both_ele += 1
    else: 
        zookeeper_in_same_room_as_one_ele


    i += 1    
 
print(zookeeper_in_same_room_as_both_ele) 
print(zookeeper_in_same_room_as_one_ele)




pos = start_positions.split(",")
startX = int(pos[0])
startY = int(pos[1])

'''

import turtle
start_positions = input("Enter a starting position: ")
width = int(input("Enter your width "))
height = int(input("Enter the height: "))
pos = start_positions.split(",")
startX = int(pos[0])
startY = int(pos[1])

height_of_each_box = height / 8
width_of_each_box = width / 8

#original box
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
#black boxes
turtle.penup()
turtle.goto(startX, startY)

x_pos_max = width + startX
y_pos_max = height + startY
isSmile = input("True or false ")
if isSmile == "true":  
        turtle.penup()
        turtle.goto(-60,60)
        turtle.setheading(-60)
        turtle.pendown()
        turtle.circle(70,120)
        turtle.penup()
else:
        turtle.penup()
        turtle.goto(-60,60)
        turtle.setheading(-60)
        turtle.pendown()
        turtle.setheading(-60)
        turtle.circle(70,-180)
        turtle.penup() 
turtle.done()





