# game.py
#Preston Fields
#3/22/26

import pygame

from gamefunctions import (
    print_welcome,
    random_monster,
    fight,
    rest,
    shop,
    equip,
    save,
    load_game,
    GRID_SIZE,
    TILE_SIZE,
    town_position,
    monster_position,
    reset_monster_position,
    check_tile_event
    )
pygame.init()

WIDTH = GRID_SIZE * TILE_SIZE
HEIGHT = GRID_SIZE * TILE_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grid RPG")
clock = pygame.time.Clock()

# ----------------------------
# PLAYER
# ----------------------------
player = {
    "x": 0,
    "y": 0,
    "health": 20,
    "base_power": 4,
    "power": 4,
    "money": 30,
    "inventory": [],
    "equipped_weapon": None
}

running = True
previous_position = (-1, -1)

while running:
    clock.tick(10)
    screen.fill((0, 0, 0))

    # ------------------------
    # EVENTS
    # ------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                player["x"] = max(0, player["x"] - 1)

            if event.key == pygame.K_RIGHT:
                player["x"] = min(GRID_SIZE - 1, player["x"] + 1)

            if event.key == pygame.K_UP:
                player["y"] = max(0, player["y"] - 1)

            if event.key == pygame.K_DOWN:
                player["y"] = min(GRID_SIZE - 1, player["y"] + 1)

    # ------------------------
    # TILE EVENTS (FIXED)
    # ------------------------
    player_pos = (player["x"], player["y"])

    if player_pos != previous_position:
        event_type = check_tile_event(player_pos, town_position, monster_position)

        if event_type == "TOWN":
            shop(player)

        elif event_type == "MONSTER":
            monster = random_monster()
            player = fight(player, monster)

            monster_position = reset_monster_position()

    previous_position = player_pos

    # ------------------------
    # DRAW GRID
    # ------------------------
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            rect = pygame.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, (40, 40, 40), rect, 1)

    # ------------------------
    # DRAW TOWN
    # ------------------------
    pygame.draw.circle(
        screen,
        (0, 200, 0),
        (town_position[0]*TILE_SIZE + 16, town_position[1]*TILE_SIZE + 16),
        10
    )

    # ------------------------
    # DRAW MONSTER
    # ------------------------
    pygame.draw.circle(
        screen,
        (200, 0, 0),
        (monster_position[0]*TILE_SIZE + 16, monster_position[1]*TILE_SIZE + 16),
        10
    )

    # ------------------------
    # DRAW PLAYER
    # ------------------------
    pygame.draw.rect(
        screen,
        (0, 0, 255),
        (player["x"]*TILE_SIZE, player["y"]*TILE_SIZE, TILE_SIZE, TILE_SIZE)
    )

    pygame.display.flip()
pygame.quit()


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

