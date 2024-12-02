'''
we can do with monotonic stacks

we need to find the lengths of the the monotonically increasing stack and decreasing stack of each row
we then check if either of those stacks len >= len(row) - 1
set safe count += 1 hten

lets create 2 subfunctions
len_montonic_


We can further optimize by modifying longest increasing subsequnce algorithm by adding in 
requirements for valid differences between indices and also check for longest decreasing subsequences

with monotonic stack we get: 
Part 1:
time complexity: O(N*M)     (we do 2 montonic stack functions that are linear time for each M length row N times (number of rows))
space complexity: O(N*M)     we have 2 monotonic stack functions that have stack at max size M (number of rows)

Part 2:
time complexity: O(N*(M^2))     (we do 2 montonic stack functions that are linear time for each M length row N times (number of rows), and iterate over M rows M times to create splices)
space complexity: O(N*(M^2))     we have 2 monotonic stack functions that have stack at max size M (number of rows), we also create M splices of of new rows 

with LIS algo we can cut down time and space complexity for part 2
Part 1:
time complexity: O(N*M)     (we do 2 modified LIS functions that are linear time for each M length row N times (number of rows))
space complexity: O(N*M)     we have 2 LIS functions that have M size array for LIS/LDS (number of rows)

Part 2:
time complexity: O(N*(M^2))      (we do 2 modified LIS functions that are linear time for each M length row N times (number of rows)) this isnt better nvm
space complexity: O(N*(M))      we have 2 LIS functions that have M size array for LIS/LDS (number of rows) 
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


def longest_increasing_subsequence(row):
        LIS = [1] * len(row)
        valid_diffs = [1, 2, 3]

        for i in range(1, len(row)):
            for j in range(i):
                if row[i] > row[j] and abs(row[j] - row[i]) in valid_diffs:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)

def longest_decreasing_subsequence(row):
        LDS = [1] * len(row)
        valid_diffs = [1, 2, 3]

        for i in range(1, len(row)):
            for j in range(i):
                if row[i] < row[j] and abs(row[j] - row[i]) in valid_diffs:
                    LDS[i] = max(LDS[i], 1 + LDS[j])
        return max(LDS)


def question_one():
    with open("day_2.txt") as f:
        lines = f.read().split("\n")

    safe_count = 0
    valid_diffs = [1, 2, 3]

    for line in lines:
        vals = line.split()
        row = [int(val) for val in vals]
        '''
        check if its initally a monotonically increasing or decreasing valid stack
        '''
        if is_monotonic_decreasing(row) or is_monotonic_increasing(row):
            safe_count += 1

    print(safe_count)


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


def question_one_DP():
    with open("day_2.txt") as f:
        lines = f.read().split("\n")

    safe_count = 0
    valid_diffs = [1, 2, 3]

    for line in lines:
        vals = line.split()
        row = [int(val) for val in vals]
        '''
        check if its initally a monotonically increasing or decreasing valid stack
        '''
        if longest_increasing_subsequence(row) == len(row) or longest_decreasing_subsequence(row) == len(row):
            safe_count += 1

    print(safe_count)

def question_two_DP():
    with open("day_2.txt") as f:
        lines = f.read().split("\n")

    safe_count = 0
    valid_diffs = [1, 2, 3]

    for line in lines:
        vals = line.split()
        row = [int(val) for val in vals]
        '''
        check if its initally a monotonically increasing or decreasing valid stack
        '''
        if longest_increasing_subsequence(row) >= len(row) - 1 or longest_decreasing_subsequence(row) >= len(row) - 1:
            safe_count += 1

    print(safe_count)


question_one()
question_one_DP()
question_two()
question_two_DP()
