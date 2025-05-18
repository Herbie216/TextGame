class Room:
    """
    Represents a room in the game map.
    Can hold a description, artifacts, and hints.
    """

    def __init__(self, row, col, description=""):
        self.row = row
        self.col = col
        self.description = description
        self.search_count = 0
        self.is_artifact_room = False
        self.is_hint_room = False
        self.hints = [
            "You are close. Try going right.",
            "Still close! Check near the east wall.",
            "Sorry, my English is rusty but look behind the painting."
        ]
        self.connections = {}  # e.g., {'north': Room(...), 'east': Room(...)}

    def connect(self, direction, other_room):
        """
        Connect this room to another room in the given direction.
        """
        self.connections[direction] = other_room

    def text_to_binary(self, text):
        """
        Convert text to a space-separated string of 8-bit binary values.
        """
        return ' '.join(format(ord(c), '08b') for c in text)

    def search(self):
        """
        Perform a search in the room.
        Shows hints in binary for first two searches, then English.
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
    Represents the game map holding multiple rooms.
    """

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        # Use a dict keyed by (row, col) to store rooms
        self.rooms = {}

    def add_room(self, room):
        """
        Add a room object to the map.
        """
        self.rooms[(room.row, room.col)] = room

    def get_room(self, row, col):
        """
        Retrieve the room at specified coordinates.
        """
        return self.rooms.get((row, col))

    def connect_rooms(self, room1, direction, room2):
        """
        Connect two rooms bidirectionally.
        """
        room1.connect(direction, room2)
        opposites = {'north': 'south', 'south': 'north', 'east': 'west', 'west': 'east'}
        opposite_dir = opposites.get(direction)
        if opposite_dir:
            room2.connect(opposite_dir, room1)

class Player:
    def __init__(self, start_row=0, start_col=0, game_map=None):
        self.row = start_row
        self.col = start_col
        self.game_map = game_map

    def move(self, direction):
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

        if 0 <= new_r < self.game_map.rows and 0 <= new_c < self.game_map.cols:
            self.row, self.col = new_r, new_c
            room = self.game_map.get_room(self.row, self.col)
            print(f"You moved {direction} to room ({self.row},{self.col}).")
            print(room.description)
        else:
            print("You bumped into a wall, Ouch!")
