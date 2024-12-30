import os
import time

# stores in x,y coord form
directions_dict = {
    "^": (-1,0),
    "v": (1,0),
    ">": (0,1),
    "<": (0,-1),
  }

def is_valid(grid, r, c, rows, cols):
    """Check if the coordinates are within the grid bounds."""
    return (0 <= r < rows and 0 <= c < cols) and (grid[r][c] != "#")

def parse_input(filename="day_15.txt"):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(current_dir, filename)
    with open(filepath) as f:
      chunks = f.read().strip().split("\n\n")
      
    grid = [list(line) for line in chunks[0].split("\n")]
    
    rows = len(grid)
    cols = len(grid[0])    

    starting_position = None

    for r in range(rows):
      for c in range(cols):
        if grid[r][c] == "@":
            starting_position = (r, c)
            grid[r][c] = "."
            break
      if starting_position:
        break
    
    movements = [char for char in chunks[1] if char in directions_dict]

    return grid, rows, cols, starting_position, movements
    
    
def shift_left_box(arr):
    first_dot = None
    for i, val in enumerate(arr):
      if val == ".":
        first_dot = i
        break
    if first_dot is None:
      return None
    arr[0], arr[first_dot] = arr[first_dot], arr[0]
    return arr

def get_vertical_slice(grid, col, start_row, end_row):
    return [grid[row][col] for row in range(start_row, end_row)]

def get_horizontal_slice(grid, row, start_col, end_col):
    return grid[row][start_col:end_col]

def traverse(grid, rows, cols, starting_position, movements):
    curr_r, curr_c = starting_position
    for move in movements:
      if directions_dict[move]:
        next_r = curr_r + directions_dict[move][0]
        next_c = curr_c + directions_dict[move][1]
        if is_valid(grid, next_r, next_c, rows, cols):
            if grid[next_r][next_c] == "O":
              if move == "^":   
                    indx_wall = None
                    for i in range(next_r, -1, -1):
                      if grid[i][next_c] == "#":
                        indx_wall = i
                        break
                    slice = get_vertical_slice(grid, next_c, indx_wall + 1, next_r + 1)[::-1]
                    new_slice = shift_left_box(slice)
                    if new_slice:
                      for i, val in enumerate(new_slice):
                        grid[next_r - i][next_c] = val
                    else:
                      continue
                      
              elif move == "v":
                    indx_wall = None
                    for i in range(next_r, rows):
                      if grid[i][next_c] == "#":
                        indx_wall = i
                        break
                    slice = get_vertical_slice(grid, next_c, next_r, indx_wall)
                    new_slice = shift_left_box(slice)
                    if new_slice:
                      for i, val in enumerate(new_slice):
                        grid[next_r + i][next_c] = val
                    else:
                      continue
                        
              elif move == "<":
                    indx_wall = None
                    for i in range(next_c, -1, -1):
                      if grid[next_r][i] == "#":
                        indx_wall = i
                        break
                    slice = get_horizontal_slice(grid, next_r, indx_wall + 1, next_c + 1)[::-1]
                    new_slice = shift_left_box(slice)
                    if new_slice:
                      for i, val in enumerate(new_slice):
                        grid[next_r][next_c - i] = val
                    else:
                      continue

              elif move == ">":
                    indx_wall = None
                    for i in range(next_c, cols):
                      if grid[next_r][i] == "#":
                        indx_wall = i
                        break
                    slice = get_horizontal_slice(grid, next_r, next_c, indx_wall)
                    new_slice = shift_left_box(slice)
                    if new_slice:
                      for i, val in enumerate(new_slice):
                        grid[next_r][next_c + i] = val
                    else:
                      continue

            curr_r , curr_c = next_r, next_c

    return grid

def question1():
    start_time = time.time()
    grid, rows, cols, starting_position, movements = parse_input()
    new_grid = [row[:] for row in grid]
    
    for r in grid:
        print(*r, sep=' ')
        
    print('\n\n')
    
    new_grid = traverse(new_grid, rows, cols, starting_position, movements)

    for r in new_grid:  
        print(*r, sep=' ')

    score = 0
    for r in range(rows):
      for c in range(cols):
        if new_grid[r][c] == "O":
            score += 100 * r + c
            
    print(score)
    end_time = time.time()
    print(f"Execution time: {end_time - start_time} seconds")


def question2():
    pass

question1()

# question2()