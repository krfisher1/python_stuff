import random

print("Welcome to the Geussing Game")
print("The Computer has picked a number from 1-10. Try to match it.")
computer_num = random.randrange(1,10)
user_num = int(input("What numver do you choose(1-10): "))
difference = abs(computer_num - user_num)

print("You picked " + str(user_num) + ", and the actual number was " + str(computer_num))


if difference == 0:
    print("Honored to play with you, master.")
if difference == 1: 
    print("You are a worthy opponent, Knight")
elif difference == 2:
    print("You have much ot learn, Padawan")
elif difference == 3:
    print("Youngling, your time will come.")
else:
    print("Keep working hard in the Service Corps")

       