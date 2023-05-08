import random as r


loopcountlist = []
again = "y"
againcount = 0
while again != "n":
    number = r.randint(1,101)
    


    
    loopcount = 0 



    while number <= 100:
        loopcount += 1
        guess = int(input("Guess a number from 1-100 "))
        if number > guess:
            print("That number is too Low guess again")
        elif number < guess:
            print("That number is too high")
        else:
            print("Good Job the number was " + str(number))
            break

    print("It took you "+ str(loopcount) + " tries")

    





    again = input("Do you want to play again(y or n) ")    
    againcount += 1
    loopcountlist.append(loopcount)






loopcountlist.sort()


with open('high_scores.txt', 'w') as wf:
    wf.write("Your scores are(from highest to lowest): " + str(loopcountlist))
    wf.close()






with open('high_scores.txt', 'r') as rf:
    f_contents = rf.read()    
    print(f_contents)


