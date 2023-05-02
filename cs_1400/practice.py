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