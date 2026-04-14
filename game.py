# game.py
#Preston Fields
#3/22/26

from gamefunctions import (
    print_welcome,
    print_shop_menu,
    purchase_item,
    random_monster,
    fight,
    rest,
    shop,
    equip,
    save,
    load_game
    )

def main():
    """Runs the main flow of the game."""

    choice = input(
        "Welcome!\n"
        "1) New Game\n"
        "2) Load Game\n"
        "Choice: "
        ).strip()
    if choice == "2":
        filename = input("Enter save file name: ")
        player_info = load_game(filename)

        if player_info is None:
            player_info = {
                "health": 20,
                "base_power": 4,
                "power": 4,
                "money": 30,
                "inventory": [],
                "equipped_weapon": None
            }

    else: 
         # Welcome the player
        name = input("Enter your name: ")
        print(print_welcome(name, 50))
        print()

        player_info = {
            "health": 20,
            "base_power": 4,
            "power": 4,
            "money": 30,
            "inventory": [],
            "equipped_weapon": None
        }

    quest = True

    while quest:
        choice = input(                                # player game options
            " \n1) Adventure into the woods."
            " \n2) Rest."
            " \n3) Visit the Shop."
            " \n4) Equip Item."
            " \n5) Save and Quit.\n"
            "Input: [choose 1-5] \n"
            ).lower().strip()

        if choice == "1":
            my_monster = random_monster()              # create monster
            player_info = fight(player_info, my_monster)  # fight it

            if player_info["health"] <= 0:             # check player has health
                print("Game Over!")                         #end the game
                quest = False

        elif choice == "2":                         #initiates the rest
            
            rest(player_info)
        
        elif choice == "3":

            player_info = shop(player_info)

        elif choice == "4":
            player_info = equip(player_info)

        elif choice == "5":                     # Quits the game
            filename = input("Enter save file name: ")
            save(filename, player_info)

            print("Game saved. Goodbye!")
            quest = False

        else:                                       #the input is invalid prompts new input
            print("Invalid input, please enter an accepted input")
     
main()
