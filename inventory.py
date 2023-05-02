# Inputs
import os
import time
import difflib

inventory = {} # Empty dictionary that will be filled later

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
        d = comma - 1
        while d >= 0 and products[d] == "-": # Check for dashes in front of the comma
            d -= 1
        products = products[:d+1] + products[comma:]
        
        d = comma + 1
        while d < len(products) and products[d] == "-": # Check for dashes behind the comma
            d += 1
        products = products[:comma+1] + products[d:]
        
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
    file.close()
    return


### Second Function (Adding Stock) ###
def addstock():
    global inventory
    os.system('cls' if os.name =='nt' else 'clear')

    ## Getting Stock ##
    for prod, info in inventory.items():
        stock = input(f"How much stock do you want to add to {prod}: ")

        # Checks #
        while True:
            try:
                stock = int(stock)
                break
            except ValueError:
                stock = input(f"NaN, Please try again: ")

        # Adding to Dict #
        inventory[prod] = [info[0] + stock, info[1]]
    
    ## File Writing ##
    file = open("restock_update.txt", "w")
    file.write("Product|Stock|Price")
    for prod, info in inventory.items():
        file.write(f"\n{prod}| {info[0]} |{info[1]}")
    file.close()
    return


### Third Function (Taking Orders) ###
def orders():
    global inventory
    money_made = 0
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
                order[_] = new
                print(f"Replaced {product} with {new}")
            else:
                new = input(f"{product} is not sold at the store, What's the real product: ")
                order[order.index(product)] = new
                _ = 0
            continue
        _ += 1
    
    ## Getting Amount for Order ##

    file = open("business_quarter.txt", "w")
    file.write("Product|Stock|Price")

    for product in order:
        amount = input(f"How much of {product} has been ordered: ")

        # Checks #
        while True:
            try:
                amount = int(amount)
                break
            except ValueError:
                amount = input(f"NaN, Please try again: ")

        # Writing to File #
        inventory[product] = [inventory[product][0] - amount, inventory[product][1]]

        file.write(f"{inventory[product]}|{inventory[product][0]}|{inventory[product][1]}")
        money_made += inventory[product][1] * amount

    money_made = round(money_made, 2)
    file.write(f"Money Earned: ${money_made}")
    file.close()
    return 
            








print ("""""")












addinventory()
addstock()
orders()
