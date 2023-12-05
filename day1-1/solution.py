def load(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]


def get_number(line):
    # get digits from line
    nums = [int(char) for char in line if char.isdigit()]
    # merge first and last digit into one number
    return int(str(nums[0]) + str(nums[-1]))

def solve(lines):
    # get numbers from each line
    numbers = [get_number(line) for line in lines]
    # sum all numbers
    return sum(numbers)
    

# Test
test_lines = load('./day1-1/test.txt')
test_solution = solve(test_lines)
assert test_solution == 142

lines = load('./day1-1/input.txt')
solution = solve(lines)
print(solution)