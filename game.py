import random

import armory
import bestiary
from classes import Player, Room, Game

from colorama import Fore, init


# Welcome prints out the welcome text
def welcome():
    print(Fore.RED + "                                                    D U N G E O N")
    print(Fore.GREEN + """
    The village of Honeywood has been terrorized by strange, deadly creatures for months now. Unable to endure any 
    longer, the villagers pooled their wealth and hired the most skilled adventurer they could find: you. After
    listening to their tale of woe, you agree to enter the labyrinth where most of the creatures seem to originate,
    and destroy the foul beasts. Armed with a longsword and a bundle of torches, you descend into the labyrinth, 
    ready to do battle....
    
    """)


def play_game():
    # init makes sure that colorama works on various platforms
    init()

    adventurer = Player()

    current_game = Game(adventurer)

    welcome()
    # Get player input
    input("Press ENTER to continue")
    explore_labyrinth(current_game)


# Generate a room
def generate_room() -> Room:
    items = []
    monster = {}

    # There is a 25% chance that this room has an item
    if random.randint(1, 100) < 26:
        i = random.choice(list(armory.items.values()))
        items.append(i)

    # There is a 25% chance that this room has a monster
    if random.randint(1, 100) < 26:
        monster = random.choice(bestiary.monsters)

    return Room(items, monster)


# Explore labyrinth is the main game loop, which takes user input and then performs specific actions based
# on that input
def explore_labyrinth(current_game: Game):
    while True:
        room = generate_room()

        current_game.room = room

        current_game.room.print_description()

        for i in current_game.room.items:
            print(f"{Fore.YELLOW}You see a {i['name']}")

        if current_game.room.monster:
            print(f"{Fore.RED}There is a {current_game.room.monster['name']} here!")

        player_input = input(Fore.YELLOW + "-> ").lower().strip()

        # Do something with that input
        if player_input == "help":
            show_help()

        elif player_input in ["n", "s", "e", "w"]:
            print(f"{Fore.GREEN}You move deeper into the dungeon.")
            continue

        # Quit the game
        elif player_input == "quit":
            print("Overcome with terror, you flee the dungeon, and are forever branded a coward.")
            # TODO: print out final score
            play_again()

        else:
            print("I'm not sure what you mean... type 'help' for help.")


def play_again():
    yn = get_yn(Fore.YELLOW + "Do you want to play again?")
    if yn == "yes":
        play_game()
    else:
        print("See you next time, Adventurer!!!")
        exit(0)


def get_yn(question: str) -> str:  # -> str is called type hinting
    while True:
        answer = input(question + " (yes/no) -> ").lower().strip()
        if answer not in ["yes", "no", "y", "n"]:
            print("Please enter yes or no")
        else:
            if answer == "y":
                answer = "yes"
            elif answer == "n":
                answer = "no"
            return answer


def show_help():
    print(Fore.GREEN + """
    Enter a command:
        - n/s/e/w: move in a direction
        - map - show a map of the labyrinth
        - look - look around and describe your environment
        - equip <item> - use an item from your inventory
        - un-equip <item> -stop using an item from your inventory
        - fight - attack a foe
        - examine <object> - examine an object more closely
        - get <item> - pick up an item
        - drop <item> - drop an item
        - rest - restore some health by resting
        - inventory - show your inventory
        - status - show current player status
        - quit - end the game
    """)
