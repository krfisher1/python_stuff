## Find multiples of 3 and 5 form the number 1 - 999 and add them together ##
num = 1
total = 0
while num < 1000:
    if num % 3 == 0 or num % 5 == 0: 
        total += num
    num += 1
    print(total)




