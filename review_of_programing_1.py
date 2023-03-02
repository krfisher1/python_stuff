
#This is a review of programing one#

##This is a print statment: It just prints the string that you type out ##
print("")
#Data Types
    #str() "This is a string" #
    #Integer = int() is a number without a decimal #
    #Float = float() is a number with a decimal#
    #Boolean is either true or false#

#String concatenation is when you add two strings together to make one string ex. "this is" + "2 strings."#
#You can't add a string to a number you must typecast it first#
    #To typecast(Making one datatype act like another) something "This is " + str(2)#


#Function is a group of code that is named that does something specific They have to have ()#
    #print(), input(), str(), #


# variables are a named box to put information in(variavles can't start with a number a capital letter or have any spaces)
box = 2
#The = sign is an operator an operator is a symbol that does an action usually has a left and a right side the right side usually happens first

print(box)
box += 2
print(box)
if box == 2:
    print("Box is two")
elif box <= 100:
    print("It's less than 100")    
else:
    print("I am in the else")


one = True
two = True
three = False

if one:
    print("this is a one")
if one and two:
    print("Both of these have to be true")
if one and two and three:
    print("If one of them are false and it's true then that means that the entire thing is false") 


if one or two:
    print("only one has to be true") 
if one or two or three:
    print("Because you are using or it would print this ")
if one and two or three:
    print("THat's tpp complicated") 

if not three:
    print("Three is true")


import random



print(random.randint(1,10))    

while box < 100:
    print("yikes")
    box += 1

#Math in python -> left hand side + right hand side #
    # math operators: +(add), -(subtraction), *(times), **(exponents), /(division), %(modulous) 
        # modulous devides the 10 % 3 = 1 ten / three with a remainder of 1 we just keep the remainder


#conditions are a section of code that gives us back a True or False
#to ask the question we use conditional operators 
    # == is equal
    # != is not equal
    # >= greather than or equal to
    # <= less than or equal to
    # < less than
    # > greather than


# Conditionals are how we ask questions in python
    #Key words: 
        #if: asks the first question(condition) only 1
        #elif: as many as you want or none
        #else is the catch all for the questions that weren't answered only one or none


#logical operators 
    # and 
    # or 
    # not


# Libraries is code that you pull into your program to use that was written at ta different time doesn't have to be your code
#to use a library we use the keyword import
#then we call the library fundctions (can be found in the documentation) 
    #   random.randint(arguments(parameters))


#this is a comment and doesn't get ran as code

#loops run a group of code until a specific condition is met


