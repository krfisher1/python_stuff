from blobber import Blobber
import time

def main():
    name = input("Enter your Blobber's name: ")
    color = input("Enter your Blobber's color: ")
    radius = eval(input("Enter your Blobber's radius: "))
    height = eval(input("Enter your Blobber's height: "))

    myBlobber = Blobber(name, color, radius, height)

    done = False
    start_time = time.time()
    while not done:
        print()
        print("Main Menu")
        print("\t(1) Display Name")
        print("\t(2) Change Name")
        print("\t(3) Display Color")
        print("\t(4) Change Color")
        print("\t(5) Feed Blobber")
        print("\t(6) Blobber Speak")
        print("\t(7) Exit")
        
        # Display current vitals and check to see if it has turned to dust
        # This will catch cases where the Blobber was fed too much as well
        volume = 3.14 * (radius ** 2) * height
        
        vitals, blobberOK = myBlobber.vitalsOK()
 

        print("Your Blobber is at " + format(vitals, ".2%") + " happiness")
        if not blobberOK:
            print("Your Blobber turned to dust")
            break

        choice = eval(input("Make a selection: "))
        print()

        # Check to see if the Blobber turned to dust while waiting for the user to make a selection
        vitals, blobberOK = myBlobber.vitalsOK() 

        if not blobberOK:
            print("Your Blobber is at " + format(vitals, ".2%") + " happiness")
            print("Your Blobber turned to dust")
            break

        if choice == 1:
            displayName(myBlobber)
        elif choice == 2:
            changeName(myBlobber)
        elif choice == 3:
            displayColor(myBlobber)
        elif choice == 4:
            changeColor(myBlobber)
        elif choice == 5:
            feedBlobber(myBlobber)
        elif choice == 6:
            blobberSpeak(myBlobber)
        elif choice == 7:
            done = True
        end_time = time.time()
        total_time = start_time - end_time
        vitals = .02 * total_time
    print("Thanks for taking care of a Blobber")

#Didn't have enough time to finish assignment so here is what I would have done next if I had time#
#Set getters and setters to pull the private variables#
#Use the vitatsOk in the blobber file to figure out if blobber is okay blobber should be okay if .90 * original volume >= volume >= 100 percent #
def displayName(blobber):
    print("Your Blobber's name is " + displayName)

def changeName(blobber):
    name = input("Enter Blobber's new name: ")

def setName(self, name):
    Blobber.__name = name
    displayName(name)

def displayColor(blobber):
    print("Your Blobber's color is " + displayColor)

def changeColor(blobber):
    color = input("Enter Blobber's new color: ")
    Blobber.__color = color
    displayColor(color)

def feedBlobber(blobber):
    food = eval(input("Enter amount to you feed your Blobber: "))
    volume = 3.14 * ((Blobber.__radius + food) ** 2) * Blobber.__height

def blobberSpeak(blobber):
    print("My name is " + Blobber.__name + ", and I am " + Blobber.__color + ". ")
    print("My current happiness level is " + Blobber.__vitals)
main()