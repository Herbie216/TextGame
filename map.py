# Constants

ROWS = 5
COLS = 11

artifact_coords = [
    # Left A
    (1, 3), (2, 2), (2, 3), (2, 4), (3, 1),
    # Shared middle
    (3, 5),
    # Right A
    (1, 7), (2, 6), (2, 7), (2, 8), (3, 9)
]

artifact_names = [
    "A - Left Top", "A - Left Mid Left", "A - Left Mid Mid", "A - Left Mid Right", "A - Left Bottom",
    "Shared Artifact",
    "A - Right Top", "A - Right Mid Left", "A - Right Mid Mid", "A - Right Mid Right", "A - Right Bottom"
]

player_start_coords = (0, 0)

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
