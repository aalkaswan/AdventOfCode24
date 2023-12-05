import re
def load(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]


digits = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6' : 6, '7': 7, '8': 8, '9': 9, 
        'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six' : 6, 'seven': 7, 'eight': 8, 'nine': 9}

def get_number(line):
    # find all the matches with the digits list
    regex = re.compile('|'.join(digits.keys()))
    matches = []
    # find all matches in the line
    # start from the beginning of the line
    # and move the start of the search window by one
    while len(line) > 0:
        match = regex.match(line)
        if match:
            matches.append(match.group())
            line = line[match.start() + 1:]
        else:
            line = line[1:]

    # convert matches to numbers
    nums = [digits[match] for match in matches]
    # merge first and last digit into one number
    return int(str(nums[0]) + str(nums[-1]))

def solve(lines):
    # get numbers from each line
    numbers = [get_number(line) for line in lines]
    # sum all numbers
    return sum(numbers)
    

# Test
test_lines = load('./day2/test.txt')
test_solution = solve(test_lines)
assert test_solution == 281

lines = load('./day2/input.txt')
solution = solve(lines)
print(solution)