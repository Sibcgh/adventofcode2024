from collections import deque
import time

def parse_input(filename="day_20.txt"):
    """
    Parse the input grid from the file and locate start (S) and end (E) positions.
    Returns the grid, dimensions, and start/end coordinates.
    """
    with open(filename) as f:
        grid = f.read().splitlines()

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    start_position = None
    end_position = None

    # Locate the start (S) and end (E) positions
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "S":
                start_position = (r, c)
            elif grid[r][c] == "E":
                end_position = (r, c)

    return grid, rows, cols, start_position, end_position


def is_valid(r, c, rows, cols):
    """Check if the coordinates are within the grid bounds."""
    return 0 <= r < rows and 0 <= c < cols


def bfs(grid, rows, cols, start_position, end_position):
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    start_r, start_c = start_position

    # Initialize distances
    dists = [[-1] * cols for _ in range(rows)]
    dists[start_r][start_c] = 0

    # BFS queue initialization
    queue = deque([(start_r, start_c)])

    while queue:
        curr_r, curr_c = queue.popleft()

        # If we reached the end, return its distance
        if grid[curr_r][curr_c] == end_position:
            break

        for dr, dc in directions:
            next_r, next_c = curr_r + dr, curr_c + dc
            if not is_valid(next_r, next_c, rows, cols):
                continue
            if grid[next_r][next_c] == "#" or dists[next_r][next_c] != -1:
                continue
            dists[next_r][next_c] = dists[curr_r][curr_c] + 1
            queue.append((next_r, next_c))

    return dists


def search(grid, rows, cols, start_position, end_position):
    dists = bfs(grid, rows, cols, start_position, end_position)

    count = 0
    neigh_directions = [(2, 0), (1, 1), (0, 2), (-1, 1)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "#":
                continue
            for dr, dc in neigh_directions:
                next_r, next_c = r + dr, c + dc
                if not is_valid(next_r, next_c, rows, cols):
                    continue
                if grid[next_r][next_c] == "#":
                    continue
                if abs(dists[r][c] - dists[next_r][next_c]) >= 102:
                    count += 1

    print(count)


def search2(grid, rows, cols, start_position, end_position):
    dists = bfs(grid, rows, cols, start_position, end_position)
    count = 0
    multipliers = [(1, 1), (-1, 1), (1, -1), (-1, -1)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "#":
                continue
            for radius in range(2, 21):
                unique_positions = set()
                for dr in range(radius + 1):
                    dc = radius - dr
                    for multiplier_r, multiplier_c in multipliers:
                        unique_positions.add((dr * multiplier_r, dc * multiplier_c))
                
                for dr, dc in unique_positions:
                    next_r, next_c = r + dr, c + dc
                    if not is_valid(next_r, next_c, rows, cols):
                        continue
                    if grid[next_r][next_c] == "#":
                        continue
                    if (dists[r][c] - dists[next_r][next_c]) >= 100 + radius:
                        count += 1

    print(count)


def question1():
    grid, rows, cols, start_position, end_position = parse_input()
    
    start_time = time.time()
    search(grid, rows, cols, start_position, end_position)
    end_time = time.time()
    
    print(f"Question 1 execution time: {end_time - start_time:.4f} seconds")


def question2():
    grid, rows, cols, start_position, end_position = parse_input()
    
    start_time = time.time()
    search2(grid, rows, cols, start_position, end_position)
    end_time = time.time()
    
    print(f"Question 2 execution time: {end_time - start_time:.4f} seconds")


question1()
question2()
