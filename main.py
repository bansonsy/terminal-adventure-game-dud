import game

from blessings import Terminal


def main():
    # Clear the terminal window
    term = Terminal()
    print(term.clear())
    # Play the game until the game is over or the player quits
    game.play_game()


if __name__ == "__main__":
    main()
