'''
lets do an 0-1 bfs

using this as the base
https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

make dict for neigbhours for each direction
make dict for offset val for each direction
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
    # Initialize visited set to track (position, direction) combinations
    visited = set()
    
    # Use a priority queue (deque in this case) to store (cost, row, col, direction)
    q = deque()
    
    # Start facing East and try all initial directions with appropriate costs
    for initial_dir in ['East', 'North', 'South']:
        initial_cost = 0 if initial_dir == 'East' else 1000  # Cost 1000 if we need to turn first
        q.append((initial_cost, start_pos[0], start_pos[1], initial_dir))
    
    # Dictionary to store minimum cost for each (position, direction) combination
    dist = defaultdict(lambda: float('inf'))
    for dir in ['East', 'North', 'South']:
        dist[(start_pos[0], start_pos[1], dir)] = 0 if dir == 'East' else 1000

    min_end_cost = float('inf')
    
    while q:
        curr_cost, curr_r, curr_c, curr_direction = q.popleft()
        
        # Skip if we've seen this state with a lower cost
        if curr_cost > dist[(curr_r, curr_c, curr_direction)]:
            continue
            
        # If we reached the end, update minimum cost if needed
        if (curr_r, curr_c) == end_pos:
            min_end_cost = min(min_end_cost, curr_cost)
            continue

        # Try all possible next directions based on current direction
        for next_direction in direction_neighbours[curr_direction]:
            dr, dc = direction_dict[next_direction]
            next_r, next_c = curr_r + dr, curr_c + dc
            
            if not is_valid(grid, next_r, next_c, rows, cols):
                continue
                
            # Calculate new cost - 1000 for rotation, 1 for moving forward
            next_cost = curr_cost + 1 + (1000 if next_direction != curr_direction else 0)
            
            # If we found a better path to this state
            if next_cost < dist[(next_r, next_c, next_direction)]:
                dist[(next_r, next_c, next_direction)] = next_cost
                # Prioritize straight moves over turns
                if next_direction == curr_direction:
                    q.appendleft((next_cost, next_r, next_c, next_direction))
                else:
                    q.append((next_cost, next_r, next_c, next_direction))

    return min_end_cost

grid, rows, cols, start_position, end_position = parse_input()
res = bfs(grid, rows, cols, start_position, end_position)
print(res)