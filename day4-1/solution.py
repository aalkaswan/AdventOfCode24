import re
def load(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]


def parse(lines):
    # split lines into card, winning, numbers
    for line in lines:
        card, line = line.replace("  ", " ").split(":")
        card = int(card[4:])
        winning, numbers = line.split("|")
        winning = [int(num) for num in winning.strip().split(" ")]
        numbers = [int(num) for num in numbers.strip().split(" ")]
        yield card, winning, numbers

def solve(lines):
    # find the winning cards and calc score
    res = 0
    for card, winning, numbers in parse(lines):
        winning_numbers = len([num for num in numbers if num in winning])
        if winning_numbers > 0:
            res = res + 2 ** (winning_numbers - 1)
    return res
    

# Test
test_lines = load('./day4-1/test.txt')
test_solution = solve(test_lines)
assert test_solution == 13

# Solution
lines = load('./day4-1/input.txt')
solution = solve(lines)
print(f"Solution: {solution}")