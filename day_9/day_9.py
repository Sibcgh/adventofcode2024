def parse_file():
    """Reads the input file and parses it into a fragmented array."""
    with open("day_9.txt") as f:
        lines = f.read().splitlines()

    fragmented_arr = []
    file_id = 0
    is_block = True

    for char in lines[0]:
        block_length = int(char)
        if is_block:
            fragmented_arr.extend([file_id] * block_length)
            file_id += 1
        else:
            fragmented_arr.extend(['.'] * block_length)
        is_block = not is_block

    return fragmented_arr

def defragment_array(fragmented_arr):
    """Defragments the array by moving non-empty blocks to the left."""
    empty_block_ptr = fragmented_arr.index(".")

    while empty_block_ptr < len(fragmented_arr):
        # Remove trailing empty blocks
        while fragmented_arr and fragmented_arr[-1] == ".":
            fragmented_arr.pop()

        # Move the last non-empty block to the empty space
        fragmented_arr[empty_block_ptr] = fragmented_arr.pop()

        # Move empty block pointer to the next empty slot
        while empty_block_ptr < len(fragmented_arr) and fragmented_arr[empty_block_ptr] != ".":
            empty_block_ptr += 1

    return fragmented_arr

def calculate_checksum(fragmented_arr):
    """Calculates the checksum by multiplying index by value."""
    return sum(index * value for index, value in enumerate(fragmented_arr))

def question_one():
    """Solves question 1: defragments the array and calculates the checksum."""
    fragmented_arr = parse_file()
    defragmented_arr = defragment_array(fragmented_arr)
    checksum = calculate_checksum(defragmented_arr)
    print(checksum)

def parse_files_and_free_spaces(line):
    """Parses the file blocks and free spaces."""
    files = {}
    free_spaces = []
    position = 0
    file_id = 0

    for idx, char in enumerate(line):
        block_size = int(char)
        if idx % 2 == 0:
            if block_size == 0:
                raise ValueError("Unexpected file block of size 0.")
            files[file_id] = (position, block_size)
            file_id += 1
        else:
            if block_size != 0:
                free_spaces.append((position, block_size))
        position += block_size

    return files, free_spaces

def place_files_in_free_spaces(files, free_spaces):
    """Places the files in the available free spaces."""
    remaining_files = list(files.items())

    while remaining_files:
        file_id, (pos, size) = remaining_files.pop()
        for idx, (start, length) in enumerate(free_spaces):
            if start >= pos:
                free_spaces = free_spaces[:idx]
                break
            if size <= length:
                files[file_id] = (start, size)
                if size == length:
                    free_spaces.pop(idx)
                else:
                    free_spaces[idx] = (start + size, length - size)
                break

    return files

def calculate_final_checksum(files):
    """Calculates the checksum for the file arrangement."""
    return sum(file_id * x for file_id, (pos, size) in files.items() for x in range(pos, pos + size))

def question_two():
    """Solves question 2: Places files in free spaces and calculates the checksum."""
    with open("day_9.txt") as f:
        lines = f.read().splitlines()

    line = lines[0]
    files, free_spaces = parse_files_and_free_spaces(line)
    placed_files = place_files_in_free_spaces(files, free_spaces)
    checksum = calculate_final_checksum(placed_files)
    print(checksum)

# Run the questions
question_one()
question_two()
