#This code does random and plays the assignment#


def main():   
    play = 0
    import turtle as t

    while play == 0:
        shape = input("Enter the shape you want(rectangle, circle, random) ")

        if shape == "random":
            from random import randint
            shapenum = randint(1,2)
            
            if shapenum == 1:
                shape = "rectangle"
                
            
                    
            elif shapenum == 2:
                shape = "circle"
            print(shape)    
                

        if shape == "rectangle":
            import rectangle
            rectangle.main()
        elif shape == "circle":
            import circle    
            circle.main()


        again = input("Do you want to run the program again and keep picture ")
        if again == "yes":
            play = 0
        else:
            play = 1    
            
            t.done()