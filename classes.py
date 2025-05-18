# Classes representing game entities and map structure

class Room:
    """
    (WIP)
    Represents a single room on the game map.
    Each room can have a description, contain artifacts,
    hints, monsters, items, and connections to adjacent rooms.
    """

    def __init__(self, row, col, description=""):
        self.row = row
        self.col = col
        self.description = description
        self.search_count = 0  # Tracks how many times the room has been searched
        self.discovered = False  # Whether the player has discovered this room
        self.is_artifact_room = False
        self.is_hint_room = False
        self.is_nonsense_room = False
        self.monsters = []  # List of monsters in the room
        self.items = []     # List of items in the room
        self.connections = {}  # Dictionary mapping directions to connected rooms

    def connect(self, direction, other_room):
        """
        Connect this room to another room in a specific direction.
        """
        self.connections[direction] = other_room

    def text_to_binary(self, text):
        """
        (Cool Test I am Trying)
        Convert a string to a space-separated string of 8-bit binary values.
        Useful for encoding hints in binary form.
        """
        return ' '.join(format(ord(c), '08b') for c in text)

    def search(self):
        """
        (WIP)
        Simulate searching the room.
        For hint rooms, provides binary hints first, then reveals the hint in plain text.
        """
        if not self.is_hint_room:
            print("Nothing special here.")
            return

        if self.search_count < len(self.hints):
            hint = self.hints[self.search_count]
            self.search_count += 1

            if self.search_count < 3:
                print(f"Binary hint: {self.text_to_binary(hint)}")
            else:
                print(hint)
        else:
            print("No more hints here.")


class Map:
    """
    Represents the entire game map composed of multiple rooms.
    """

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        # Store rooms in a dictionary keyed by (row, col) tuples
        self.rooms = {}

    def add_room(self, room):
        """
        Add a Room object to the map at its coordinates.
        """
        self.rooms[(room.row, room.col)] = room

    def get_room(self, row, col):
        """
        Retrieve a room from the map by its coordinates.
        Returns None if no room exists at those coordinates.
        """
        return self.rooms.get((row, col))

    def connect_rooms(self, room1, direction, room2):
        """
        Connect two rooms in a bidirectional manner.
        The direction parameter describes how room2 is connected relative to room1.
        """
        room1.connect(direction, room2)
        opposites = {'north': 'south', 'south': 'north', 'east': 'west', 'west': 'east'}
        opposite_dir = opposites.get(direction)
        if opposite_dir:
            room2.connect(opposite_dir, room1)


class Player:
    """
    Represents the player character, tracking position, health,
    inventory, and allowing movement and combat.
    """

    def __init__(self, start_row=0, start_col=0, game_map=None, initial='P'):
        self.row = start_row
        self.col = start_col
        self.game_map = game_map
        self.initial = initial
        self.hp = 100
        self.inventory = []

    def move(self, direction):
        """
        Move the player in the specified direction if possible.
        Updates the player's position and reveals the new room.
        """
        direction = direction.lower()
        delta = {
            'north': (-1, 0),
            'south': (1, 0),
            'east': (0, 1),
            'west': (0, -1)
        }

        if direction not in delta:
            print("Invalid direction! Use north, south, east, or west.")
            return

        dr, dc = delta[direction]
        new_r, new_c = self.row + dr, self.col + dc

        # Check if the new position is within map bounds
        if 0 <= new_r < self.game_map.rows and 0 <= new_c < self.game_map.cols:
            self.row, self.col = new_r, new_c
            room = self.game_map.get_room(self.row, self.col)
            room.discovered = True

            print(f"You moved {direction} to room ({self.row},{self.col}).")
            print(room.description)

            # Notify player of monsters or items present
            if room.monsters:
                print("Monsters here!")
                for monster in room.monsters:
                    print(f"- {monster.name}: {monster.description}")

            if room.items:
                print("Items in the room:")
                for item in room.items:
                    print(f"- {item.name}: {item.description}")
        else:
            print("You bumped into a wall.")

    def attack(self, monster):
        """
        Attack a monster, dealing fixed damage.
        """
        damage = 10  # Base damage value
        monster.hp -= damage
        print(f"You hit {monster.name} for {damage} damage.")
        if not monster.is_alive():
            print(f"{monster.name} has been defeated!")

    def take_damage(self, amount):
        """
        Reduce player HP by the specified amount and check for death.
        """
        self.hp -= amount
        print(f"You took {amount} damage! HP: {self.hp}")
        if self.hp <= 0:
            print("You have died!")

    def add_item(self, item):
        """
        Add an item to the player's inventory.
        """
        self.inventory.append(item)
        print(f"You picked up: {item.name}")

    def use_item(self, item_name):
        """
        Use an item from inventory by name.
        If found, apply its effect and remove it from inventory.
        """
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                item.use(self)
                self.inventory.remove(item)
                return
        print("Item not found in inventory.")


class Monster:
    """
    Represents a monster with health, damage, and a description.
    """

    def __init__(self, name, hp, damage, description=""):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.description = description

    def is_alive(self):
        """
        Returns True if the monster has HP remaining.
        """
        return self.hp > 0

    def attack(self, player):
        """
        Attack the player, dealing damage.
        """
        print(f"{self.name} attacks!")
        player.take_damage(self.damage)


class Item:
    """
    Represents an item that the player can use.
    Effects are defined by a dictionary with a type and value.
    """

    def __init__(self, name, effect, description=""):
        self.name = name
        self.effect = effect  # e.g., {"type": "heal", "value": 20}
        self.description = description

    def use(self, player):
        """
        Apply the item's effect to the player.
        Currently supports healing.
        """
        effect_type = self.effect.get("type")
        value = self.effect.get("value", 0)

        if effect_type == "heal":
            old_hp = player.hp
            player.hp = min(100, player.hp + value)
            print(f"Used {self.name}, healed for {player.hp - old_hp} HP.")
        else:
            print(f"{self.name} has no usable effect.")
