def load(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]

def parse(lines):
    # return list of 2d array of chars
    res = []
    grid = []
    for line in lines:
        if line.strip() == '':
            res.append(grid)
            grid = []
        else:
            grid.append(list(line))
    # split list after each double newline
    res.append(grid)
    return res 

def find_split(rows):
    # return index of split
    for i in range(0, len(rows)):
        max_len = min(len(rows) - (i + 1), i+1)
        up = rows[:i+1][-max_len:]
        down = rows[i+1:][:max_len]
        # limit up and down to max_len
        down.reverse()
        if up == down:
            return i + 1
    return 0


def solve(input):
    res = 0
    for grid in input:
        horizontal_split = find_split(grid)*100
        if horizontal_split == 0:
            # find vertical split
            vertical_split = find_split(list(zip(*grid)))
            res += vertical_split
        else:
            res += horizontal_split
    return res
    

# Test
test_lines = load('./day13-1/test.txt')
parsed = parse(test_lines)
test_solution = solve(parsed)
print(test_solution)
assert test_solution == 405

# Solution
lines = load('./day13-1/input.txt')
parsed = parse(lines)
solution = solve(parsed)
print(f"Solution: {solution}")