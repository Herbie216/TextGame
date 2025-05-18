import random

# # Lists of dialogues for hints and nonsense lines the Dungeon Master might say

HINT_DIALOGUES = [
    "You are close. Try going right.",
    "Still close! Check near the east wall.",
    "Sorry, my English is rusty but look behind the painting.",
    "It shimmers in moonlight, doesn't it?",
    "One artifact rests in shadows.",
    "Seek where the wind whistles.",
    "Do not trust the corners.",
    "Follow the path of broken stone.",
    "It hides beneath silence.",
    "Not far. Just one more step."
]

NONSENSE_DIALOGUES = [
    "The sky beneath your feet whispers.",
    "Green tastes like triangles today.",
    "You are dreaming of a dreamer's dream.",
    "They buried the concept of time in Room (1,1).",
    "Beware the sponge that remembers.",
    "Laughter echoes backward here.",
    "Shadows argue about your intentions.",
    "This room is full of unspoken punctuation.",
    "All is one, and one is none.",
    "Your reflection walked off two minutes ago."
]

# Predefined comments Dungeon Master uses for game events (WIP)
DM_COMMENTS = {
    "invalid_command": "That's not a valid move, traveler.",
    "dead_end": "The way is shut.",
    "search_result": "You rummage around...",
    "artifact_found": "You've discovered a sacred artifact!",
    "death_warning": "This room reeks of danger.",
}

# Allowed player commands for reference (WIP)
PLAYER_NAME = ""
PLAYER_COMMANDS = [
    "go north", "go south", "go east", "go west",
    "search", "inventory", "quit"
]

# Dungeon Master class to manage dialogues and choices  (WIP)

class DM:
    def __init__(self, dialogues):
        self.dialogues = dialogues # Dialogue data passed in
        self.current_id = 'start'  # Start at the initial dialogue


    def speak(self):
        # Print current dialogue text and return list of options if any
        dialogue = self.dialogues.get(self.current_id)
        if not dialogue:
            print("Dungeon Master has nothing more to say.")
            return []

        print(f"Dungeon Master: {dialogue['text']}")
        return dialogue.get('options', [])

    def next(self, choice_index=None):
        # Move to next dialogue, optionally based on player choice
        dialogue = self.dialogues.get(self.current_id)
        if not dialogue:
            self.current_id = None
            return

        next_id = dialogue.get('next_id')

        if isinstance(next_id, list):
            # Choose next dialogue branch by player choice index
            if choice_index is not None and 0 <= choice_index < len(next_id):
                self.current_id = next_id[choice_index]
            else:
                self.current_id = None
        else:
            self.current_id = next_id

        if self.current_id is None:
            print("Dungeon Master has nothing more to say.")

# Helper function to print Dungeon Master messages with optional pause
def dm_speak(key_or_text, pause=True):

    if key_or_text in DM_COMMENTS:
        print(f"\nDM: \"{DM_COMMENTS[key_or_text]}\"")
    else:
        print(f"\nDM: \"{key_or_text}\"")

    if pause:
        input("\n(Press Enter to continue...)")

# Function to prompt player to choose from options
def player_reply(options):

    if not options:
        print("Herb: ...")
        return None

    print("Choose your reply:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    while True:
        choice = input("Enter choice number: ").strip()
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(options):
                print(f"{PLAYER_NAME}: {options[idx]}")
                return idx
        print("Invalid choice, try again.")
