# gamefunctions2.py
#Preston Fields
#3/1/26

#provides game functions for buying items and encountering random monsters from definitions
"""
This program contians interactive game functions, a shop menu, monster summoning, item purchasing and
a welcome, for a simple text-based adventure game.

It includes functions to:
    - Display a welcome message for the player
    - Show a shop menu with 2 items and prices
    - Allow the player to purchase items and track remaining money
    - summon a random monster with stats and a description

Dependencies:
    -Python standard library: random

Usage:
    Import the functions and call them as part of the game flow:
        i.e. from game_module import print_welcome, print_shop_menu
        i.e. from game_module import purchase_item, random_monster

    Calls:
        print_welcome("Player", 50)
        print_shop_menu("Potion", 5, "Sword", 20)
        purchase_item()
        random_monster()        
"""

import random

#--------------------------------------------------------------------------------------------#
def print_welcome(name, width):
    """
    Prints a centered welcome message for the player. 

    Parameters:
        name (str): The player's name.
        width (int): The total width for centering the message.

    Returns:
        str: the formatted welcome message centered within the width. 
    """
    return f"{'Hello, ' + name + '!':^{width}}"    

def print_shop_menu(item1, price1, item2, price2):
    """
    Displays a shop menu with two items and thier prices.

    Parameters:
        item1 (str): Name of the first item.
        price1 (float): Price of the first item.
        item2 (str): Name of the second item.
        price2 (float): Price of the second item.

    Prints:
        A formatted shop menu with items and prices. 
    """
    item1 = item1.capitalize()
    item2 = item2.capitalize()
    price1 = f"${price1:.2f}"
    price2 = f"${price2:.2f}"
    
    print(f"//{'#'*22}\\\\")
    print(f"|| {item1:<12}{price1:>8} ||")
    print(f"|| {item2:<12}{price2:>8} ||")
    print(f"\\\\{'#'*22}//")
    

def purchase_item():
    """
    Allows the player to purchase items and tracks money spent.

    Prompts the user for:
        -Item price
        -Starting money
        -Quantity to purchase (default of 1)

    Prints:
        -Number of items purchase
        -Remaining money

    Returns:
        None
    """

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
    """
    Summons a random monster with stats and a description.

    Parameters:
        None. The monster's type, health, power, and money are randomly determined.
        Prints details to the screen.

    Returns:
        dict: A dictionary with keys:
            - name (str): Monster's name
            - description (str): Monster description
            - health (int): Monster health points
            - power (int): Monster attack power
            - money (int): Money the monster carries 
    """


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


def test_functions():
    """Runs basic tests for all functions in this module."""

    print("Testing print_welcome:")
    print(print_welcome("Preston", 30))
    print()

    print("Testing print_shop_menu:")
    print_shop_menu("potion", 5, "sword", 20)
    print()

    print("Testing purchase_item:")
    purchase_item()
    print()

    print("Testing random_monster:")
    monster = random_monster()
    print("Returned dictionary:", monster)


if __name__ == "__main__":
    test_functions()
