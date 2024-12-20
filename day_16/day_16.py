'''
lets do an 0-1 bfs

using this as the base
https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

make dict for neigbhours for each direction
make dict for offset val for each direction


part 2 
lets create a prev dict that points to parent

start at S and recursively traverse until we can get find all combinations to
E and return count of num nodes traversed

'''
from collections import defaultdict, deque
import time

# Direction dictionaries
direction_dict = {
    'East': (0, 1),
    'West': (0, -1),
    'South': (1, 0),
    'North': (-1, 0)
}

# Direction neighbours dictionaries
direction_neighbours = {
    'East': ['East', 'South', 'North'],
    'West': ['West', 'South', 'North'],
    'South': ['East', 'South', 'West'],
    'North': ['East', 'North', 'West']
}


def parse_input():
    """Parse the input grid from the file and locate start (S) and end (E) positions."""
    with open("day_16.txt") as f:
        grid = f.read().splitlines()
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    start_position = None
    end_position = None

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "S":
                start_position = (r, c)
            if grid[r][c] == "E":
                end_position = (r, c)

    return grid, rows, cols, start_position, end_position


def is_valid(grid, r, c, rows, cols):
    """Check if the given position is valid in the grid."""
    return 0 <= r < rows and 0 <= c < cols and grid[r][c] != "#"


def bfs(grid, rows, cols, start_pos, end_pos):
    """Perform 0-1 BFS to find the minimum cost from start to end."""
    q = deque()
    dist = defaultdict(lambda: float('inf'))

    # Start in all directions from the start position
    for initial_dir in ['East', 'North', 'South']:
        initial_cost = 0 if initial_dir == 'East' else 1000
        q.append((initial_cost, start_pos[0], start_pos[1], initial_dir))
        dist[(start_pos[0], start_pos[1])] = initial_cost

    while q:
        curr_cost, curr_r, curr_c, curr_direction = q.popleft()

        if (curr_r, curr_c) == end_pos:
            return curr_cost  # Return as soon as the shortest path to the end is found

        # Explore neighbors
        for next_direction in direction_neighbours[curr_direction]:
            dr, dc = direction_dict[next_direction]
            next_r, next_c = curr_r + dr, curr_c + dc

            if not is_valid(grid, next_r, next_c, rows, cols):
                continue

            # Calculate cost
            next_cost = curr_cost + 1 + (1000 if next_direction != curr_direction else 0)

            if next_cost < dist[(next_r, next_c)]:
                dist[(next_r, next_c)] = next_cost
                if next_direction == curr_direction:
                    q.appendleft((next_cost, next_r, next_c, next_direction))
                else:
                    q.append((next_cost, next_r, next_c, next_direction))

    return float('inf')  # Return infinity if no path is found


def bfs2(grid, rows, cols, start_pos, end_pos):
    """Perform BFS while tracking paths for backtracking."""
    q = deque()
    dist = defaultdict(lambda: float('inf'))
    best_cost = float('inf')
    backtrack = defaultdict(set)
    end_states = set()

    for initial_dir in ['East', 'North', 'South', 'West']:
        initial_cost = 0 if initial_dir == 'East' else 1000
        q.append((initial_cost, start_pos[0], start_pos[1], initial_dir))
        dist[(start_pos[0], start_pos[1], initial_dir)] = initial_cost

    while q:
        curr_cost, curr_r, curr_c, curr_direction = q.popleft()

        if curr_cost > dist[(curr_r, curr_c, curr_direction)]:
            continue

        if (curr_r, curr_c) == end_pos:
            if curr_cost < best_cost:
                best_cost = curr_cost
                end_states.clear()
            if curr_cost == best_cost:
                end_states.add((curr_r, curr_c, curr_direction))

        for next_direction in direction_neighbours[curr_direction]:
            dr, dc = direction_dict[next_direction]
            next_r, next_c = curr_r + dr, curr_c + dc

            if not is_valid(grid, next_r, next_c, rows, cols):
                continue

            next_cost = curr_cost + 1 + (1000 if next_direction != curr_direction else 0)

            if next_cost < dist[(next_r, next_c, next_direction)]:
                dist[(next_r, next_c, next_direction)] = next_cost
                backtrack[(next_r, next_c, next_direction)].clear()
            if next_cost == dist[(next_r, next_c, next_direction)]:
                backtrack[(next_r, next_c, next_direction)].add((curr_r, curr_c, curr_direction))
                if next_direction == curr_direction:
                    q.appendleft((next_cost, next_r, next_c, next_direction))
                else:
                    q.append((next_cost, next_r, next_c, next_direction))

    return best_cost, end_states, backtrack


def find_all_nodes(visited_set, backtrack_graph):
    """Find all nodes traversed in shortest paths using backtracking."""
    visited = set(visited_set)

    def dfs(node):
        for neighbor in backtrack_graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                dfs(neighbor)

    for state in visited_set:
        dfs(state)

    return {(r, c) for r, c, _ in visited}


def mark_best_paths(grid, path_positions):
    """Mark the best path positions in the grid."""
    marked_grid = [list(row) for row in grid]
    for r, c in path_positions:
        if marked_grid[r][c] not in '#SE':
            marked_grid[r][c] = 'O'
    return marked_grid


def print_grid(grid):
    """Print the grid."""
    for row in grid:
        print(''.join(row))


def question1():
    grid, rows, cols, start_position, end_position = parse_input()
    start_time = time.time()
    res = bfs(grid, rows, cols, start_position, end_position)
    end_time = time.time()
    print(f"Minimum cost: {res}")
    print(f"Runtime: {end_time - start_time:.4f} seconds")


def question2():
    grid, rows, cols, start_position, end_position = parse_input()
    start_time = time.time()
    _, visited_set, backtrack_graph = bfs2(grid, rows, cols, start_position, end_position)
    best_path_positions = find_all_nodes(visited_set, backtrack_graph)
    end_time = time.time()
    print(f"Number of tiles in best paths: {len(best_path_positions)}")
    print(f"Runtime: {end_time - start_time:.4f} seconds")


# Run the questions
question1()
question2()
