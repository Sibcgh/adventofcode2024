import os

def parse_file(filename="day_25.txt"):
    locks = []
    keys = []

    current_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(current_dir, filename)

    with open(filepath) as f:
        blocks = f.read().split("\n\n")

    for block in blocks:
        curr_grid = list(zip(*block.splitlines()))
        if curr_grid[0][0] == "#":
            locks.append([row.count('#') - 1 for row in curr_grid])
        else:
            keys.append([row.count('#') - 1 for row in curr_grid])

    res = 0
    for lock in locks:
        for key in keys:
            compatible = True
            for x, y in zip(lock, key):
                if x + y > 5:
                    compatible = False
                    break
            if compatible:
                res += 1

    print(res)

parse_file()