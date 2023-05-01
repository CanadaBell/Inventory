import os
inventory = {} # Empty dictionary that will be filled later
# def addstock():
#     global inventory
#     for prod, info in inventory.items():
#         os.system('cls' if os.name =='nt' else 'clear')
#         prod_stock = int(input(f"How much stock do you want to add to {prod}: "))
#         inventory[prod] = [info[0] + prod_stock, info[1]]
#     file = open("restock_update.txt", "w")
#     file.write("Product|Stock|Price")
#     for prod, info in inventory.items():
#         file.write(f"\n{prod}| {info[0]} |{info[1]}")
#     return

# def orders():
#     global inventory
#     while True:
#         os.system('cls' if os.name =='nt' else 'clear')
#         print ("Please enter the items for the order. Sepparate each item with a comma (,)")
#         ordered_items = input("> ")
#         ordered_items = ordered_items.replace(" ", "-")
#         comma = ordered_items.find(",")
#         while comma != -1:
#             if ordered_items[comma + 1] == "-":
#                 ordered_items = ordered_items[:comma + 1] + ordered_items[comma + 2:]
#             if ordered_items[comma - 1] ==  "-": 
#                 ordered_items = ordered_items[:comma - 1] + ordered_items[comma:]
#             comma = ordered_items.find(",", comma + 1)
#         ordered_items = ordered_items.replace(",", " ").split()
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
def addinventory(): # Function for user to add inv (fills dict)
    global inventory # Allows function to access the dict
    os.system('cls' if os.name =='nt' else 'clear') 
    print ("Please enter the products you have stock of. Sepparate each product with a comma (,)")
    products = input("> ").strip().replace(" ", "-").lower() # Takes input, replaces spaces with - and removes and start and end white space and makes it l
    comma = products.find(",")
    while comma != -1: # For each comma, 
        if products[comma + 1] == "-": # Checks if there is a - infront of the comma
            products = products[:comma + 1] + products[comma + 2:] # And gets rid of it
        if products[comma - 1] == "-": # Checks if there is a - behind of the comma
            products = products[:comma - 1] + products[comma:] # And gets rid of it
        comma = products.find(",", comma + 1) # Moves on to the next comma, or -1 if none
    print (products)
    more = input("Are all those products correct (Y/N): ").lower()
    if more == "n":
        incorrect = input("What product name is wrong: ")
        while not(incorrect in products): 
            incorrect = input("Not a product. Try Again: ")
        change = input("What do you want to replace it with: ").strip().replace(" ", "-")
        products = products.replace(incorrect, change)
    os.system('cls' if os.name =='nt' else 'clear')
    print (products)
    more = input("Do you want to add more products (Y/N): ").lower()
    if more == 'y':
        add = input("Add more products, sepparate each by a comma: ").strip().replace(" ", "-") # Takes input, replaces spaces with - and removes and start and end white space
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
    for product in products:
        prod_price = input(f"price of {product}: ")
        inventory[product] = [0, prod_price] # Make a dict entry for reach product with the stock = 0 and the price being what they inputed
    file = open("product_base.txt", "w")
    file.write("Product|Stock|Price")
    for prod, info in inventory.items():
        file.write(f"\n{prod}| {info[0]} |{info[1]}")
    return

def addstock():
    
addinventory()
