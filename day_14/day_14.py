import re
import time

def get_robots(file_path):
    """
    Reads the input file and extracts robot information as tuples of integers.
    Each line in the file is parsed for integers and converted into a tuple.
    """
    with open(file_path) as f:
        lines = f.read().split("\n")
    return [tuple(map(int, re.findall(r"-?\d+", line))) for line in lines if line.strip()]

def calculate_positions(robots, width, height, factor=100):
    """
    Calculates the new positions of robots using modulo and scaling.
    Returns a list of tuples representing the final positions of robots.
    """
    return [((px + vx * factor) % width, (py + vy * factor) % height) for px, py, vx, vy in robots]

def question_one():
    """
    Reads robot data from the file, computes positions, and calculates quadrant counts.
    Returns the product of counts from all quadrants excluding the medians.
    """
    WIDTH = 101
    HEIGHT = 103
    FILE_PATH = "day_14.txt"

    # Get robots from the input file
    robots = get_robots(FILE_PATH)

    # Compute positions
    robots = calculate_positions(robots, WIDTH, HEIGHT)

    # Initialize quadrant counts
    top_left, top_right, bottom_left, bottom_right = 0, 0, 0, 0

    # Calculate medians for the grid
    VERTICAL_MEDIAN = (HEIGHT - 1) // 2
    HORIZONTAL_MEDIAN = (WIDTH - 1) // 2

    # Count robots in each quadrant
    for px, py in robots:
        if px == HORIZONTAL_MEDIAN or py == VERTICAL_MEDIAN:
            continue
        if px < HORIZONTAL_MEDIAN:
            if py < VERTICAL_MEDIAN:
                top_left += 1
            else:
                bottom_left += 1
        else:
            if py < VERTICAL_MEDIAN:
                top_right += 1
            else:
                bottom_right += 1

    # Print the product of counts
    print(top_left * top_right * bottom_left * bottom_right)


def question_two():
    """
    Finds the second when the safety factor is minimized by simulating robot movements.
    Returns the second with the minimum safety factor.
    """
    WIDTH = 101
    HEIGHT = 103
    FILE_PATH = "day_14.txt"

    # Get robots from the input file
    robots = get_robots(FILE_PATH)

    min_safety_factor = float("inf")
    best_iteration = None
    seconds = WIDTH * HEIGHT  # we have that many possible combinations

    for second in range(seconds):
        res = calculate_positions(robots, WIDTH, HEIGHT, factor=second)
        # Initialize quadrant counts
        top_left, top_right, bottom_left, bottom_right = 0, 0, 0, 0

        # Calculate medians for the grid
        VERTICAL_MEDIAN = (HEIGHT - 1) // 2
        HORIZONTAL_MEDIAN = (WIDTH - 1) // 2

        # Count robots in each quadrant
        for px, py in res:
            if px == HORIZONTAL_MEDIAN or py == VERTICAL_MEDIAN:
                continue
            if px < HORIZONTAL_MEDIAN:
                if py < VERTICAL_MEDIAN:
                    top_left += 1
                else:
                    bottom_left += 1
            else:
                if py < VERTICAL_MEDIAN:
                    top_right += 1
                else:
                    bottom_right += 1

        # Calculate safety factor
        curr_sf = (top_left * top_right * bottom_left * bottom_right)
        if curr_sf < min_safety_factor:
            min_safety_factor = curr_sf
            best_iteration = second

    return best_iteration


def calculate_positions_at_time(robots, width, height, t):
    """
    Calculates the positions of robots at time t using the velocity and modulo arithmetic.
    """
    return [((px + vx * t) % width, (py + vy * t) % height) for px, py, vx, vy in robots]

def write_grid_to_file(positions, width, height, second, file_path):
    """
    Writes the grid with robot positions marked in-place for the given second to the output file.
    Robots are marked with '#' and empty spaces are '.'.
    """
    # Create a grid initialized with empty spaces
    grid = [["." for _ in range(width)] for _ in range(height)]

    # Mark the positions of the robots on the grid
    for x, y in positions:
        grid[y][x] = "#"  # Map (x, y) to grid[y][x]

    # Write the grid and time info to the file
    with open(file_path, 'a') as out_file:
        out_file.write(f"Time: {second} seconds\n")
        for row in grid:
            out_file.write("".join(row) + "\n")


def question_two_print(input_time):
    """
    Simulates the movement of robots for the given second and writes the
    positions in-place to the output file for that second.
    """
    WIDTH = 101
    HEIGHT = 103
    FILE_PATH = "day_14.txt"
    OUTPUT_FILE = "day_14_out.txt"

    # Get robots from the input file
    robots = get_robots(FILE_PATH)

    # Ensure the output file is cleared first
    with open(OUTPUT_FILE, 'w') as out_file:
        out_file.write("Robot Movement Simulation:\n")

    # Simulate and display robot movements for the given second
    positions = calculate_positions_at_time(robots, WIDTH, HEIGHT, input_time)
    write_grid_to_file(positions, WIDTH, HEIGHT, input_time, OUTPUT_FILE)


# Run the functions
question_one()

# Get the best iteration (second) from question_two
best_time = question_two()
print(best_time)

# Use the best time to print the positions in question_two_print
question_two_print(best_time)
