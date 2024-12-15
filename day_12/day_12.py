from collections import deque

def is_valid(x, y, cols, rows):
    """Check if the coordinates are within the grid bounds."""
    return 0 <= x < cols and 0 <= y < rows

def parse_file(filename="day_12.txt"):
    """Read the input file and return the grid."""
    with open(filename) as f:
        grid = f.read().splitlines()
    return grid

def bfs(grid, rows, cols, start_cell, value, visited):
    """
    Perform BFS to calculate the area, perimeter, and return the group of cells.
    """
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]  # 4 possible directions
    queue = deque([start_cell])
    visited.add(start_cell)

    area = 0
    perimeter = 0
    grp = set()

    while queue:
        curr_r, curr_c = queue.popleft()
        area += 1
        grp.add((curr_r, curr_c))

        for offset_r, offset_c in directions:
            next_r, next_c = curr_r + offset_r, curr_c + offset_c
            if is_valid(next_c, next_r, cols, rows) and grid[next_r][next_c] != grid[curr_r][curr_c]:
                perimeter += 1
            elif not is_valid(next_c, next_r, cols, rows):
                perimeter += 1
            elif (next_r, next_c) not in visited:
                visited.add((next_r, next_c))
                queue.append((next_r, next_c))

    return grp, area, perimeter

def calculate_perimeter(grp, grid, rows, cols):
    """Calculate the perimeter of a group."""
    perimeter = 0
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for (curr_r, curr_c) in grp:
        for offset_r, offset_c in directions:
            next_r, next_c = curr_r + offset_r, curr_c + offset_c
            if is_valid(next_c, next_r, cols, rows) and grid[next_r][next_c] != grid[curr_r][curr_c]:
                perimeter += 1
            elif not is_valid(next_c, next_r, cols, rows):
                perimeter += 1

    return perimeter

def calculate_sides(grp, grid):
    """Calculate the number of unique corner sides for a group.
    
    sides_seen: A set to track unique "corner sides." 
    Each side is represented by four parameters: 
    the start (curr_r, curr_c) of the corner and 
    the direction of the turn (offset_r, offset_c)
    """
    sides_seen = set()
    sides = 0
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # iterate over each cell in current grp
    for (curr_r, curr_c) in grp:
        # check all neigbhours of current cell
        for offset_r, offset_c in directions:
            # if neighbour not in current group we can trace around it
            if (curr_r + offset_r, curr_c + offset_c) not in grp:
                # Start tracing the corner from the current cell.
                next_r, next_c = curr_r, curr_c
                
                # While we can continue tracing the corner (check the two adjacent cells),
                # and we're still within the group, keep moving to the next cell.
                while (next_r + offset_c, next_c + offset_r) in grp and (next_r + offset_r, next_c + offset_c) not in grp:
                    next_r += offset_c  # move in 1 direction
                    next_c += offset_r  # move in perpendicular direction

                # If this corner oohasn't been seen before, mark it as seen and count it.
                if (next_r, next_c, offset_c, offset_r) not in sides_seen:
                    sides_seen.add((next_r, next_c, offset_c, offset_r))    # mark corner as seen
                    sides += 1                                              # increase side count

    return sides

def question1(grid):
    """Calculate the total cost of fencing all regions on the map."""
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    total_price = 0

    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited:
                grp, area, perimeter = bfs(grid, rows, cols, (r, c), grid[r][c], visited)
                total_price += area * perimeter

    return total_price

def question2(grid):
    """Calculate the total cost for part 2 using sides instead of perimeter."""
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    total_price_part2 = 0

    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited:
                grp, area, _ = bfs(grid, rows, cols, (r, c), grid[r][c], visited)
                area = len(grp)
                sides = calculate_sides(grp, grid)
                total_price_part2 += area * sides

    return total_price_part2

# Parse the input grid
grid = parse_file()

# Calculate the total price for part 1
total_price = question1(grid)

# Calculate the total price for part 2
total_price_part2 = question2(grid)

# Print the results
print(f"Question 1: {total_price}")
print(f"Question 2: {total_price_part2}")
