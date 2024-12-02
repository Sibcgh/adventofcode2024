'''
lets check if a row is monotonically increasing or decreasing 
make sure abs diff 1,2,3
'''

def question_one():
    with open("day_2.txt") as f:
        lines = f.read().split("\n")

    safe_count = 0
    valid_diffs = [1, 2, 3]

    for line in lines:
        vals = line.split()
        vals = [int(val) for val in vals]
        '''
        base case check first 2 vals
        '''
        curr_diff = vals[1] - vals[0]
        if curr_diff == 0 or abs(curr_diff) not in valid_diffs:
            continue

        start_increasing = True if (vals[1] - vals[0] > 0) else False
        is_valid_row = True
        '''
        if we are increasing and our abs diff between curr val and last val
        is in diff we keep iterating else we move to next line
        '''
        row_len = len(vals)
        i = 2

        while i < len(vals):
            diff = vals[i] - vals[i - 1]
            curr_indx_increasing = True if (diff > 0) else False

            if (abs(diff) not in valid_diffs) or curr_indx_increasing != start_increasing or diff == 0:
                is_valid_row = False
                break
            i += 1

        if not is_valid_row:
            continue
        else:
            safe_count += 1

    print(safe_count)


'''
we can do with monotonic stacks

we need to find the lengths of the the monotonically increasing stack and decreasing stack of each row
we then check if either of those stacks len >= len(row) - 1
set safe count += 1 hten

lets create 2 subfunctions
len_montonic_
'''

def is_monotonic_decreasing(row):
    stack = []
    valid_diffs = [1, 2, 3]

    for i in range(len(row)):
        '''
        while its monotonically decreasing and we got valid diff values when we subtract
        '''
        while stack and (row[i] >= row[stack[-1]] or abs(row[i] - row[stack[-1]]) not in valid_diffs):
            stack.pop()
        stack.append(i)

    return len(stack) == len(row)

def is_monotonic_increasing(row):
    stack = []
    valid_diffs = [1, 2, 3]

    for i in range(len(row)):
        '''
        while its monotonically increasing and we got valid diff values when we subtract
        '''
        while stack and (row[i] <= row[stack[-1]] or abs(row[i] - row[stack[-1]]) not in valid_diffs):
            stack.pop()
        stack.append(i)

    return len(stack) == len(row)

def question_two():
    with open("day_2.txt") as f:
        lines = f.read().split("\n")

    safe_count = 0

    for line in lines:
        vals = line.split()
        row = [int(val) for val in vals]
        row_len = len(row)

        '''
        check if its initally a monotonically increasing or decreasing valid stack

        lets redo part 1 with this code later
        '''
        if is_monotonic_decreasing(row) or is_monotonic_increasing(row):
            safe_count += 1
            continue

        '''
        trying to figure out how to make a linear time rather than n^2 runtime
        '''
        for i in range(row_len):
            '''
            lets remove the ith index in row and check if it makes a monotonic stack
            '''
            new_row = row[:i] + row[i+1:]
            if is_monotonic_decreasing(new_row) or is_monotonic_increasing(new_row):
                safe_count += 1
                '''
                if this is valid we dont need to check rest of array lets break
                '''
                break 

    print(safe_count)

# question_one()
question_two()

