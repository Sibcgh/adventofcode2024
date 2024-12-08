from collections import Counter


def read_data(filename="day_1.txt"):
    """Helper function to read the file and return two sorted lists."""
    with open(filename) as f:
        lines = f.read().splitlines()
    
    arr1, arr2 = [], []
    for line in lines:
        if line.strip():  # Avoid empty lines
            num_1, num_2 = line.split()
            arr1.append(int(num_1))
            arr2.append(int(num_2))
    
    return sorted(arr1), sorted(arr2)


def question_one():
    """Calculates the sum of absolute differences between sorted arrays."""
    arr1, arr2 = read_data()
    total_sum = sum(abs(a - b) for a, b in zip(arr1, arr2))
    print(total_sum)


def question_two():
    """Calculates the weighted sum of the elements in arr1 based on their occurrences in arr2."""
    arr1, arr2 = read_data()
    
    # Count the occurrences of each number in arr2
    counter = Counter(arr2)
    
    # Compute the weighted sum
    total_sum = sum(k * counter[k] for k in arr1)
    print(total_sum)

# Run the functions
question_one()
question_two()
