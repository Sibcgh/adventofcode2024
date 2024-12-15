import re
import time

'''
Initially tried to use matrix multiplication but found that could be unstable
Shifted over to Cramer rule

 Explanation:
 Cramer's rule is used instead of matrix multiplication to solve the system of linear equations. 
 It's a more direct method for systems with two equations and two variables and simplifies the problem 
 by avoiding matrix inversion, especially in the case of solving for integer solutions.
'''

# Pattern to extract numbers from input lines
pattern = r'\d+'

def read_file(filename="day_13.txt"):
    """Reads the input file and returns the chunks."""
    with open(filename) as f:
        return f.read().strip().split("\n\n")

def parse_line(line):
    """Extracts integer values from a line using regex."""
    return list(map(int, re.findall(pattern, line)))

def solve_cramers_rule(A, B):
    """Solve the system using Cramer's rule and return x and y if valid integer solutions exist."""
    a0, a1 = A[0]
    b0, b1 = A[1]
    c0, c1 = B

    det_A = a0 * b1 - a1 * b0
    if det_A == 0:
        return None  # No solution if determinant is 0

    # Calculate Cramer's determinants for Ax and Ay
    det_Ax = c0 * b1 - c1 * b0
    det_Ay = a0 * c1 - a1 * c0

    x, y = det_Ax / det_A, det_Ay / det_A

    if x.is_integer() and y.is_integer():
        return int(x), int(y)
    return None

def solve_and_compute_cost(A, B):
    """Solves the system and computes the cost if the solution is valid."""
    res = solve_cramers_rule(A, B)
    return res[0] * 3 + res[1] if res else 0

def parse_input_and_solve(chunk, adjust_B=False):
    """Extracts the input, adjusts B if needed, and returns the calculated cost."""
    lines = [parse_line(line) for line in chunk.strip().split("\n")]
    A, B = lines[:2], lines[2]

    if adjust_B:
        B = [b + 10000000000000 for b in B]  # Adjust B by adding the large constant if required

    return solve_and_compute_cost(A, B)

def process_chunks(filename="day_13.txt", adjust_B=False):
    """Processes each chunk in the input file and calculates the total cost."""
    chunks = read_file(filename)
    return sum(parse_input_and_solve(chunk, adjust_B) for chunk in chunks)

def question1():
    """Main function to process the file and compute the total cost for the original solution."""
    start_time = time.time()
    total_cost = process_chunks()
    end_time = time.time()
    
    print(f"Total Cost: {total_cost}")
    print(f"Execution Time: {end_time - start_time:.4f} seconds")

def question2():
    """Main function to process the file and compute the total cost with the adjusted B vector."""
    start_time = time.time()
    total_cost = process_chunks(adjust_B=True)
    end_time = time.time()

    print(f"Total Cost: {total_cost}")
    print(f"Execution Time: {end_time - start_time:.4f} seconds")

# Call the main functions
question1()
question2()
