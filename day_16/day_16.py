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
import heapq

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
    return 0 <= r < rows and 0 <= c < cols and grid[r][c] != "#"

def bfs(grid, rows, cols, start_pos, end_pos):
    # Use a deque to store (cost, row, col, direction)
    q = deque()
    
    # Start facing East and try all initial directions with appropriate costs
    for initial_dir in ['East', 'North', 'South']:
        initial_cost = 0 if initial_dir == 'East' else 1000  # Cost 1000 if we need to turn first
        q.append((initial_cost, start_pos[0], start_pos[1], initial_dir))
    
    # Dictionary to store minimum cost for each (position, direction) combination
    dist = defaultdict(lambda: float('inf'))
    
    while q:
        curr_cost, curr_r, curr_c, curr_direction = q.popleft()
        
        # Skip if we've seen this state with a lower cost
        if curr_cost > dist[(curr_r, curr_c)]:
            continue
            
        # If we reached the end, update minimum cost if needed
        if (curr_r, curr_c) == end_pos:
            return curr_cost

        # Try all possible next directions based on current direction
        for next_direction in direction_neighbours[curr_direction]:
            dr, dc = direction_dict[next_direction]
            next_r, next_c = curr_r + dr, curr_c + dc
            
            if not is_valid(grid, next_r, next_c, rows, cols):
                continue
                
            # Calculate new cost - 1000 for rotation, 1 for moving forward
            next_cost = curr_cost + 1 + (1000 if next_direction != curr_direction else 0)
            
            # If we found a better path to this state
            if next_cost < dist[(next_r, next_c)]:
                dist[(next_r, next_c)] = next_cost
                # Prioritize straight moves over turns
                if next_direction == curr_direction:
                    q.appendleft((next_cost, next_r, next_c, next_direction))
                else:
                    q.append((next_cost, next_r, next_c, next_direction))

    return 0

'''
lets edit this so it stores the shortest dist

we need an dict
key = curr node val = prev node so parent (can be multiple if several nodes have same cost)
initialize with None value for all keys
'''

def dijkstra(grid, rows, cols, start_pos, end_pos):
    pq = []
    # Start with all possible directions
    for initial_dir in ['East', 'West', 'South', 'North']:
        initial_cost = 0 if initial_dir == 'East' else 1000  # Cost 1000 if we need to turn first
        heapq.heappush(pq, (initial_cost, start_pos[0], start_pos[1], initial_dir))

    # Track minimum cost to reach each position from each direction
    dist = defaultdict(lambda: float('inf'))
    prev = defaultdict(set)  # Changed to set to avoid duplicates
    best_cost = float('inf')  # Track the best cost to end
    
    dist[(start_pos[0], start_pos[1])] = 0

    while pq:
        curr_cost, curr_r, curr_c, curr_dir = heapq.heappop(pq)
        curr_pos = (curr_r, curr_c)
        if (curr_pos) == (7, 4):
            print("here", curr_cost)
            print(pq)

        # If we've exceeded the best cost to end, skip
        if curr_cost > best_cost:
            continue

        # If we've reached the end, update best cost
        if curr_pos == end_pos:
            best_cost = min(best_cost, curr_cost)
            continue

        for next_dir in direction_neighbours[curr_dir]:
            dr, dc = direction_dict[next_dir]
            next_r, next_c = curr_r + dr, curr_c + dc
            next_pos = (next_r, next_c)

            if not is_valid(grid, next_r, next_c, rows, cols):
                continue

            next_cost = curr_cost + 1 + (1000 if next_dir != curr_dir else 0)

            # If this path is not worse than what we've seen, track it
            if next_cost <= dist[next_pos]:
                if next_cost < dist[next_pos]:
                    dist[next_pos] = next_cost
                    prev[next_pos] = set()  # Clear previous paths
                prev[next_pos].add(curr_pos)  # Add this path
                heapq.heappush(pq, (next_cost, next_r, next_c, next_dir))

    return prev, best_cost
'''
TODO
create function to iterate over all paths from End to Start
and count how many nodes we traversed along the path
'''
def find_all_best_paths(prev, end_pos, start_pos):
    best_paths = set()
    
    def dfs(curr_pos, visited):
        if curr_pos == start_pos:
            best_paths.update(visited)
            return True
            
        if curr_pos not in prev:
            return False
            
        found_path = False
        for parent in prev[curr_pos]:
            if parent not in visited:
                visited.add(parent)
                if dfs(parent, visited):
                    found_path = True
                visited.remove(parent)
        return found_path

    visited = {end_pos}
    dfs(end_pos, visited)
    return best_paths

def mark_best_paths(grid, path_positions):
    marked_grid = [list(row) for row in grid]
    for r, c in path_positions:
        if marked_grid[r][c] not in '#SE':
            marked_grid[r][c] = 'O'
    return marked_grid

def print_grid(grid):
    for row in grid:
        print(''.join(row))

def question1():
    grid, rows, cols, start_position, end_position = parse_input()
    res = bfs(grid, rows, cols, start_position, end_position)
    print(res)


def question2():
    grid, rows, cols, start_position, end_position = parse_input()
    prev_dict, best_cost = dijkstra(grid, rows, cols, start_position, end_position)
    
    # Find all positions that are part of any best path
    best_path_positions = find_all_best_paths(prev_dict, end_position, start_position)
    
    # Mark and print the result
    marked_grid = mark_best_paths(grid, best_path_positions)
    # print(f"Number of tiles in best paths: {len(best_path_positions)}")
    print('\n\n')
    print_grid(marked_grid)
    print(best_cost)

question2()

