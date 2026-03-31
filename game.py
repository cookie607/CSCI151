# game.py
#Preston Fields
#3/22/26

from gamefunctions import (
    print_welcome,
    print_shop_menu,
    purchase_item,
    random_monster,
    fight,
    rest
    )

def main():
    """Runs the main flow of the game."""

    # Welcome the player
    name = input("Enter your name: ")
    print(print_welcome(name, 50))
    print()

    player_info = {
        "health": 20,
        "power": 4,
        "money": 30
    }

    quest = True

    while quest:
        choice = input(                                # player game options
            " \n1) Adventure into the woods."
            " \n2) Rest."
            " \n3) Abandon run.\n"
            "Input: [choose 1,2 or 3]"
            ).lower().strip()

        if choice == "1":
            my_monster = random_monster()              # create monster
            player_info = fight(player_info, my_monster)  # fight it

            if player_info["health"] <= 0:             # check player has health
                print("Game Over!")                         #end the game
                quest = False

        elif choice == "2":                         #initiates the rest
            
            rest(player_info)
        
        elif choice == "3":                         #quits the game
            print(f"You did well {name}!")
            print("You have abandoned the run.")
            quest = False

        else:                                       #the input is invalid prompts new input
            print("Invalid input, please enter an accepted input")
     
main()
