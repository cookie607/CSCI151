# game.py
#Preston Fields
#3/22/26

from gamefunctions import (
    print_welcome,
    print_shop_menu,
    purchase_item,
    random_monster
    )

def main():
    """Runs the main flow of the game."""

    # Welcome the player
    name = input("Enter your name: ")
    print(print_welcome(name, 50))
    print()

    # Show shop
    print("Welcome to the shop!")
    print_shop_menu("potion", 5, "sword", 20)
    print()

    # Purchase item
    print("Let's buy something:")
    purchase_item()
    print()

    # Encounter monster
    print("Time for a battle!")
    monster = random_monster()

    print("\nGood luck,", name + "!")


if __name__ == "__main__":
    main()
