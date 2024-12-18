'''
lets do an 0-1 bfs

make dict for neigbhours for each direction
make dict for offset val for each direction
'''

import time
from collections import defaultdict, deque

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
    with open("day_15.txt") as f:
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

# Utility function
def is_valid(grid, r, c, rows, cols):
    return 0 <= r < rows and 0 <= c < cols and grid[r][c] != "#"


'''
TODO fix 01 bfs function to return 
final generate score
'''
def bfs(self, grid):
    
    '''
    soln using bfs 0-1
    if we have nodes that only have weights that can be either 
    0 or 1 we can shift to using a bfs instead of djikstra
    this will improve our runtime from mnlogmn to mn 

    https://cp-algorithms.com/graph/01_bfs.html
    '''
    rows = len(grid)
    cols = len(grid[0])

    '''
    TODO
    fix this
    '''
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    # Distance array to track minimum obstacles encountered to reach each cell
    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[0][0] = grid[0][0]  # Initialize start position

    q = deque([(dist[0][0], 0, 0)])  # Store (obstacle_count, row, col)

    while q:
        curr_count, curr_r, curr_c = q.popleft()

        # If we reach the bottom-right corner, return the result
        if (curr_r, curr_c) == (rows - 1, cols - 1):
            return curr_count

        for dx, dy in directions:
            next_r, next_c = curr_r + dx, curr_c + dy
            if is_valid(next_r, next_c):
                next_count = curr_count + grid[next_r][next_c]
                if next_count < dist[next_r][next_c]:
                    dist[next_r][next_c] = next_count
                    # Use deque's appendleft for 0-weight cells to prioritize them
                    if grid[next_r][next_c] == 0:
                        q.appendleft((next_count, next_r, next_c))
                    else:
                        q.append((next_count, next_r, next_c))

    return 0


'''

'''
