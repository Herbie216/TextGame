# Alot of work to do here now that the player moves around!!!

def print_map(game_map, player):
    for r in range(game_map.rows):
        row_display = ""
        for c in range(game_map.cols):
            if r == player.row and c == player.col:
                row_display += f"{player.initial} "
            else:
                room = game_map.get_room(r, c)
                if room.is_artifact_room and room.discovered:
                    row_display += "* "
                else:
                    row_display += ". "
        print(row_display.strip())
    print()

def print_welcome():
    """
    Print the welcome message at the start of the game.
    """
    print("Welcome to A Hint from the Past!")

def print_room_description(room):
    """
    Print the description of a given room.
    """
    print(room.description)

def print_artifacts_list(game_map):
    """
    Print a list of all artifact rooms and their coordinates.
    Used for getting started, Maybe rework it later
    """
    artifacts = []
    for r in range(game_map.rows):
        for c in range(game_map.cols):
            room = game_map.get_room(r, c)
            if room and room.is_artifact_room:
                artifacts.append((r, c, room.artifact))
    print("Artifacts found in the map:")
    for r, c, artifact in artifacts:
        print(f" - {artifact} at ({r},{c})")

def text_to_binary(text):
    """
    Convert a string of text to a string of binary codes separated by spaces.
    (Trying something)
    """
    return ' '.join(format(ord(c), '08b') for c in text)

def print_binary_hint(hint_text):
    """
    Print a hint as a binary encoded string.
    (Trying something)
    """
    binary_hint = text_to_binary(hint_text)
    print(f"Binary hint: {binary_hint}")

def interact_with_player():
    """
    Interact with the player, giving a binary hint and responding based on input.
    (Trying something)
    """
    print_binary_hint("You are close. Try going right.")
    while True:
        reply = input("Are you a computer? (yes/no): ").strip().lower()
        if reply in ['no', 'n', 'i am not a computer', 'not']:
            print("Okay, human! Here's a clearer hint: Go right from here!")
            break
        elif reply in ['yes', 'y']:
            print("Good! Then decipher the code carefully.")
            break
        else:
            print("Please answer yes or no.")
