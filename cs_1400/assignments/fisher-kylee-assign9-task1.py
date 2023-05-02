

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
        t.penup()
        t.goto(0,0)
        t.color("yellow")
        t.begin_fill() 
        t.pendown()
        t.circle(100)
        t.penup()       

    def isHappy(self):
        
  

    def isDarkEyes(self):
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

    def changeMouth(self):
        <Fill-In>
        self.draw_face()

    def changeEmotion(self):
        <Fill-In>
        self.draw_face()

    def changeEyes(self):
        <Fill-In>
        self.draw_face()


def main():
    face = <Fill-In>
    face.<Fill-In>

    done = False

    while not done:
        print("Change My Face")
        mouth = "frown" <Fill-In> "smile"
        emotion = "angry" <Fill-In> "happy"
        eyes = "blue" <Fill-In> "black"
        print("1) Make me", mouth)
        print("2) Make me", emotion)
        print("3) Make my eyes", eyes)
        print("0) Quit")

        menu = eval(input("Enter a selection: "))

        if menu == 1:
            <Fill-In>
        elif menu == 2:
            <Fill-In>
        elif menu == 3:
            <Fill-In>
        else:
            break

    print("Thanks for Playing")

    t.hideturtle()
    t.done()


main()








