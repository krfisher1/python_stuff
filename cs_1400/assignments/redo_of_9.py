
import turtle
class Face:
    def __init__(self):
        self.__smile = True
        self.__happy = True
        self.__darkEyes = True
        
    def draw_face(self):
        turtle.clear()
        self.__drawHead()
        self.__drawEyes()
        self.__drawMouth()

    def isSmile(self):
        return self.__smile
    def isHappy(self):
        return self.__happy
    def isDarkEyes(self):
        return self.__darkEyes

    def changeMouth(self):
        if self.isSmile:
            drawHead
        else:
            
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
            if isSmile:
                isSmile = False
            elif isSmile == False:
                isSmile = True
        elif menu == 2:
<Fill-In>
        elif menu == 3:
<Fill-In>
        else:
            break
print("Thanks for Playing")
turtle.hideturtle()
turtle.done()
main()
