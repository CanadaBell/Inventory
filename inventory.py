import os
inventory = {}

def addinventory():
    global inventory
    while True:
        os.system('cls' if os.name =='nt' else 'clear')
        product = input("Product you want to add: ")
        prod_price = input("Price of one of that item: ")
        inventory[product] = [0, prod_price]
        done = input("Done? (Y/N): ").lower()
        if done == "y": break
    file = open("product_base.txt", "w")
    file.write("Product\tStock\tPrice")
    for prod, info in inventory.items():
        file.write(f"\n{prod}\t{info[0]}\t{info[1]}")
    return

def addstock():
    global inventory
    for prod, info in inventory.items():
        os.system('cls' if os.name =='nt' else 'clear')
        prod_stock = input(f"How much stock do you have for {prod}: ")
        inventory[prod] = [prod_stock, info[1]]
    print (inventory)
    return

addinventory()
addstock()
