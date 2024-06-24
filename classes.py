class Player:
    def __init__(self):
        self.hp: int = 100  # Type Hint
        self.treasure: int = 0
        self.monsters_defeated: int = 0
        self.xp: int = 0
        self.turns: int = 0


class Room:
    def __init__(self):
        self.description: str
        self.sound: str
        self.smell: str

    def print_description(self):
        print(self.description)
        print(self.smell)
        print(self.sound)
