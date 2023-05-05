def list():

    numberlist = []

    numberlist = input("Add numbers to your list: ")



def mean(numberlist):

    added = 0

    for i in range(len(numberlist)):
        added += numberlist[i]
        i += 1
    added /= len(numberlist)    
    print(added)


list()
mean()