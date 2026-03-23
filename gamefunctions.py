# gamefunctions2.py
#Preston Fields
#3/1/26

#provides game functions for buying items and encountering random monsters from definitions

import random

#--------------------------------------------------------------------------------------------#
def print_welcome(name, width):
    """Function welcomes the user with a specialized welcome from the parameters of a name
    and the desired width of the centered welcome phrase"""
    return f"{'Hello, ' + name + '!':^{width}}"    

def print_shop_menu(item1, price1, item2, price2):
    """Calling the function opens the shop displaying 2 items with prices from the inputs of
    the first item with its price and the second item with its price respectively"""
    item1 = item1.capitalize()
    item2 = item2.capitalize()
    price1 = f"${price1:.2f}"
    price2 = f"${price2:.2f}"
    
    print(f"//{'#'*22}\\\\")
    print(f"|| {item1:<12}{price1:>8} ||")
    print(f"|| {item2:<12}{price2:>8} ||")
    print(f"\\\\{'#'*22}//")
    

def purchase_item():
    """This function opens an opportunity for the player to purchase an item by specifying the
     item's price, how much money they have and how many they would like to purchase and returns
     how many they have purchased with how much remaining money they have"""

    itemPrice = int(input("Enter item price: ")) #recieves user input about the item price followed by how much money they have then how many items they wish to buy
    startingMoney = int(input("Enter starting money: "))
    quantitytoPurchase = input("Enter quanitity desired (press Enter for 1): ")

    if quantitytoPurchase == "":
        quantitytoPurchase = 1
    else:
        quantitytoPurchase = int(quantitytoPurchase)

    if quantitytoPurchase <= (startingMoney / itemPrice):
        num_purchased = quantitytoPurchase
    else:
        num_purchased = startingMoney // itemPrice

    leftover_money = startingMoney - (num_purchased * itemPrice)

    print(f"Number of items purchased: {num_purchased}")
    print(f"Money remaining: {leftover_money}")

def random_monster():
    """A random monster gets summoned by random with random aspects to challenge the user.
    The monsters have random stats and a description is provided for each"""
    my_monster = {} #empty dictionary to be assigned with monster information
    chance = random.randint(1,3)

    if chance == 1:
        my_monster["name"] = "Goblin" # assigns the first possible monstser as a goblin
        my_monster["description"] = (
            "A small, "
            "scrawny creature with dull "
            "green skin and a rusty dagger. "
            "It’s quick but fragile, relying on "
            "sneak attacks and fleeing when threatened."
            )
        my_monster["health"] = random.randint(5,7)
        my_monster["power"] = random.randint(2,4)
        my_monster["money"] = random.randint(3,6)

    elif chance == 2:
        my_monster["name"] = "Slime" # assigns the second monster as a slime
        my_monster["description"] = (
            "A small, "
            "wobbling blob of translucent "
            "goo. It moves slowly and deals "
            "little damage, making it more of "
            "a minor obstacle than a real threat."
            )
        my_monster["health"] = random.randint(2,3)
        my_monster["power"] = random.randint(0,1)
        my_monster["money"] = random.randint(0,2)

    elif chance == 3:
        my_monster["name"] = "Angry Chicken" # monster three is an angry chicken
        my_monster["description"] = (
            "A small, "
            "scrappy bird with sharp claws "
            "and a fierce glare. It pecks and "
            "scratches quickly but is fragile "
            "and easily frightened. "
            )
        my_monster["health"] = random.randint(2,4)
        my_monster["power"] = random.randint(1,2)
        my_monster["money"] = 0

    print("\nAn enemy approaches! \n    ----------")
    print(f"{my_monster['name']}")
    print(f"{my_monster['description']}")
    print(f"Health: {my_monster['health']}")
    print(f"Power: {my_monster['power']}")
    print(f"Money: {my_monster['money']}")

    return my_monster
