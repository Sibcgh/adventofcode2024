'''
lets just brute force this 
'''
import time
from collections import defaultdict


# Set to store unique antinode locations
antinodes = set()
antinodes_2 = set()


def is_valid(x, y, rows, cols):
    """Check if the coordinates are within the grid bounds."""
    return 0 <= x < rows and 0 <= y < cols


def parse_file(filename="day_8.txt"):
    """Read the input file and return the grid, number of rows and columns."""
    with open(filename) as f:
        grid = f.read().splitlines()

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    return grid, rows, cols


def get_inputs():
    """Parse the input file and return the rows, cols, and a dictionary of antennas by frequency."""
    grid, rows, cols = parse_file()
    nodes = defaultdict(list)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != ".":
                nodes[grid[r][c]].append((r, c))

    return rows, cols, nodes


def get_antinodes(node1, node2, rows, cols):
    """Calculate the antinode created by two antennas (Part 1)."""
    x_1, y_1 = node1
    x_2, y_2 = node2

    # Similar to finding using slope
    new_x = x_2 + (x_2 - x_1)
    new_y = y_2 + (y_2 - y_1)
    if is_valid(new_x, new_y, rows, cols):
        antinodes.add((new_x, new_y))


def get_antinodes_repeating(node1, node2, rows, cols):
    """Calculate the repeating antinodes created by two antennas (Part 2)."""
    x_1, y_1 = node1
    x_2, y_2 = node2
    # Add the initial positions of the antennas as antinodes
    if is_valid(x_1, y_1, rows, cols):
        antinodes_2.add((x_1, y_1))
    if is_valid(x_2, y_2, rows, cols):
        antinodes_2.add((x_2, y_2))

    # Calculate other antinodes along the line formed by the two antennas
    new_x, new_y = x_2 + (x_2 - x_1), y_2 + (y_2 - y_1)
    while is_valid(new_x, new_y, rows, cols):
        antinodes_2.add((new_x, new_y))
        new_x += (x_2 - x_1)
        new_y += (y_2 - y_1)


def process_antennas(nodes, rows, cols, part=1):
    """Process all antennas and calculate antinodes for Part 1 or Part 2."""
    for _, node_lists in nodes.items():
        for i in range(len(node_lists)):
            for j in range(i + 1, len(node_lists)):
                a = node_lists[i]
                b = node_lists[j]
                if part == 1:
                    get_antinodes(a, b, rows, cols)
                    get_antinodes(b, a, rows, cols)
                else:
                    get_antinodes_repeating(a, b, rows, cols)
                    get_antinodes_repeating(b, a, rows, cols)


def question_one():
    """Calculate and print the number of unique antinodes for Part 1."""
    rows, cols, nodes = get_inputs()

    # Start timing Part 1
    start_time = time.time()
    
    process_antennas(nodes, rows, cols, part=1)

    # End timing Part 1
    end_time = time.time()
    print(f"Part 1: {len(antinodes)}")
    print(f"Part 1 execution time: {end_time - start_time:.6f} seconds")


def question_two():
    """Calculate and print the number of unique antinodes for Part 2."""
    rows, cols, nodes = get_inputs()

    # Start timing Part 2
    start_time = time.time()

    process_antennas(nodes, rows, cols, part=2)

    # End timing Part 2
    end_time = time.time()
    print(f"Part 2: {len(antinodes_2)}")
    print(f"Part 2 execution time: {end_time - start_time:.6f} seconds")


# Run both parts of the puzzle with timers
question_one()
question_two()
