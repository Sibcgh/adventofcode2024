'''
originally was running with an array but then realized we can do recursive backtracking
'''
import time

def count_stones(numbers, depth):
    cache = {}

    def process_stone(number, depth):
        # Check if result is already in cache
        cache_key = (number, depth)
        if cache_key in cache:
            return cache[cache_key]

        # Base case when depth reaches 0
        if depth == 0:
            cache[cache_key] = 1
            return 1

        # If the stone is "0" or an empty string, return 1 after transforming to "1"
        if number == "0" or number == "":
            result = process_stone("1", depth - 1)
            cache[cache_key] = result
            return result

        # If the number has an odd number of digits, multiply by 2024 and recurse
        if len(number) % 2:
            result = process_stone(str(int(number) * 2024), depth - 1)
            cache[cache_key] = result
            return result

        # If the number has an even number of digits, split it and recurse on both halves
        l = len(number) // 2
        result = (
            process_stone(number[:l], depth - 1) + 
            process_stone(number[l:].lstrip("0"), depth - 1)
        )

        # Store result in cache
        cache[cache_key] = result
        return result

    # Sum the results for all numbers in the input
    return sum(process_stone(s, depth) for s in numbers)

# Example usage:
with open("day_11.txt", "r") as f:
    line = f.readline().split()

# Timer for q1 (25 iterations)
start_q1 = time.time()
q1 = count_stones(line, 25)
end_q1 = time.time()
execution_time_q1 = end_q1 - start_q1

# Timer for q2 (75 iterations)
start_q2 = time.time()
q2 = count_stones(line, 75)
end_q2 = time.time()
execution_time_q2 = end_q2 - start_q2

# Output results
print(f"q1 (25 iterations): {q1}")
print(f"q2 (75 iterations): {q2}")
print(f"Execution time for q1: {execution_time_q1:.4f} seconds")
print(f"Execution time for q2: {execution_time_q2:.4f} seconds")
