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


def random_monster():
    monsters = [
        {
            "name": "Goblin",
            "description": "A small, scrawny creature...",
            "health": (6,9),
            "power": (2,4),
            "money": (3,4)
        },
        {
            "name": "Slime",
            "description": "A wobbling blob...",
            "health": (5,7),
            "power": (1,2),
            "money": (1,2)
        },
        {
            "name": "Angry Chicken",
            "description": "A scrappy bird...",
            "health": (2,4),
            "power": (1,2),
            "money": (0,2)
        }
    ]

    base = random.choice(monsters)

    my_monster = {
        "name": base["name"],
        "description": base["description"],
        "health": random.randint(*base["health"]),
        "power": random.randint(*base["power"]),
        "money": random.randint(*base["money"])
    }

    print("\nAn enemy approaches!\n----------")
    print(my_monster["name"])
    print(my_monster["description"])
    print(f"Health: {my_monster['health']}")
    print(f"Power: {my_monster['power']}")
    print(f"Money: {my_monster['money']}")

    return my_monster

def fight(player_info, monster_info):
    """
    Handles turn-based combat between player and monster.
    """

    # Local copies for combat
    player_health = player_info["health"]
    monster_health = monster_info["health"]
    player_damage = player_info["power"]
    monster_damage = monster_info["power"]

    print(f"\n You engage the {monster_info['name']} in battle!")

    while player_health > 0 and monster_health > 0:
        user_action = input("\nChoose action: (1) Fight (2) Run: ").strip()

        if user_action == "1":
            # Player attacks first
            monster_health -= player_damage
            print(f"\nYou hit the {monster_info['name']} for {player_damage} damage!")

            # Check if monster is defeated before it attacks
            if monster_health <= 0:
                print(f"The {monster_info['name']} has been defeated!")
                break

            # Monster attacks back
            player_health -= monster_damage
            print(f"The {monster_info['name']} hits you for {monster_damage} damage!")

            # Display updated health
            print(f"Your health: {player_health}")
            print(f"{monster_info['name']} health: {monster_health}")

        elif user_action == "2":
            print("You ran away!")
            player_info["health"] = player_health
            return player_info

        else:
            print("Invalid command. Choose 1 or 2.")

    # --- After combat ends ---
    if player_health <= 0:
        print("\n You have been defeated...")
        
    elif monster_health <= 0:
        print(f"\n You defeated the {monster_info['name']}!")
        print(f"You found {monster_info['money']} gold!")
        player_info["money"] += monster_info["money"]

    # Save updated health back to player
    player_info["health"] = max(player_health, 0)

    return player_info

def rest(player_info):
    """Allows the player to rest for 5 gold and recover 5 health points, up to max health."""

    print(f"Your current health: {player_info['health']}, Gold: {player_info['money']}")
    choice = input("Would you like to rest for the price of 5 gold? (yes or no) ").strip().lower()

    if choice == "yes":

        if player_info["money"] < 5:                #Checks if the player has enough money
            print("You don't have enough gold to rest!")
            return

        if player_info["health"] >= player_info.get("max_health", 20):  #checks if player has full health
            print("Your health is already full!")

        else:                                       #heals the player and collects payment
            player_info["health"] += 5
            if player_info["health"] > player_info.get("max_health", 20):
                player_info["health"] = player_info.get("max_health", 20)
            player_info["money"] -= 5
            print(f"You take a rest. Health: {player_info['health']}, Gold: {player_info['money']}")

    elif choice == "no":                            #leaves the resting area
        print("You chose not to rest.")

    else:                                           #the input is invalid prompts new input
        print("Invalid input, please enter 'yes' or 'no'.")



"""def test_functions():
    Runs basic tests for all functions in this module.

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

"""
