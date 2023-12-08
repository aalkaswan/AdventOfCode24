def load(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]

def parse(lines):
    # return 'LR', {'AAA': ('BBB', 'CCC') ...}
    instr = lines.pop(0)
    lines.pop(0) # blank line
    directions = {}
    for line in lines:
        src, left, right = line[0:3], line[7:10], line[12:15]
        directions[src] = (left, right)
    return instr, directions


def solve(instr, directions):
    i = 0
    curr = 'AAA'
    while True:
        if curr == 'ZZZ':
            return i
        next = instr[i%len(instr)]
        if next == 'L':
            curr = directions[curr][0]
        else:
            curr = directions[curr][1]
        i += 1


# Test
test_lines = load('./day8-1/test.txt')
instr, directions = parse(test_lines)
test_solution = solve(instr, directions)
# print(test_solution)
assert test_solution == 6

# Solution
lines = load('./day8-1/input.txt')
instr, directions = parse(lines)
solution = solve(instr, directions)
print(f"Solution: {solution}")