"""
Module to create and print a simple grid map with artifact locations.

Constants:
- ROWS, COLS: Dimensions of the map grid.
- artifact_coords: Coordinates of artifact rooms marked with 'A'.

Functions:
- generate_map_grid(): Returns a 2D list representing the map grid.
- print_map(grid): Prints the map grid to the console.
"""

ROWS = 5
COLS = 11

# Coordinates of artifact rooms
artifact_coords = [
    (1, 3),
    (2, 2), (2, 3), (2, 4),
    (3, 1),
    (3, 5),
    (1, 7),
    (2, 6), (2, 7), (2, 8),
    (3, 9)
]

def generate_map_grid():
    """
    Generate a 2D grid representing the map.
    'A' marks artifact rooms; '.' marks empty rooms.
    """
    grid = [['.' for _ in range(COLS)] for _ in range(ROWS)]
    for (r, c) in artifact_coords:
        grid[r][c] = 'A'
    return grid

def print_map(grid):
    """
    Print the map grid to the console.
    """
    for row in grid:
        print(' '.join(row))
