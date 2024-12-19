'''
looks like word break 2 but simplier?

seperate into chunks

first row will be word dict

iterate through each string in chunk 2
if we can word break is possible return true
count up all possible valid word breaks

'''
from collections import defaultdict

def patternBreak(s, designSet):
    """
    Count the number of ways to segment the string `s` using the given `wordDict`.
    """
    cache = {}

    def backtrack(i):
        if i == len(s):  # Base case: reached the end of the string
            return True

        if i in cache:  # Retrieve cached result
            return cache[i]

        for j in range(i, len(s)):
            curr_pattern = s[i: j + 1]  # Slice the substring
            if curr_pattern in designSet and backtrack(j + 1):  # If valid pattern and remainder is valid
                cache[i] = True  # Cache and return early
                return True

        cache[i] = False  # Cache result for the current index
        return False

    return backtrack(0)

def patternBreakCount(s, designSet):
    """
    Count the number of ways to segment the string `s` using the given `wordDict`.
    """
    cache = {}

    def backtrack(i):
        if i == len(s):  # Base case: reached the end of the string
            return 1

        if i in cache:  # Retrieve cached result
            return cache[i]


        curr_count = 0
        for j in range(i, len(s)):
            curr_pattern = s[i: j + 1]  # Slice the substring
            if curr_pattern in designSet:
                curr_count += backtrack(j + 1) # Check remainder of the string

        cache[i] = curr_count  # Cache result for the current index
        return cache[i]

    return backtrack(0)

def read_file(filename="day_19.txt"):
    """Reads the input file and returns the chunks."""
    with open(filename) as f:
        return f.read().strip().split("\n\n")


def question1():
    chunks = read_file()

    design_set = set(design.strip() for design in chunks[0].strip().split(','))
    possible_pattern = chunks[1].splitlines()

    count = 0

    for p in possible_pattern:
        if patternBreak(p, design_set):
            count += 1

    print(count)


def question2():
    chunks = read_file()

    design_set = set(design.strip() for design in chunks[0].strip().split(','))
    possible_pattern = chunks[1].splitlines()

    count = 0

    for p in possible_pattern:
        count += patternBreakCount(p, design_set)

    print(count)

# question1()
question2()