'''
looks like its backtracking and DP similar to 

target sum
'''
import math

def isTargetSumPossible_combine(target, nums):
    cache = {}

    def search(indx, curr_sum):
        if indx >= len(nums) and curr_sum != target:
            return False

        if indx == len(nums) and curr_sum == target:
            return True

        if (indx, curr_sum) in cache:
            return cache[(indx, curr_sum)]

        opt1 = search(indx + 1, curr_sum * nums[indx] if curr_sum != 0 else nums[indx])
        opt2 = search(indx + 1, curr_sum + nums[indx])
        '''
        fixed logic we concatenate everything from the left onto current index
        we then search then with this as option
        '''
        concat_num = int(f"{curr_sum}{nums[indx]}")
        opt3 = search(indx + 1, concat_num)

        cache[(indx, curr_sum)] = opt1 or opt2 or opt3
        return cache[(indx, curr_sum)]

    res = search(0, 0)
    return res



def isTargetSumPossible(target, nums):
    cache = {}

    def search(indx, curr_sum):
        if indx >= len(nums) and curr_sum != target:
            return False

        if indx == len(nums) and curr_sum == target:
            return True

        if (indx, curr_sum) in cache:
            return cache[(indx, curr_sum)]

        opt1 = search(indx + 1, curr_sum * nums[indx] if indx > 0 else nums[indx])
        opt2 = search(indx + 1, curr_sum + nums[indx])
        cache[(indx, curr_sum)] = opt1 or opt2
        return cache[(indx, curr_sum)]

    res = search(0, 0)
    return res

def parse_file():
    # Read the input
    with open("day_7.txt") as f:
        lines = f.read().splitlines()

        targets, nums = [], []

        for line in lines:
            first, second = line.strip().split(':')[0], line.strip().split(':')[1]
            target = int(first)
            nums_list = list(map(int, second.split()))
            targets.append(target)
            nums.append(nums_list)

        return zip(targets, nums)

def question_one():
    lines = parse_file()

    curr_sum = 0

    for target, nums in lines:
        if isTargetSumPossible(target, nums):
            curr_sum += target

    print(curr_sum)

def question_two():
    lines = parse_file()

    curr_sum = 0

    for target, nums in lines:
        if isTargetSumPossible_combine(target, nums):
            curr_sum += target

    print(curr_sum)

# question_one()
question_two()

