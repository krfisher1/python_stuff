import a_math as am


 
'''from a_math import add 
if you do this then you don't have to write am
also use , to use more then one thing to imput '''

print("Calculator ")
do = input("What would you like to do: (add, subtract, multiply, divide) ")
first_num =int(input("First number "))
sec_num = int(input("second number"))
if do == "add":
    print(am.add(first_num, sec_num))

if do == "subtract":
    print(am.subract(first_num, sec_num))
if do == "multiply":
    print(am.multiply(first_num, sec_num))
if do == "divide":
    print(am.divide(first_num, sec_num))    



print(am.constants["pi"])    

























