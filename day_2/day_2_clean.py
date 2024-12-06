def is_monotonic(row, valid_diffs):
    """
    Checks if the row is either monotonically increasing or decreasing with valid differences.
    """
    # Monotonic stack check
    stack = []
    
    # Check increasing
    for i in range(len(row)):
        while stack and (row[i] <= row[stack[-1]] or abs(row[i] - row[stack[-1]]) not in valid_diffs):
            stack.pop()
        stack.append(i)

    # Check decreasing (reverse)
    stack_rev = []
    for i in range(len(row)):
        while stack_rev and (row[i] >= row[stack_rev[-1]] or abs(row[i] - row[stack_rev[-1]]) not in valid_diffs):
            stack_rev.pop()
        stack_rev.append(i)

    return len(stack) == len(row) or len(stack_rev) == len(row)


def question_one():
    with open("day_2.txt") as f:
        lines = f.read().splitlines()

    safe_count = 0
    valid_diffs = [1, 2, 3]

    for line in lines:
        row = list(map(int, line.split()))
        if is_monotonic(row, valid_diffs):
            safe_count += 1

    print(safe_count)


def question_two():
    with open("day_2.txt") as f:
        lines = f.read().splitlines()

    safe_count = 0
    valid_diffs = [1, 2, 3]

    for line in lines:
        row = list(map(int, line.split()))
        row_len = len(row)
        
        if is_monotonic(row, valid_diffs):
            safe_count += 1
            continue

        for i in range(row_len):
            new_row = row[: i] + row[i + 1:]
            if is_monotonic(new_row, valid_diffs):
                safe_count += 1
                break

    print(safe_count)


question_one()
question_two()
