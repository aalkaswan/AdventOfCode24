import re
def load(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]

def is_symbol(line, row, lines):
    # check if the char at line[row] is a symbol
    if line == -1 or row == -1: # out of bounds
        return False
    char = lines[line][row]
    return char != "." and not char.isdigit()

def find_numbers(line):
    # find all numbers in a line, return the numbers and their positions
    matches = re.finditer(r'\d+', line)
    return matches

def add_index(line, row):
    # add index if it is safe
    if line <= max_line and row <= max_row and line >= 0 and row >= 0:
        return (line, row)
    return (-1, -1)

def spaces_to_check(start, end, line):
    # return the spaces to check for a given number
    #  rows
    #l-------
    #i-+++++-
    #n-+123+-
    #e-+++++-
    #s-------
    
    indices = []

    indices.append(add_index(line, start - 1))
    indices.append(add_index(line, end + 1))
    
    for i in range(start-1, end+2):
        indices.append(add_index(line - 1, i))
        indices.append(add_index(line + 1, i))
    return indices
        


def solve(lines):
    # find all numbers in a line
    numbers = []
    for line_num, line in enumerate(lines):
        matches = find_numbers(line)
        for match in matches:
            # fix end index
            spaces = spaces_to_check(match.start(), match.end()-1, line_num)

            for space in spaces:

                if is_symbol(space[0], space[1], lines):
                    numbers.append(match.group())
                    break
    return sum([int(n) for n in numbers])
                    



# Test
test_lines = load('./day3-1/test.txt')
max_line = len(test_lines) - 1
max_row = len(test_lines[0]) - 1

test_solution = solve(test_lines)
assert test_solution == 4361

# Solution
lines = load('./day3-1/input.txt')
max_line = len(lines) - 1
max_row = len(lines[0]) - 1

solution = solve(lines)
print(f"Solution: {solution}")