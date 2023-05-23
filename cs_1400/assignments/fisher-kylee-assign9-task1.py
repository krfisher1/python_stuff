
import turtle as t


class Face:
    def __init__(self):
        self.__smile = True
        self.__happy = True
        self.__darkEyes = True

    def draw_face(self):
        t.clear()
        self.__drawHead()
        self.__drawEyes()
        self.__drawMouth()

    def isSmile(self):
        return self.__smile
    def isHappy(self):
        return self.__happy 
    def isDarkEyes(self):
        return self.__darkEyes       

    def __drawHead(self):
        if self.isHappy:
                color = "yellow"


                
        elif self.isHappy == False:
                color = "red"
                t.goto(0,0)
                
                
                
        

        t.color(color)

        t.begin_fill() 
        t.pendown()
        t.circle(100)
        t.end_fill()
        t.penup()


    def __drawMouth(self): 
        if self.isSmile:   
            t.penup()
            t.color("black")
            t.width(8)
            t.goto(-60,60) 
            t.pendown()
            t.setheading(-60)
            t.circle(70, 120)
            t.penup()
        else:
            t.penup()
            t.color("black")
            t.width(8)
            t.goto(60,60)
            t.setheading(120)
            t.pendown()
            t.circle(70,120)
            t.penup() 

    def __drawEyes(self):  
        if self.isDarkEyes: 
            t.penup()
            t.goto(-30,135)
            t.color("black")
            t.begin_fill() 
            t.pendown()
            t.dot(25)
            t.end_fill()
            t.penup() 

            t.goto(30,135)
            t.color("black")
            t.begin_fill() 
            t.pendown()
            t.dot(25)
            t.end_fill()
            t.penup() 

        else:
            t.penup()
            t.goto(-30,135)
            t.color("blue")
            t.begin_fill() 
            t.pendown()
            t.dot(25)
            t.end_fill()
            t.penup() 

            t.goto(30,135)
            t.color("blue")
            t.begin_fill() 
            t.pendown()
            t.dot(25)
            t.end_fill()
            t.penup()
                            



#Didn't have enough time to finish assignment so next I would figure out why the smile keeps moving even though I have it starting at 0,0 each time#


def main():
    face = Face()
    done = False
    loopcount = 0 
    while not done:
        face.draw_face()
        print("Change My Face")
        mouth = "frown" if face.isSmile else "smile"
        emotion = "angry" if face.isHappy else "happy"
        eyes = "blue" if face.isDarkEyes else "black"
        print("1) Make me", mouth)
        print("2) Make me", emotion)
        print("3) Make my eyes", eyes)
        print("0) Quit")

        menu = eval(input("Enter a selection: "))

        if menu == 1:
            if face.isSmile:
                face.isSmile = False
            elif face.isSmile == False:
                face.isSmile = True    
               
        elif menu == 2:
            if face.isHappy:
                face.isHappy = False
            elif face.isHappy == False:
                face.isHappy = True 
            
            
        elif menu == 3:
            if face.isDarkEyes:
                face.isDarkEyes = False
            elif face.isDarkEyes == False:
                face.isDarkEyes = True 
                       
        else:
            break

        
    print("Thanks for Playing")

    t.hideturtle()
    t.done()


main()











