#Design for number pyramid
# 
# 
# 
# ask the user to imput a number and a space after it then save it to a variable titled num
# define a function called makeNumberPyramid
# in the function enter the following:
# 
# 
# ask the user to imput the number of rows
# set up a for loop the number of rows in the rows set up another loop to use spaces 
# set up a while loop to print out the numbers that will be in each of the rows. 
# also set up an if statement saying that if the number of rows the user imputed are above ten then the spaceing will be different and you will have to add extra spaces. 
# 
# hint if you set up the botom first(like the idea of the bottom string) then the other lines will make more sense. 
# 


rows = int(input("Enter number of rows: "))
rowcount = 0
k = 0

while rowcount <= rows:
    for i in range(1, rows+1):

        for space in range(1, (rows-i)+1):
            print(end="  ")
   
        while k!=(2*i-1):
            
            print(rowcount , end="")
            k += 1
    rowcount += 1
k = 0
print()


# 
# 
# #