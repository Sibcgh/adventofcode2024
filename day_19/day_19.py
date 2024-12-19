'''
looks like word break 2 but simplier?

seperate into chunks

first row will be word dict

iterate through each string in chunk 2
if we can word break is possible return true
count up all possible valid word breaks

'''
import time
from collections import defaultdict

def patternBreak(s, designSet):
    """
    Determine if the string `s` can be segmented into valid patterns from `designSet`.
    """
    cache = {}

    def backtrack(i):
        if i == len(s):
            return True
        if i in cache:
            return cache[i]
        for j in range(i, len(s)):
            curr_pattern = s[i:j + 1]
            if curr_pattern in designSet and backtrack(j + 1):
                cache[i] = True
                return True
        cache[i] = False
        return False

    return backtrack(0)


def patternBreakCount(s, designSet):
    """
    Count the number of ways to segment the string `s` using the given `designSet`.
    """
    cache = {}

    def backtrack(i):
        if i == len(s):
            return 1
        if i in cache:
            return cache[i]
        curr_count = 0
        for j in range(i, len(s)):
            curr_pattern = s[i:j + 1]
            if curr_pattern in designSet:
                curr_count += backtrack(j + 1)
        cache[i] = curr_count
        return cache[i]

    return backtrack(0)


def read_file(filename="day_19.txt"):
    """Reads the input file and returns the chunks."""
    with open(filename) as f:
        return f.read().strip().split("\n\n")


def question1():
    """
    Count the number of strings in chunk 2 that can be segmented.
    """
    chunks = read_file()
    design_set = set(design.strip() for design in chunks[0].strip().split(','))
    possible_patterns = chunks[1].splitlines()

    start_time = time.time()  # Start timer
    count = sum(1 for p in possible_patterns if patternBreak(p, design_set))
    end_time = time.time()  # End timer

    print(f"Question 1: {count}")
    print(f"Execution Time: {end_time - start_time:.6f} seconds")


def question2():
    """
    Count the total number of valid segmentations for all strings in chunk 2.
    """
    chunks = read_file()
    design_set = set(design.strip() for design in chunks[0].strip().split(','))
    possible_patterns = chunks[1].splitlines()

    start_time = time.time()  # Start timer
    count = sum(patternBreakCount(p, design_set) for p in possible_patterns)
    end_time = time.time()  # End timer

    print(f"Question 2: {count}")
    print(f"Execution Time: {end_time - start_time:.6f} seconds")


question1()
question2()