from itertools import product
import os
import time
import difflib
inventory = {} # Empty dictionary that will be filled later

#     while True:
#         
#         
#         
#         
#         
#      
#         for item_ordered in ordered_iitems:
#             item_amount = int(input(f"How much of {item_ordered} is wanted: "))
#             inventory[item_ordered] = [inventory[item_ordered][0] - item_amount, inventory[item_ordered][1]]
#         file = open("restock_update.txt", "w")
#         file.write("Product|Stock|Price")
#         for prod, info in inventory.items():
#             file.write(f"\n{prod}| {info[0]} |{info[1]}")
#         ask = input("More orders (Y/N): ").lower()
#         if ask == "n": break
#     return

### First Function (Adding Inventory) ###
def addinventory(): # Function for user to add inv (fills dict)
    global inventory # Allows function to access the dict
    os.system('cls' if os.name =='nt' else 'clear')

    ## Getting Products ##
    print ("Please enter the products you have stock of. Sepparate each product with a comma (,)")
    products = input("> ").strip().replace(" ", "-").lower() # Takes input, replaces spaces with - and removes and start and end white space and makes it lowercase

    # Checks #
    comma = products.find(",")
    while comma != -1: # For each comma, 
        if products[comma + 1] == "-": # Checks if there is a - infront of the comma
            products = products[:comma + 1] + products[comma + 2:] # And gets rid of it
        if products[comma - 1] == "-": # Checks if there is a - behind of the comma
            products = products[:comma - 1] + products[comma:] # And gets rid of it
        comma = products.find(",", comma + 1) # Moves on to the next comma, or -1 if none
    os.system('cls' if os.name =='nt' else 'clear')

    # Changes #
    print (products)
    more = input("Are all those products correct (Y/N): ").lower()
    if more == "n":
        incorrect = input("What product name is wrong: ")
        while not(incorrect in products): 
            incorrect = input("Not a product. Try Again: ")
        change = input("What do you want to replace it with: ").strip().replace(" ", "-")
        products = products.replace(incorrect, change)
    os.system('cls' if os.name =='nt' else 'clear')

    # Adding #
    print (products)
    more = input("Do you want to add more products (Y/N): ").lower() # makes input lowercase
    if more == 'y':
        add = input("Add more products, sepparate each by a comma: ").strip().replace(" ", "-").lower() # Takes input, replaces spaces with - and removes and start and end white space and makes it lowercase
        comma = add.find(",")
        while comma != -1: # For each comma, 
            if add[comma + 1] == "-": # Checks if there is a - infront of the comma
                add = add[:comma + 1] + add[comma + 2:] # And gets rid of it
            if add[comma - 1] == "-": # Checks if there is a - behind of the comma
                add = add[:comma - 1] + add[comma:] # And gets rid of it
            comma = add.find(",", comma + 1) # Moves on to the next comma, or -1 if none
        products = products + "," + add
    products = products.replace(",", " ").split() # Turns the commas to spaces then into a list
    os.system('cls' if os.name =='nt' else 'clear')

    ## Getting Price ##
    for product in products:
        prod_price = input(f"price of {product}: ")
        # Checks #
        while True:
            try:
                prod_price = float(prod_price)
                break
            except ValueError:
                prod_price = input(f"NaN, Please try again: ")

        # Adding to Dict #
        inventory[product] = [0, prod_price] # Make a dict entry for reach product with the stock = 0 and the price being what they inputed
    
    ## File Writing ##
    file = open("product_base.txt", "w")
    file.write("Product|Stock|Price")
    for prod, info in inventory.items():
        file.write(f"\n{prod}| {info[0]} |{info[1]}")
    return


### Second Function (Adding Stock) ###
def addstock():
    global inventory
    os.system('cls' if os.name =='nt' else 'clear')

    ## Getting Stock ##
    for prod, info in inventory.items():
        stock = input(f"How much stock do you want to add to {prod}: ")

        # Checks #
        while True: #Checks if the input can be a number
            try:
                stock = float(stock)
                break
            except ValueError:
                stock = input(f"NaN, Please try again: ")
        while stock % 1 != 0: #Checks if stock is a whole number
            stock = input(f"Stock must be a whole number, Please try again: ")

        # Adding to Dict #
        inventory[prod] = [info[0] + stock, info[1]]
    
    ## File Writing ##
    file = open("restock_update.txt", "w")
    file.write("Product|Stock|Price")
    for prod, info in inventory.items():
        file.write(f"\n{prod}| {info[0]} |{info[1]}")
    return


def orders():
    global inventory
    os.system('cls' if os.name =='nt' else 'clear')

    ## Getting Items for Order ##
    print ("Please enter the items for the order. Sepparate each item with a comma (,)")
    order = input("> ").strip().replace(" ", "-").lower()

    # Checks #
    comma = order.find(",")
    while comma != -1: # For each comma, 
        if order[comma + 1] == "-": # Checks if there is a - infront of the comma
            order = order[:comma + 1] + order[comma + 2:] # And gets rid of it
        if order[comma - 1] == "-": # Checks if there is a - behind of the comma
            order = order[:comma - 1] + order[comma:] # And gets rid of it
        comma = order.find(",", comma + 1) # Moves on to the next comma, or -1 if none
    os.system('cls' if os.name =='nt' else 'clear')

    # Changes #
    print (order)
    more = input("Are all those products correct (Y/N): ").lower()
    if more == "n":
        incorrect = input("What product name is wrong: ")
        while not(incorrect in order): 
            incorrect = input("Not on Order. Try Again: ")
        change = input("What do you want to replace it with: ").strip().replace(" ", "-")
        products = products.replace(incorrect, change)
    os.system('cls' if os.name =='nt' else 'clear')

    # Adding #
    print (order)
    more = input("Do you want to add more products (Y/N): ").lower() # makes input lowercase
    if more == 'y':
        add = input("Add more products, sepparate each by a comma: ").strip().replace(" ", "-").lower() # Takes input, replaces spaces with - and removes and start and end white space and makes it lowercase
        comma = add.find(",")
        while comma != -1: # For each comma, 
            if add[comma + 1] == "-": # Checks if there is a - infront of the comma
                add = add[:comma + 1] + add[comma + 2:] # And gets rid of it
            if add[comma - 1] == "-": # Checks if there is a - behind of the comma
                add = add[:comma - 1] + add[comma:] # And gets rid of it
            comma = add.find(",", comma + 1) # Moves on to the next comma, or -1 if none
        order = order + "," + add
    order = order.replace(",", " ").split() # Turns the commas to spaces then into a list
    os.system('cls' if os.name =='nt' else 'clear')

    # More Checks #
    _ = 0
    while _ < len(order):
        product = order[_]
        if product not in inventory.keys():
            closest_match = difflib.get_close_matches(product, inventory.keys(), n=1, cutoff=0.6)
            if closest_match:
                new = closest_match[0]
                order[i] = new
                print(f"Replaced {product} with {new}")
            else:
                new = input(f"{product} is not sold at the store, What's the real product: ")
                order[order.index(product)] = new
                _ = 0
            continue
        _ += 1
    











addinventory()
addstock()
