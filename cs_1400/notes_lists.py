total_scores = 0

def average(listOfNumbers):
    avg = 0
    
    for num in listOfNumbers:
       avg += num
    avg /= len(listOfNumbers)
    return avg   




numbers = [0, 1, 2, 3, 4]
print(numbers)

blueberry = "blueberry"
fruits = ["apple", "orange", "banana", blueberry, ]
print(fruits)

print(numbers[0])
number_1 = numbers[1]
print(number_1)

print(fruits[0])

sum = numbers[0] + numbers[1] + numbers[2] + numbers[3]

print(sum)

#select starting at 1 and going to one befor the last number of 4
print(numbers[1:4])

# see how big your list is len
print("Length of numbers pre " + str(len(numbers)))
print(len(numbers))

#add information to list when you need it
# append adds numbers to list
for i in range(5,10):
    
    numbers.append(i)
print(numbers)
# see how big your list is 
print("length of numbers post" + str(len(numbers)))
print(len(numbers))
#
 
listOfNumbers = len(numbers)

   # again = "y"
quiz_score = [53.4, 89.0, 90.98, 100.0, 79.1, 45.5]
 #   while again == "y":
#
    #    number_quizscore = float(input("Enter in a quiz score "))
   #     quiz_score.append(number_quizscore)
  #      again = input("Do you want to enter another quizscore ")
 #       
#        print(quiz_score)







average(quiz_score)
#
#
#
#
#
#
#




#How to print a string vertically


hello_message = "Hello this is a welcome message"

def print_vertically(my_string):
    for charactor in my_string:
        print(charactor)

print_vertically(hello_message)











def replace(toFind, replaceWith, sentence):
    newStr = ""
    for index in range(0, len(sentence)):
        if sentence[index] == toFind:
            newStr += replaceWith
        else:
            newStr += sentence[index]  
    return newStr






newSentence = replace("t", "T", "the tiny turtle talks to tim")            
print(newSentence)



quizzes = [45.5, 100, 89, 90, 56, 87,76]

# remove lowest score from list


print(quizzes)

def removeLowest(listOfNumbers):
    min = listOfNumbers[0]
    for num in listOfNumbers:
        if num < min:
            min = num
    print("Removing " + str(min))
    listOfNumbers.remove(min)

removeLowest(quizzes)
print(quizzes)




def deleteIndexFromList(index, list):
    print("deleting index" + str(index) + " from the list " + str(list) + ". ")
    del list[index]


print()
print(quizzes)
deleteIndexFromList(0, quizzes)
print(quizzes)
print()







# greatest to smallest is needed for true
# false makes it smallest to biggest
quizzes.sort(reverse=True)
print(quizzes)









def explainTheSort(list, isRevers = False):
    print(list)
    if isRevers:
        print("you are sorting this array from smallest to biggest")
        list.sort()
    if not isRevers:
        print("You are sorting this from biggest to smallest")   
        list.sort() 
    print(list)

explainTheSort(quizzes)





# another way to get rid of the lowest score is:
def bestWayToGetRid(list):
    print(list)
    list.sort()
    del list[0]
    print(list)


bestWayToGetRid(quizzes)    


































































