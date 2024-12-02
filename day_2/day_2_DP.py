'''
with a modified LIS algo w/ DP we can solve this without a stack
Part 1:
time complexity: O(N*M)     (we do 2 modified LIS functions that are linear time for each M length row N times (number of rows))
space complexity: O(N*M)     we have 2 LIS functions that have M size array for LIS/LDS (number of rows)

Part 2:
time complexity: O(N*(M^2))      (we do 2 modified LIS functions that are linear time for each M length row N times (number of rows)) this isnt better nvm
space complexity: O(N*(M))      we have 2 LIS functions that have M size array for LIS/LDS (number of rows) 

'''
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


question_one_DP()
question_two_DP()