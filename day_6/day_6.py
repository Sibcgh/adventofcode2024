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

from collections import defaultdict

def parse_file():
    # Read the input
    with open("day_6.txt") as f:
        grid = f.read().splitlines()

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    return grid, rows, cols

def search(grid, start_pos, rows, cols):
    directions = {
        0: (0, 1),   # Right
        1: (1, 0),   # Down
        2: (0, -1),  # Left
        3: (-1, 0)   # Up
    }

    visited = set()
    path = []
    curr_x, curr_y, curr_dir = start_pos[0], start_pos[1], 3

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    while is_valid(curr_x, curr_y):
        visited.add((curr_x, curr_y))
        path.append((curr_x, curr_y))
        offset_x, offset_y = directions[curr_dir]
        next_x, next_y = curr_x + offset_x, curr_y + offset_y

        for _ in range(4):  # Try all 4 directions
            if not is_valid(next_x, next_y):
                # If out of bounds, stop searching
                return len(visited), path

            if grid[next_x][next_y] in ['.', '^']:
                # Found a valid cell to move to
                break

            # Rotate and calculate the next position
            curr_dir = (curr_dir + 1) % 4
            offset_x, offset_y = directions[curr_dir]
            next_x, next_y = curr_x + offset_x, curr_y + offset_y
        else:
            # If no valid move is found, stop searching
            return len(visited), path

        # Move to the valid cell
        curr_x, curr_y = next_x, next_y

    return len(visited), path


def check_cycle(grid, start_pos, rows, cols):
    directions = {
        0: (0, 1),   # Right
        1: (1, 0),   # Down
        2: (0, -1),  # Left
        3: (-1, 0)   # Up
    }

    visited = set()
    curr_x, curr_y, curr_dir = start_pos[0], start_pos[1], 3

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    while is_valid(curr_x, curr_y):
        if (curr_x, curr_y, curr_dir) in visited:
            return True  # Cycle detected

        visited.add((curr_x, curr_y, curr_dir))
        offset_x, offset_y = directions[curr_dir]
        next_x, next_y = curr_x + offset_x, curr_y + offset_y

        for _ in range(4):  # Try all 4 directions
            if not is_valid(next_x, next_y):
                break  # Out of bounds, rotate

            if grid[next_x][next_y] in ['.', '^']:
                # Found a valid move
                break

            # Rotate direction and recalculate the next cell
            curr_dir = (curr_dir + 1) % 4
            offset_x, offset_y = directions[curr_dir]
            next_x, next_y = curr_x + offset_x, curr_y + offset_y
        else:
            # No valid moves found, exit
            return False

        # Move to the next valid cell
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
    grid, rows, cols, start_pos = get_inputs()
    res, _ = search(grid, start_pos, rows, cols)
    print(res)


def question_two():
    grid, rows, cols, start_pos = get_inputs()
    _, path = search(grid, start_pos, rows, cols)

    count = 0
    for pos in set(path):
        if pos == start_pos:
            continue  # Skip the starting position
        
        # Create a modified grid with the obstacle
        modified_grid = [list(row) for row in grid]
        modified_grid[pos[0]][pos[1]] = '#'

        # Check if placing the obstacle creates a cycle
        if check_cycle(modified_grid, start_pos, rows, cols):
            count += 1

    print(count)


# Run both questions
question_one()
question_two()
