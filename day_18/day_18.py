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


def remove_wall(grid, walls, index):
    """Remove a wall at a specific index from walls."""
    c, r = walls[index]
    grid[r][c] = "."  # Replace the wall '#' with '.'


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

    # Fill grid initially with all walls
    fill_grid_vals(grid, walls_list, slice_count=len(walls_list))

    start_time = time.time()
    res = 0

    # Use binary search to find the index at which a path becomes possible
    left, right = 0, len(walls_list) - 1

    while left <= right:
        mid = (left + right) // 2
        # Create a new grid and fill it up to the mid index
        grid, _, _ = create_2d_grid(length=71, width=71)
        fill_grid_vals(grid, walls_list, slice_count=mid)

        if bfs(grid, rows, cols) != 0:  # If a valid path exists
            res = mid  # Record the mid index
            right = mid - 1  # Try to find a smaller index
        else:
            left = mid + 1  # Try to find a larger index

    end_time = time.time()

    print(f"Answer for Question 2: {walls_list[res]}")
    print(f"Index that makes a path possible: {res}")
    print(f"Execution time for Question 2: {end_time - start_time:.6f} seconds")


question1()
question2()
