from colorama import Fore


# Welcome prints out the welcome text
def welcome():
    print(Fore.RED + "                                                   D U N G E O N")
    print(Fore.GREEN + """
    The village of Honeywood has been terrorized by strange, deadly creatures for months now. Unable to endure any 
    longer, the villagers pooled their wealth and hired the most skilled adventurer they could find: you. After
    listening to their tale of woe, you agree to enter the labyrinth where most of the creatures seem to originate,
    and destroy the foul beasts. Armed with a longsword and a bundle of torches, you descend into the labyrinth, 
    ready to do battle....
    
    """)


def play_game():
    welcome()
    # Get player input
    input("Press ENTER to continue")
    explore_labyrinth()


def explore_labyrinth():
    while True:
        player_input = input(Fore.YELLOW + "-> ").lower().strip()

        # Do something with that input
        if player_input == "help":
            show_help()

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
