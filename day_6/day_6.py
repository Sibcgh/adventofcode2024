'''
similar to LC 2061


parse input int a grid 

find starting position
have visited list of nodes the person travels 


do search 
move 1 unit every turn, add that cell to visit list
if we encounter # in our path keep rotating until next unit is not a square (while loop)
keep moving until we go out of bounds
return len of visit list in set



we return len(set(visited))

had a weird bug in part 2 wasnt iterating over proper set
'''
import time
from collections import defaultdict

def parse_file():
    with open("day_6.txt") as f:
        grid = f.read().splitlines()

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    return grid, rows, cols

def is_valid(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols

def search(grid, start_pos, rows, cols):
    directions = {
        0: (0, 1),   # Right
        1: (1, 0),   # Down
        2: (0, -1),  # Left
        3: (-1, 0)   # Up
    }

    visited = set()
    curr_x, curr_y, curr_dir = start_pos[0], start_pos[1], 3

    while is_valid(curr_x, curr_y, rows, cols):
        visited.add((curr_x, curr_y))
        offset_x, offset_y = directions[curr_dir]
        next_x, next_y = curr_x + offset_x, curr_y + offset_y

        for _ in range(4):  # Try all 4 directions
            if not is_valid(next_x, next_y, rows, cols):
                return visited

            if grid[next_x][next_y] in ['.', '^']:
                break

            curr_dir = (curr_dir + 1) % 4
            offset_x, offset_y = directions[curr_dir]
            next_x, next_y = curr_x + offset_x, curr_y + offset_y
        else:
            return visited

        curr_x, curr_y = next_x, next_y

    return visited

def check_cycle(grid, start_pos, rows, cols):
    directions = {
        0: (0, 1),   # Right
        1: (1, 0),   # Down
        2: (0, -1),  # Left
        3: (-1, 0)   # Up
    }

    visited = set()
    curr_x, curr_y, curr_dir = start_pos[0], start_pos[1], 3

    while is_valid(curr_x, curr_y, rows, cols):
        if (curr_x, curr_y, curr_dir) in visited:
            return True

        visited.add((curr_x, curr_y, curr_dir))
        offset_x, offset_y = directions[curr_dir]
        next_x, next_y = curr_x + offset_x, curr_y + offset_y

        for _ in range(4):  # Try all 4 directions
            if not is_valid(next_x, next_y, rows, cols):
                break

            if grid[next_x][next_y] in ['.', '^']:
                break

            curr_dir = (curr_dir + 1) % 4
            offset_x, offset_y = directions[curr_dir]
            next_x, next_y = curr_x + offset_x, curr_y + offset_y
        else:
            return False

        curr_x, curr_y = next_x, next_y

    return False

def get_inputs():
    grid, rows, cols = parse_file()

    start_pos = None

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "^":
                start_pos = (r, c)
                break
        if start_pos:
            break

    return grid, rows, cols, start_pos

def question_one():
    start_time = time.time()  # Start timing

    grid, rows, cols, start_pos = get_inputs()
    res = search(grid, start_pos, rows, cols)
    print(len(res))

    end_time = time.time()  # End timing
    print(f"question_one took {end_time - start_time:.6f} seconds")

def question_two():
    start_time = time.time()  # Start timing

    grid, rows, cols, start_pos = get_inputs()
    path = search(grid, start_pos, rows, cols)
    modified_grid = [list(row) for row in grid]

    count = 0
    for pos in path:
        if pos == start_pos:
            continue

        modified_grid[pos[0]][pos[1]] = '#'
        if check_cycle(modified_grid, start_pos, rows, cols):
            count += 1
        modified_grid[pos[0]][pos[1]] = "."

    print(count)

    end_time = time.time()  # End timing
    print(f"question_two took {end_time - start_time:.6f} seconds")

# Run both questions
question_one()
question_two()