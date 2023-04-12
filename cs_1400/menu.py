
## Menu for cs 1400 ## 


print("Welcome to my menu!")
print()
input("Press enter to see the menu ")
##list of menu items##
print("Menu: ")
print()
print()
print("1) breakfast burrito: $3.10")
print("      -Our breakfast burrito has hach browns, eggs, chopped green chiles,breakfast sausage links, cheese, and our homemade flour tortillas. ")
print()
print("2) Baccon $1.20")
print("      -our baccon is localy harvested and salted to prefection ")
print()
print("3) Ham $1.00")
print(
  "        -Our ham is localy harvest and cooked in honey to give it a sweet flavor.")
print()
print("4) Bread $2.99")
print("        -our bread is made fresh daily from local sources.")
print()
print("5) waffles $5.00")
print(
  "        -our waffles are surved with maple surup from Canada, our secret waffel mix is sure to astound you.")
print()
print("6) croissant $4.10")
print(
  "         -our croissants are shiped from France that day and are served with nutela")
print()
print("7) sausage $2.30")
print("     -our sausage are served with canadian surup")
total = 0.0
print()


##loop that asks them how many they want then runs it that many times and add there total as you are going##
totalnum = input("How many food items do you want ")
for i in range(int(totalnum)):
  number = input("Type in the number next to the thing you want ")
  if number == "1" or number == "breakfast burrito" or number == "Breakfast burrito" or number == "Breakfast Burrito":
    total += 3.10
  elif number == "2" or number == "Baccon" or number == "baccon":
    total += 1.20
  elif number == "3" or number == "Ham" or number == "ham":
    total += 1
  elif number == "4" or number == "Bread" or number == "bread":
    total += 2.90
  elif number == "5" or number == "waffles" or number == "Waffles":
    total += 5
  elif number == "6" or number == "croissant" or number == "Croissant":
    total += 4.10
  elif number == "7" or number == "Sausage" or number == "sausage":
    total += 1.30

##Print there total add tax, then print new total##
print("your total is without tax is $" + str(total))
print("A $.5 tax has been added.")
total += .5     
print("Your total with tax is $" + str(total))   
##Ask the user what they are paying with (Cash or card), then if they pay with cash ask how much they are paying with then give them there change back, tell them to have a good day##
pay = input("Are you paying with cash or card? ")
if pay == "cash" or pay == "Cash":
    cash = int(input("How much money are you paying? "))
    cash -= total
    print("Alright we owe you $" + str(cash))
elif pay == "Card" or pay == "card":
    print("Alright you are good to pay")
else:
    print("That isn't a useable form of payment, your order has been canceled.")
enjoy = input("Did you enjoy your stay with us")
   
## exit statment ##    
print("Thank you for dinning with us")    










