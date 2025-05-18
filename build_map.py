from classes import Room, Map

# Your artifact coordinates and names in order
artifact_coords = [
    # Left A
    (1, 3), (2, 2), (2, 3), (2, 4), (3, 1),

    # Shared middle
    (3, 5),

    # Right A
    (1, 7), (2, 6), (2, 7), (2, 8), (3, 9)
]

artifact_names = [
    "A - Left Top",
    "A - Left Mid Left",
    "A - Left Mid Mid",
    "A - Left Mid Right",
    "A - Left Bottom",

    "Shared Artifact",

    "A - Right Top",
    "A - Right Mid Left",
    "A - Right Mid Mid",
    "A - Right Mid Right",
    "A - Right Bottom"
]

def build_game_map():
    rows, cols = 5, 11
    game_map = Map(rows, cols)

    # Create all rooms
    for r in range(rows):
        for c in range(cols):
            room = Room(r, c, description=f"Room at ({r},{c})")
            game_map.add_room(room)

    # Add artifacts to designated rooms
    for coord, name in zip(artifact_coords, artifact_names):
        row, col = coord
        room = game_map.get_room(row, col)
        if room:
            room.artifact = name
            room.description += f" This room holds the artifact: {name}."
            room.is_artifact_room = True  # Flag to identify artifact rooms

    # Connect adjacent rooms (N, S, E, W)
    for r in range(rows):
        for c in range(cols):
            room = game_map.get_room(r, c)
            if not room:
                continue

            # North
            north_room = game_map.get_room(r - 1, c)
            if north_room:
                game_map.connect_rooms(room, 'north', north_room)

            # East
            east_room = game_map.get_room(r, c + 1)
            if east_room:
                game_map.connect_rooms(room, 'east', east_room)

            # South
            south_room = game_map.get_room(r + 1, c)
            if south_room:
                game_map.connect_rooms(room, 'south', south_room)

            # West
            west_room = game_map.get_room(r, c - 1)
            if west_room:
                game_map.connect_rooms(room, 'west', west_room)

    return game_map


def list_artifact_rooms(game_map):
    """
    Return a list of tuples (row, col, artifact_name) for all artifact rooms in the map.
    """
    artifacts = []
    for r in range(game_map.rows):
        for c in range(game_map.cols):
            room = game_map.get_room(r, c)
            if room and room.is_artifact_room:
                artifacts.append((r, c, room.artifact))
    return artifacts
