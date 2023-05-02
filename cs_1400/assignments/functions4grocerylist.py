def whole_list_functionmain():
            



    groceries = []
    electronics = []
    clothes = []
    books = []
    unknown =[]

    print("Welcome to the online shopping cart. ")
    def add_groceries():
        print("Items in groceries: vegetable, bread, producs, rice, pasta ect. ")
        items = input("What would you like to add to your list: ")
        groceries.append(items)
        

    def add_electronics():
        print("Items in Electronist: phones, phone chargers, lamp, computer, remote, tv ect. ")
        items = input("What would you like to add to your list: ")
        electronics.append(items)


    def add_clothes():
        print("Items in clothes: shirt, pants, jeans, shoes, socks ect. ")
        items = input("What would you like to add to your list: ")
        clothes.append(items)    


    def add_books():
        print("Items in books: green eggs and ham, cat in the hat, inside out and back again ect.")
        items = input("What would you like to add to your list: ")
        books.append(items)    


    def department_unknown():
        items = input("What would you like to add to your list: ")
        unknown.append(items)


    def remove2():
        listcount = 0
        for asdf in range(listcount):
            rem = removedep[i] 
            if thing == rem:
                i = int
                del removedep[i]
            else:    
                listcount += 1
                i += 1
        

    def print_items():
        print("Items in groceries = " + str(groceries))
        print("Items in electronics = " + str(electronics))
        print("Items in clothes = " + str(clothes))
        print("Items in books = " + str(books))
        print("Items in unknown = " + str(unknown))


    def sort_all():
        groceries.sort()
        electronics.sort()
        clothes.sort()
        books.sort()
        unknown.sort()






    again = "y"
    while again != "n":
        department = input("What department do you want to go to(groceries, clothes, electronics, clothes, books, unknown) ")
        if department == "groceries":
            add_groceries()
        elif department == "electronics":
            add_electronics() 
        elif department == "clothes":
            add_clothes()
        elif department == "books":
            add_books()    
        else:          
            department_unknown()
        again = input("Enter another item(y or n) ")



    sort_all()
    print_items()
    removequ = "y"
    print("It's time to remove. ")
    removequ = input("Would you like to remove any items(y or n): ")

    listcount = 0
    while removequ != "n":
        removedep = input("What department do you want to remove from: ")
        if removedep == "books":
            remo = books
        elif removedep == "groceries":
            remo = groceries
        elif removedep == "clothes":
            remo = clothes
        elif removedep == "electronics":   
            remo = electronics
        else:
            remo = unknown           

        thing  = input("What item do you want to remove: ")
        
        remo.remove(thing)
        
        sort_all()
        print_items()
        removequ = input("Would you like to remove any items(y or n): ")







    sort_all()
    print_items()










