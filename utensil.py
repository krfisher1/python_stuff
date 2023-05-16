class Utensil:

    

    def __init__(self, type, material):
        self.type = type
        self.material = material



    #function defined in class is a method
    def cut(self):
        if self.type == "knife" : 
            print("I am a knife, I will cut you. ")
        elif self.type == "fork":
            print("I am a fork, I can try to cut")
        elif self.type == "spork":
            print("I am a spork I can't cut anything")
        else:
            print("I am not something that cuts well. Don't make me do it. ")    


    def pickfood(itself):
        if itself.type == "knife" : 
            print("I am a knife, I can't pick up food. ")
        elif itself.type == "fork":
            print("I am a fork, I am the best at picking up food")
        elif itself.type == "spork":
            print("I am a spork I can pick up food by stabbing and scooping")    
        else:
            print("I am not something that picks up food. Don't make me do it. ")    




class Person:


    def __init__(self, __name = "Bob", __age = 32, __fingers = 10, __weight = 1000):
        self.name = __name
        self.age = __age
        self.fingers = __fingers
        self.weight = __weight
        


    def numberOfFingers(self):
        if self.fingers == 10:
            print("Me too I have ten fingers")
        elif self.fingers != 10:
            print("We don't have the same amount of fingers")   


    def driving(self):
        if self.age < 16:
            print("You can't get a drivers licence ")
        elif self.age == 16:
            print("Go get your licence") 
        else:
            print("You should have a drivers licence")   


    def speak(self, language = "English"):
        if language == "English":
            print("Hello, I am " + self.name)          
        elif language == "Pig latin":
            print("Something in pig latin")

    def __giveAge(this):
        print("I am " + str(this.__age) + " Years old") 


    def __giveWeight(self):
        print("I weigh ")


    def introduceSelf(self):
        self.speak()

    
    # getters
    def getName(self):
        return self.__name

    # setters
    def setName(self, name):
        if self.__name != "Shane":
            self.__name = name

    def getAge(self):
        return self.__age

    def setAge(self, age):
        if self.__age != 16:
            self.__age = age

    def getFingers(self):
        return self.__fingers

    def setFingers(self, fingers):
        if self.__fingers != 10:
            self.__fingers = fingers    








