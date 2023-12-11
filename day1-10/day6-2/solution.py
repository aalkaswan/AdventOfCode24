# The solution really is the same as the previous one, but I'm going to copy it here for posterity 🗿:

import re
def load(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]

def parse(lines):
    # return [(time, dist) ...]
    times = [int(i) for i in lines[0].strip().split()[1:]]
    distances = [int(i) for i in lines[1].strip().split()[1:]]
    return [(time, dist) for time, dist in zip(times, distances)]

def quardratic_solve(a,b,c):
    # solve for x in ax^2 + bx + c = 0
    # return x1, x2
    d = b**2 - 4*a*c
    x1 = (-b + d**0.5) / (2*a)
    x2 = (-b - d**0.5) / (2*a)
    # return in order
    if x1 > x2:
        return x2, x1
    else:
        return x1, x2

def solve(parsed):
    total = 1
    for time, dist in parsed:
        # find the quadratic equation
        x1, x2 = quardratic_solve(1, -1*time, dist+1)
        # round x1 up and x2 down, add bit of float sauce
        x1 = int(x1 - 0.0001) + 1
        x2 = int(x2 + 0.0001)
        possible = x2 - x1 + 1
        total *= possible
    return total


# Test
test_lines = load('./day6-2/test.txt')
parsed_test = parse(test_lines)
test_solution = solve(parsed_test)
assert test_solution == 71503

# # Solution
lines = load('./day6-2/input.txt')
parsed = parse(lines)
solution = solve(parsed)
print(f"Solution: {solution}")