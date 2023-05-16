
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
        return self.__drawEyes


    def __drawMouth():
        if self.isHappy:   
            t.penup()
            t.goto(-60,60)
            t.setheading(-60)
            t.pendown()
            t.circle(70,120)
            t.penup()
        else:
            t.penup()
            t.goto(-60,60)
            t.pendown()
            t.setheading(-60)
            t.circle(100,90) 

    def __drawHead():
        if self.isSmile:
            t.penup()
            t.color("yellow")
            t.begin_fill() 
            t.pendown()
            t.circle(100)
            t.end_fill()
            t.penup()
        else:
            t.penup()
            t.goto(0,0)
            t.color("red")
            t.begin_fill() 
            t.pendown()
            t.circle(100)
            t.penup()

    def __drawEyes():        
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
            t.circle(15)
            t.end_fill()
            t.penup() 

            t.goto(30,135)
            t.color("blue")
            t.begin_fill() 
            t.pendown()
            t.circle(15)
            t.end_fill()
            t.penup()
                         


    def changeMouth(self):
        return self.__drawMouth
    def changeEmotion(self):
        return self.__drawHead    
    def changeEyes(self):
        return self.__drawEyes

def main():
    face = Face()
    done = False




    while not done:
        print("Change My Face")
        mouth = "frown" if face.isSmile else "smile"
        emotion = "angry" if face.isHappy else "happy"
        eyes = "blue" if face.isDarkEyes else "black"
        print("1) Make me", mouth)
        print("2) Make me", emotion)
        print("3) Make my eyes", eyes)
        print("0) Quit")

        menu = eval(input("Enter a selection: "))

        face.draw_face()
        if menu == 1:

                face.changeMouth()    
        elif menu == 2:

                face.changeEmotion() 
            
        elif menu == 3:

                face.changeEyes()             
            
        else:
            break

    print("Thanks for Playing")

    t.hideturtle()
    t.done()


main()
