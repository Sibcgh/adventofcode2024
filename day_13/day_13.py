import re
import numpy as np

# Pattern to extract numbers, excluding the signs (+ or -)
pattern = r'\d+'  # This will only capture digits, no signs

def parse_file(filename="day_13.txt"):
    """Read the input file and return the chunks."""
    with open(filename) as f:
        chunks = f.read().split("\n\n")  # Split chunks by double newlines
    return chunks

'''
TODO FIX
Will solve linear combination (to be implemented later)
'''
def solve(A, B, C):
        # Solve for x using numpy's linear algebra solver
        x = np.linalg.solve(A, b)
        return x
    except np.linalg.LinAlgError as e:
        print(f"Error solving the system: {e}")
        return None


def parse_inputs_solve(chunk):
    """Parse the chunk, extract numbers, convert to integers, and store in A, B, C."""
    
    # Split the chunk by lines to extract values for Button A, Button B, and Prize
    lines = chunk.strip().split('\n')
    
    if len(lines) != 3:
        print("Error: Expected exactly 3 lines.")
        return

    res = []

    # Extract numbers from each line and convert them to integers
    for line in lines:
        matches = re.findall(pattern, line)
        if matches:
            # Convert all matched numbers to integers
            res.append([int(num) for num in matches])  # Append the list of integers

    # Assign the lists A, B, C to the extracted numbers
    A = np.array(res[0])
    B = np.array(res[1])
    C = np.array(res[2])
    
    # Print the results
    print(A, B, C)

# Reading the input file
chunks = parse_file()

# Processing each chunk
for c in chunks:
    parse_inputs_solve(c)
