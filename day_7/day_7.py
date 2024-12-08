'''
looks like its backtracking and DP similar to 

target sum
'''
import time


def is_target_sum_possible(target, nums):
    """
    Determines if it is possible to reach the target using addition and multiplication.
    Uses dynamic programming with caching.
    """
    cache = {}

    def search(index, curr_sum):
        # Base cases
        if index >= len(nums):
            return curr_sum == target

        if (index, curr_sum) in cache:
            return cache[(index, curr_sum)]

        # Option 1: Add nums[index] to curr_sum
        opt1 = search(index + 1, curr_sum + nums[index])

        # Option 2: Multiply nums[index] with curr_sum (if curr_sum > 0)
        opt2 = search(index + 1, curr_sum * nums[index] if curr_sum != 0 else nums[index])

        cache[(index, curr_sum)] = opt1 or opt2
        return cache[(index, curr_sum)]

    return search(0, 0)


def is_target_sum_possible_combine(target, nums):
    """
    Determines if it is possible to reach the target using addition, multiplication, 
    or concatenation of numbers in the list.
    Uses dynamic programming with caching.
    """
    cache = {}

    def search(index, curr_sum):
        # Base cases
        if index >= len(nums):
            return curr_sum == target

        if (index, curr_sum) in cache:
            return cache[(index, curr_sum)]

        # Option 1: Add nums[index] to curr_sum
        opt1 = search(index + 1, curr_sum + nums[index])

        # Option 2: Multiply nums[index] with curr_sum (if curr_sum > 0)
        opt2 = search(index + 1, curr_sum * nums[index] if curr_sum != 0 else nums[index])

        # Option 3: Concatenate nums[index] to curr_sum
        opt3 = search(index + 1, int(f"{curr_sum}{nums[index]}"))

        cache[(index, curr_sum)] = opt1 or opt2 or opt3
        return cache[(index, curr_sum)]

    return search(0, 0)


def parse_file():
    """
    Reads and parses the input file into targets and nums.
    Expects each line to be in the format `target: num1 num2 num3`.
    """
    with open("day_7.txt") as f:
        lines = f.read().splitlines()

    targets, nums = [], []

    for line in lines:
        target, numbers = line.strip().split(':')
        targets.append(int(target))
        nums.append(list(map(int, numbers.split())))

    return zip(targets, nums)


def question_one():
    """
    Sums all targets for which the `is_target_sum_possible` function returns True.
    """
    lines = parse_file()
    curr_sum = 0
    start_time = time.time()

    for target, nums in lines:
        if is_target_sum_possible(target, nums):
            curr_sum += target

    end_time = time.time()
    print(f"Question One Result: {curr_sum}")
    print(f"Time Taken for Question One: {end_time - start_time:.2f} seconds")


def question_two():
    """
    Sums all targets for which the `is_target_sum_possible_combine` function returns True.
    """
    lines = parse_file()
    curr_sum = 0
    start_time = time.time()

    for target, nums in lines:
        if is_target_sum_possible_combine(target, nums):
            curr_sum += target

    end_time = time.time()
    print(f"Question Two Result: {curr_sum}")
    print(f"Time Taken for Question Two: {end_time - start_time:.2f} seconds")


# Run the questions
question_one()
question_two()
