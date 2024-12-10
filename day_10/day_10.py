'''
lets do BFS


we find all the trail heads and put them in a list

we then iterate overall trailheads and find how many trails that end in 9 we can find 
from this trail head

return count

do this for every trailhead we find and keep running count

return it
'''
import time
from collections import defaultdict, deque


def is_valid(x, y, rows, cols):
    """Check if the coordinates are within the grid bounds."""
    return 0 <= x < rows and 0 <= y < cols


def parse_file(filename="day_10.txt"):
    """Read the input file and return the grid, number of rows, and columns."""
    with open(filename) as f:
        grid = f.read().splitlines()

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    return grid, rows, cols


def bfs(grid, rows, cols, start):
    """Perform BFS to count the number of paths that end at a '9' cell starting from 'start'."""
    count = 0
    visited = set()
    queue = deque([start])

    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]  # 4 possible directions

    while queue:
        curr_r, curr_c = queue.popleft()

        # Skip if already visited
        if (curr_r, curr_c) in visited:
            continue

        visited.add((curr_r, curr_c))

        if grid[curr_r][curr_c] == '9':
            count += 1
            continue  # Continue to explore other paths

        for offset_r, offset_c in directions:
            next_r, next_c = curr_r + offset_r, curr_c + offset_c

            if is_valid(next_r, next_c, rows, cols) and (next_r, next_c) not in visited and grid[next_r][next_c] != "." and \
                int(grid[next_r][next_c]) == 1 + int(grid[curr_r][curr_c]):
                queue.append((next_r, next_c))

    return count


def bfs2(grid, rows, cols, start):
    """Perform BFS and count the distinct paths to reach '9' cells."""
    ways = defaultdict(int)
    ways[start] = 1  # Start with 1 way to reach the starting point

    queue = deque([start])
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]  # 4 possible directions

    while queue:
        curr_r, curr_c = queue.popleft()

        for offset_r, offset_c in directions:
            next_r, next_c = curr_r + offset_r, curr_c + offset_c

            if is_valid(next_r, next_c, rows, cols) and grid[next_r][next_c] != "." and \
                int(grid[next_r][next_c]) == 1 + int(grid[curr_r][curr_c]):

                if ways[(next_r, next_c)] == 0:
                    queue.append((next_r, next_c))

                # Accumulate the number of ways to reach this cell
                ways[(next_r, next_c)] += ways[(curr_r, curr_c)]

    # Count distinct paths that end at '9'
    return sum(ways[(r, c)] for (r, c), count in ways.items() if grid[r][c] == '9')


def find_zeroes(grid, rows, cols):
    """Find all the cells with '0' which serve as trailheads."""
    return [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == "0"]


# Parse the grid from the file
grid, rows, cols = parse_file()

# Find all trailheads (i.e., '0' cells)
trailheads = find_zeroes(grid, rows, cols)

# Measure execution time for bfs (first method)
start_time = time.time()
total_paths = sum(bfs(grid, rows, cols, start) for start in trailheads)
bfs_time = time.time() - start_time
print(f"Total paths (bfs): {total_paths}")
print(f"Time for bfs: {bfs_time:.6f} seconds")

# Measure execution time for bfs2 (second method)
start_time = time.time()
distinct_paths = sum(bfs2(grid, rows, cols, start) for start in trailheads)
bfs2_time = time.time() - start_time
print(f"Distinct paths (bfs2): {distinct_paths}")
print(f"Time for bfs2: {bfs2_time:.6f} seconds")