import bad_math 


do = input("Do you want to add, subtract, multiply, divide ")
first = int(input("Number one: "))
sec = int(input("Number two: "))
if do == "add":
    print(bad_math.add(first, sec))
if do == "subtract":
    print(bad_math.subtract(first, sec))  
if do == "multiply":
    print(bad_math.multiply(first, sec))
if do == "divide":
    print(bad_math.divide(first, sec))