import re

# The regex pattern to match mul(xxx, xxx) and capture the numbers
mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

def question_one():
    """Sum the product of numbers in mul(xxx, xxx) from each line."""
    cum_sum = 0
    with open("day_3.txt") as f:
        lines = f.read().split("\n")

    for line in lines:
        # Find all mul(xxx, xxx) matches and sum their products
        matches = re.findall(mul_pattern, line)
        for match in matches:
            cum_sum += int(match[0]) * int(match[1])

    print(cum_sum)


def question_two():
    """Sum the product of mul(xxx, xxx) based on 'do'/'don't' logic."""
    cum_sum = 0
    do_flag = False  # Tracks if 'do' has been encountered
    word_match_flag = False  # Tracks if 'do' or 'don't' has been encountered

    with open("day_3.txt") as f:
        lines = f.read().split("\n")

    for line in lines:
        # Regex patterns for 'do', 'don't', and 'mul(xxx, xxx)'
        do_matches = [(match.group(), match.start()) for match in re.finditer(r'do', line)]
        dont_matches = [(match.group(), match.start()) for match in re.finditer(r"don[\'’]t", line)]
        mul_matches = [(match.group(), match.start()) for match in re.finditer(mul_pattern, line)]

        # Remove 'do' matches that overlap with 'don't' matches (same index)
        do_matches = [do for do in do_matches if not any(do[1] == dont[1] for dont in dont_matches)]

        # Combine all matches into one list (do, don't, and mul) along with their indices
        all_matches = do_matches + dont_matches + mul_matches

        # Sort all matches by their starting index to maintain the order in the string
        all_matches.sort(key=lambda x: x[1])

        # Extract just the match values (without indices) for iteration
        all_matches = [string_val for string_val, _ in all_matches]

        # Iterate through the matches
        for val in all_matches:
            if val == 'do':
                do_flag = True
                word_match_flag = True
            elif val == "don't":
                do_flag = False
                word_match_flag = True
            elif val.startswith('mul'):
                if do_flag or not word_match_flag:
                    nums = re.findall(mul_pattern, val)
                    if nums:
                        a, b = map(int, nums[0])
                        cum_sum += a * b
                word_match_flag = False  # Reset after processing mul

    print("Cumulative sum:", cum_sum)


# Call the functions
question_one()
question_two()
