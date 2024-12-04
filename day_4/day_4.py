'''
kinda like an exhaustive DFS search from leetcode word search
'''
def count_occurrences(board, word):
    ROWS, COLS = len(board), len(board[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    def dfs(r, c, path_indx, direction, path):
        # If we've matched the entire word, we found an occurrence
        if path_indx == len(word):
            return 1 if len(set(path)) == len(word) else 0

        count = 0
        # Continue in the same direction
        next_r, next_c = r + direction[0], c + direction[1]

        # Check if next cell is valid for continuing the word
        if (0 <= next_r < ROWS and 0 <= next_c < COLS and 
            board[next_r][next_c] == word[path_indx]):
            # Only add if this cell hasn't been used in previous steps
            if (next_r, next_c) not in path:
                new_path = path + [(next_r, next_c)]
                count += dfs(next_r, next_c, path_indx + 1, direction, new_path)

        return count

    total_occurrences = 0
    # Try starting from each cell that matches the first letter
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == word[0]:
                # Try each direction from this starting point
                for direction in directions:
                    total_occurrences += dfs(r, c, 1, direction, [(r, c)])

    return total_occurrences


'''
simplier traversal and check if we can form MAS in each direction
'''
def count_x_mas_patterns(board):
    ROWS, COLS = len(board), len(board[0])
    x_mas_count = 0

    def check_x_mas_pattern(r, c, count):
        diagonals = [
            # Top-left to bottom-right diagonal
            [(r - 1, c - 1), (r, c), (r + 1, c + 1)],
            # Top-right to bottom-left diagonal
            [(r - 1, c + 1), (r, c), (r + 1, c - 1)]
        ]

        # Check if both diagonals form MAS
        valid_diagonals = [False, False]
        for i, diagonal in enumerate(diagonals):
            # Check if all cells are within board bounds
            is_valid = True
            if all((0 <= x < ROWS and 0 <= y < COLS) for x, y in diagonal):
                # Check forward and reverse for MAS
                cells = [board[x][y] for x, y in diagonal]
                if cells == ['M', 'A', 'S'] or cells == ['S', 'A', 'M']:
                    valid_diagonals[i] = True

        # Only count if both diagonals form MAS
        if all(valid_diagonals):
            count += 1
        return count

    # Iterate through board to find 'A's
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == 'A':
                x_mas_count = check_x_mas_pattern(r, c, x_mas_count)

    return x_mas_count

# Read the input
with open("day_4.txt") as f:
    grid = f.read().splitlines()

# Count XMAS occurrences
res = count_occurrences(grid, "XMAS")
print(res)

res = count_x_mas_patterns(grid)
print(res)