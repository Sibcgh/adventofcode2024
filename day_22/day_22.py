import time
from collections import defaultdict

def parse_input(filename="day_22.txt"):
    """
    Parse the input grid from the file and generate a list of input lines for 
    each secret
    """
    with open(filename) as f:
        lines = f.read().splitlines()
        lines = list(map(int, lines))
        return lines
    

def generate_secret(line):
    line = (line << 6 ^ line) & 0xFFFFFF  # Equivalent to line * 64
    line = ((line >> 5) ^ line) & 0xFFFFFF
    line = (line << 11 ^ line) & 0xFFFFFF  # Equivalent to line * 2048
    return line


def question_one():
    start_time = time.time()
    lines = parse_input()
    res = [generate_secret_multiple_times(num, 2000) for num in lines]
    print(sum(res))
    end_time = time.time()
    print(f"Question One took {end_time - start_time:.2f} seconds")


def generate_secret_multiple_times(num, times):
    for _ in range(times):
        num = generate_secret(num)
    return num


def question_two():
    start_time = time.time()
    seq_to_total = defaultdict(int)
    lines = parse_input()

    for num in lines:
        buyer = [num % 10]
        for _ in range(2000):
            num = generate_secret(num)
            buyer.append(num % 10)
        update_seq_to_total(buyer, seq_to_total)
    
    print(max(seq_to_total.values()))
    end_time = time.time()
    print(f"Question Two took {end_time - start_time:.2f} seconds")


def update_seq_to_total(buyer, seq_to_total):
    seen = set()
    for i in range(len(buyer) - 4):
        seq = tuple(buyer[j+1] - buyer[j] for j in range(i, i+4))
        if seq not in seen:
            seen.add(seq)
            seq_to_total[seq] += buyer[i+4]


question_one()
question_two()