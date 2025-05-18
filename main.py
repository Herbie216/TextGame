from classes import Player
from build_map import build_game_map
import print_message as pm
from dungeon_master import DM, player_reply

def main():
    # Build the game map and get special room coordinates
    game_map, artifact_coords, hint_rooms, nonsense_rooms = build_game_map()

    # Get player's name and use the first letter as their initial
    player_name = input("Enter your name, Traveler: ").strip()
    player_initial = player_name[0].upper() if player_name else 'P'

    # Initialize the player at starting position with the game map reference
    player = Player(start_row=0, start_col=0, game_map=game_map, initial=player_initial)

    print("Welcome to A Hint from the Past!")
    pm.print_map(game_map, player)

    # Sample dialogue tree for dungeon master interactions (WIP)
    dialogues = {
        "start": {
            "text": "You stand before the dark portal. Enter?",
            "options": ["Yes", "No"],
            "next_id": ["enter_portal", "dont_enter"]
        },
        "enter_portal": {
            "text": "You step through the portal and find a treasure!",
            "options": [],
            "next_id": None
        },
        "dont_enter": {
            "text": "You decide to stay safe and walk away.",
            "options": [],
            "next_id": None
        }
    }

    # Initialize the Dungeon Master with dialogue data (WIP)
    dm = DM(dialogues)

    while True:
        # Ask player for movement input or quit command
        command = input("Enter direction to move (north, south, east, west) or 'quit': ").strip().lower()
        if command == 'quit':
            print("I didn't want to play with you anyway!")
            break

        # Move the player and update the map display
        player.move(command)
        pm.print_map(game_map, player)

        # Trigger a dungeon master dialogue on a specific map tile (WIP)
        if (player.row, player.col) == (2, 3):
            options = dm.speak()
            if options:
                choice = player_reply(options)
                dm.next(choice)

if __name__ == "__main__":
    main()
