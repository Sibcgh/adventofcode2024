'''
looks like a bfs
how do we want to do this?


first lets work on the example
lets construct an inplace grid
of 0-6 width and height of '.'

parse over input and generate a new graph where
we replace each '.' with corresponding '#'

'''
import time
from collections import deque


def parse_input(filename="day_18.txt"):
    """Parse input from the file and transform it into a set of (x, y) tuples."""
    with open(filename) as f:
        data = f.read().strip().splitlines()
    # Convert lines into a list of tuples (x, y) coordinates
    return [(int(x.split(",")[0]), int(x.split(",")[1])) for x in data]


def create_2d_grid(length=7, width=7):
    """Create a 2D grid initialized with '.' (safe positions)."""
    return [["." for _ in range(width)] for _ in range(length)], length, width


def fill_grid_vals(grid, walls, slice_count):
    """Fill grid with '#' up to the specified slice_count based on wall positions."""
    for c, r in walls[:slice_count]:
        grid[r][c] = "#"


def is_valid(r, c, rows, cols):
    """Check if the coordinates are within the grid bounds."""
    return 0 <= r < rows and 0 <= c < cols


def bfs(grid, rows, cols):
    """Perform BFS to count the number of steps required to reach the bottom-right corner."""
    visited = set()
    queue = deque([(0, 0, 0)])  # Queue stores (row, col, step_count)

    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]  # 4 possible directions

    while queue:
        curr_r, curr_c, curr_steps = queue.popleft()

        # Skip if already visited
        if (curr_r, curr_c) in visited:
            continue

        visited.add((curr_r, curr_c))

        # Return step count once we reach the bottom-right corner
        if (curr_r, curr_c) == (rows - 1, cols - 1):
            return curr_steps 

        for offset_r, offset_c in directions:
            next_r, next_c = curr_r + offset_r, curr_c + offset_c

            # Add valid neighbor to the queue
            if is_valid(next_r, next_c, rows, cols) and (next_r, next_c) not in visited and grid[next_r][next_c] != "#":
                queue.append((next_r, next_c, curr_steps + 1))

    return 0  # Return 0 if no path is found


def question1():
    walls_list = parse_input()
    grid, rows, cols = create_2d_grid(length=71, width=71)

    start_time = time.time()
    fill_grid_vals(grid, walls_list, slice_count=1028)
    res = bfs(grid, rows, cols)
    end_time = time.time()

    print(f"Answer for Question 1: {res}")
    print(f"Execution time for Question 1: {end_time - start_time:.6f} seconds")


def question2():
    walls_list = parse_input()
    grid, rows, cols = create_2d_grid(length=71, width=71)

    start_time = time.time()
    res = 0

    for index in range(1, len(walls_list) + 1):
        fill_grid_vals(grid, walls_list, slice_count=index)
        if not bfs(grid, rows, cols):  # If no path is found
            res = index  # Record the index that causes the path to be blocked
            break

    end_time = time.time()

    print(f"Answer for Question 2: {walls_list[res - 1]}")  # Print the coordinates of the blocking byte
    print(f"Index that blocks the path: {res - 1}")
    print(f"Execution time for Question 2: {end_time - start_time:.6f} seconds")


question1()
question2()
