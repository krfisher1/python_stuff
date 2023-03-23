


print("Welcome to the social situation analyzer system")
print("This is for person 1")



#person 1#
p1name = input("Enter your name: ")
x1 = int(input("Enter your x position "))
y1 = int(input("Enter your y position "))
p1rad = int(input("enter your personal space radius: "))




#person 2#
print("This is for person 2")
p2name = input("Enter your name: ")

x2 = int(input("Enter your x position "))
y2 = int(input("Enter your y position"))
p2rad = int(input("enter your personal space radius:"))


d1 = (x2 - x1) ** 2 +(y2 - y1) ** 2
distance = d1 ** (1/2)



totalrad = int(p1rad) + int(p2rad)

#person test#
if int(distance) < (int(p2rad)  + int(p1rad)):
    person = (p2name + " is in " + p1name +"'s personal space")
elif distance > (p2rad +p1rad):
    person = ("Neither "+ p1name  +" nor "+p2name+" is in the orther's personal space")
elif (int(distance) < int(p1rad)) and int(distance) < int(p2rad):
    person = (p1name + " and "+ p2name +"  are in each other's personal space")
else:
    person = (p1name + " is in " + p2name + "'s personal space")
    

distanceex = distance < (int(p1rad) + int(p2rad))
p1bigp2 = int(p1rad) > int(p2rad)

#space test#
if bool(distanceex) and bool(p1bigp2):
    space = (p1name + "'s personal space is entirely inside" + p2name + "'s personal space")
elif distanceex:  
    space = ( p1name + " and " + p2name + "'s personal spaces oerlap")
elif distance > (p1rad + p2rad):
    space = ( p1name + " and " + p2name + "'s personal spaces do not overlap")
else:
    space = (p2name + "'s personal space is entirely inside "+ p1name + "'s personal space")    



msg = "Person Test: " + person +"\n Space Test: " +space 




print(msg)