# Map Building and Helper Functions

from classes import Room, Map
from typing import Tuple, List
from map import artifact_coords, artifact_names, player_start_coords
import random

def create_rooms(map_instance: Map, rows: int, cols: int) -> None:
    for r in range(rows):
        for c in range(cols):
            room = Room(r, c, description=f"Room at ({r},{c})")
            map_instance.add_room(room)

def add_artifacts(map_instance: Map, coords: List[Tuple[int, int]], names: List[str]) -> None:
    for coord, name in zip(coords, names):
        row, col = coord
        room = map_instance.get_room(row, col)
        if room:
            room.artifact = name
            room.description += f" This room holds the artifact: {name}."
            room.is_artifact_room = True

def assign_hint_and_nonsense_rooms(map_instance: Map, hint_count=10, nonsense_count=10) -> Tuple[List[Room], List[Room]]:
    all_rooms = [room for room in map_instance.rooms.values() if not room.is_artifact_room]
    random.shuffle(all_rooms)
    hint_rooms = all_rooms[:hint_count]
    nonsense_rooms = all_rooms[hint_count:hint_count + nonsense_count]

    for room in hint_rooms:
        room.is_hint_room = True
        room.description += " A strange feeling washes over you... Something important is nearby."

    for room in nonsense_rooms:
        room.is_nonsense_room = True
        room.description += " Your senses distort... None of this feels real."

    return hint_rooms, nonsense_rooms


def connect_rooms(map_instance: Map, rows: int, cols: int) -> None:
    for r in range(rows):
        for c in range(cols):
            room = map_instance.get_room(r, c)
            if not room:
                continue
            directions = {
                'north': (r - 1, c),
                'east': (r, c + 1),
                'south': (r + 1, c),
                'west': (r, c - 1),
            }
            for direction, (nr, nc) in directions.items():
                neighbor = map_instance.get_room(nr, nc)
                if neighbor:
                    map_instance.connect_rooms(room, direction, neighbor)

def build_game_map() -> Tuple[Map, List[Tuple[int, int]], List[Room], List[Room]]:
    rows, cols = 5, 11
    map_instance = Map(rows, cols)

    create_rooms(map_instance, rows, cols)
    add_artifacts(map_instance, artifact_coords, artifact_names)
    hint_rooms, nonsense_rooms = assign_hint_and_nonsense_rooms(map_instance)

    connect_rooms(map_instance, rows, cols)

    return map_instance, artifact_coords, hint_rooms, nonsense_rooms

if __name__ == "__main__":
    game_map, artifacts, hints, nonsense = build_game_map()
    total_rooms = len(game_map.rooms) * len(game_map.rooms[0])
    print(f"Map with {total_rooms} rooms built.")
    print(f"Artifacts placed: {len(artifacts)}")
    print(f"Hint rooms assigned: {len(hints)}")
    print(f"Nonsense rooms assigned: {len(nonsense)}")
