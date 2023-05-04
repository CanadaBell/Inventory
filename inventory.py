# Inputs
import random as r
import os
import time
import difflib
import sys
from textwrap import dedent

inventory = {} # Empty dictionary that will be filled later
inventory2 = {} # Empty dictionary that will be filled later

### Menu Functions ###

## Main Menu ##
def main_menu():
    os.system('cls' if os.name =='nt' else 'clear')
    print (dedent("""
    Welcome to BISS: Bamazon Inventory System Solutions

    Here you can: 
        - Add products to your inventory
        - Add stock 
        - Get orders and remove stock

    Please enter one of the following commands: 
    1. Add Products For Sale - add products and their price to the inventory 
    2. Add Stock - to add stock to an existing product in your store's inventory                                
    3. Place Order - order items from vendors or customers                        
    4. Quit - exit BISS
    """))
    command = input("> ") # Input for command


    while True:
        try:
            command = int(command)
            if command not in [1, 2, 3, 4]:
                command = input("Please input a valid command ")
                continue
            break
        except ValueError:
            command = input("Please input a valid command ")
    
    return command

## First Menu ##
def first_menu():
    os.system('cls' if os.name =='nt' else 'clear')
    print (dedent("""
    When adding products to inventory you can upload a ready made txt file

    OR

    Create a whole new inventory

    You can also pick a random inventory

    Please enter one of the following commands: 
    1. Upload File 
    2. Create File
    3. Random Inventory
    4. View Inventory
    5. Go Back

    """))
    command = input("> ")

    while True:
        try:
            command = int(command)
            if command not in [1, 2, 3, 4, 5]:
                command = input("Please input a valid command ")
                continue
            break
        except ValueError:
            command = input("Please input a valid command ")
    
    return command

## Second Menu ##
def second_menu():
    os.system('cls' if os.name =='nt' else 'clear')
    print (dedent("""
    When adding product stock to inventory you can add stock to each product

    OR

    Look at inventory

    Please enter one of the following commands: 
    1. Add Stock 
    2. Look at Inventory
    3. Go Back

    """))
    command = input("> ")

    while True:
        try:
            command = int(command)
            if command not in [1, 2, 3]:
                command = input("Please input a valid command ")
                continue
            break
        except ValueError:
            command = input("Please input a valid command ")
    
    return command

## Third Menu ##
def third_menu():
    os.system('cls' if os.name =='nt' else 'clear')
    print (dedent("""
    You can either input an order

    OR

    Look at inventory

    Please enter one of the following commands: 
    1. Input order
    2. Look at Inventory
    3. Go Back

    """))
    command = input("> ")

    while True:
        try:
            command = int(command)
            if command not in [1, 2, 3]:
                command = input("Please input a valid command ")
                continue
            break
        except ValueError:
            command = input("Please input a valid command ")
    
    return command

### Extra Functions ###

## Returning Text ##
def returning():
    t = 0
    while t < 5:
        sys.stdout.write('\rreturning |')
        time.sleep(0.1)
        sys.stdout.write('\rreturning /')
        time.sleep(0.1)
        sys.stdout.write('\rreturning -')
        time.sleep(0.1)
        sys.stdout.write('\rreturning \\')
        time.sleep(0.1)
        t += 0.5
    return

## Random Inventory ##
def random_inv():
    global inventory
    os.system('cls' if os.name =='nt' else 'clear')
    pick = r.randint(1, 5)
    if pick == 1:
        inventory = {
            "Self-cleaning litter box": [0, 249.99],
            "Magnetic cat door": [0, 36.50],
            "Cute cat-shaped salt and pepper shakers": [0, 9.99],
            "Feather wand toy": [0, 7.50],
            "Elevated food and water bowls": [0, 29.99],
            "Cute cat figurine": [0, 7.50],
            "Scratch post": [0, 29.95],
            "Stylish cat carrier purse": [0, 58.99],
            "Grooming gloves": [0, 14.95],
            "Luxury cat bed": [0, 89.99],}
            
    elif pick == 2:
        inventory = {
            "Poop Bags": [0, 8.85],
            "Dog Raincoat": [0, 34.99],
            "Dog Harness": [0, 26.99],
            "Dog Stuffed Animal": [0, 12.99],
            "Grooming Brush": [0, 11.75],
            "Dog Boots": [0, 24.99],
            "Dog Pajamas": [0, 15.99],
            "Dog GPS Tracker": [0, 79.99],
            "Dog Christmas Sweater": [0, 18.99],
            "Dog Carrier Backpack": [0, 48.99],}

    elif pick == 3:
        inventory = {
            "Gaming Mouse": [0,29.99],
            "Tote bag": [0,19.50],
            "Plant": [0,14.99],
            "Desk Lamp": [0,22.75],
            "Hair Dryer": [0,34.50],
            "Sneakers": [0,89.99],
            "Nail Polish": [0,6.25],
            "Coffee Mug": [0,8.50],
            "Candle": [0,9.99],
            "Wi-Fi Extender": [0,27.50],}
    
    elif pick == 4:
        inventory = {
            "Backpack": [0,34.99],
            "Picture Frame": [0,7.99],
            "Desk Chair": [0,79.99],
            "Yoga Mat": [0,24.72],
            "Water Bottle": [0,12.99],
            "Sunglasses": [0,24.95],
            "Card Game": [0,14.95],
            "T-shirt": [0,19.99],
            "Notebook": [0,4.99],
            "Watering Can": [0,11.25],}
    
    else:
        inventory = {
            "Shower Curtain": [0,15.99],
            "Lip Balm": [0,3.49],
            "Jump Rope": [0,8.55],
            "Cooking Timer": [0,7.50],
            "Speaker": [0,39.50],
            "Android Phone Charger": [0,9.99],
            "Bath Mat": [0,16.25],
            "Yoga Block": [0,10.99],
            "Umbrella": [0,16.75],
            "Fishing Rod": [0,59.99],}

    print ("Random Inventory Selected")
    returning()
    return

## File Reader ##
def file_reader():
    global inventory, inventory2, inventory3
    os.system('cls' if os.name =='nt' else 'clear')

    print ("Please input the name of your stock file *MUST BE A .TXT FILE*")
    file_name = input("(don't include the .txt) > ").replace(".txt", "") + ".txt"

    while os.path.exists(file_name) != True:
        file_name = input("Please input an actuall file (don't include the .txt) ").replace(".txt", "") + ".txt"

    file = open(file_name, "r")
    for line in file.readlines():
        line = line.strip().replace("|", "").split()

        if len(line) != 3: continue
        item = line[0]; stock = line[1]; price = line[2]

        if stock.isdigit() != True: stock = 0
        stock = int(stock)

        try: price = float(price)
        except ValueError: continue

        inventory[item] = [stock, price]

    os.system('cls' if os.name =='nt' else 'clear')
    print ("Here is the inventory:")
    for p,i in inventory.items():
        print (f"{p}: {i[0]}, {i[1]}")
    inventory2 = inventory.copy(); inventory3 = inventory.copy()
    time.sleep(5)

    os.system('cls' if os.name =='nt' else 'clear')
    returning()
    return
## Inventory Printer ##
def inventory_print(num_of_inv):
    
    os.system('cls' if os.name =='nt' else 'clear')

    print ("Here is the requested inventory")
    global inventory, inventory2, inventory3
    if num_of_inv == 1:
        if len(inventory) == 0:
            print ("If nothing prints then the invintory is empty")
        for p,i in inventory.items():
            print (f"{p}: {i[0]}, {i[1]}")
    else:
        if len(inventory2) == 0:
            print ("If nothing prints then the invintory is empty")
        for p,i in inventory2.items():
            print (f"{p}: {i[0]}, {i[1]}")
    time.sleep(5)

    os.system('cls' if os.name =='nt' else 'clear')

    returning()
    return

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
    global inventory, inventory2
    if len(inventory2) == 0:
        inventory2 = inventory.copy()
    os.system('cls' if os.name =='nt' else 'clear')

    ## Getting Stock ##
    for prod, info in inventory2.items():
        stock = input(f"How much stock do you want to add to {prod}: ")

        # Checks #
        while True:
            try:
                stock = int(stock)
                break
            except ValueError:
                stock = input(f"NaN, Please try again: ")

        # Adding to Dict #
        inventory2[prod] = [info[0] + stock, info[1]]
    
    ## File Writing ##
    file = open("restock_update.txt", "w")
    file.write("Product|Stock|Price")
    for prod, info in inventory2.items():
        file.write(f"\n{prod}| {info[0]} |{info[1]}")
    file.close()
    return


### Third Function (Taking Orders) ###
def orders():
    while True:
        global inventory2
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

            # Upadting Dict #
            inventory2[product] = [inventory2[product][0] - amount, inventory2[product][1]]

        for prod, info in inventory2.items():
            file.write(f"\n{prod}| {info[0]} |{info[1]}")

        file.close()

        os.system('cls' if os.name =='nt' else 'clear')
        ask = input("Is there another order you would like to enter (Y/N): ").lower()
        if ask == "n":
            os.system('cls' if os.name =='nt' else 'clear')
            returning()
            break
    return

### Outputs ###

while True:
    dec = main_menu()

    if dec == 1:
        while True:
            dec = first_menu()
            if dec == 1:
                file_reader()
                continue
            elif dec == 2:
                addinventory()
                break
            elif dec == 3:
                random_inv()
                continue
            elif dec == 4:
                inventory_print(1)
                continue
            else:
                break

    elif dec == 2:
        while True:
            dec = second_menu()
            if dec == 1:
                addstock()
                break
            elif dec == 2:
                inventory_print(2)
                continue
            else:
                break
    
    elif dec == 3:
        while True:
            dec = third_menu()
            if dec == 1:
                orders()
                break
            elif dec == 2:
                inventory_print(2)
                continue
            else:
                break

    else:
        os.system('cls' if os.name =='nt' else 'clear')
        print("Thank you for using Bamazon Inventory System Solutions\nHope to see you again")
        sys.exit()
