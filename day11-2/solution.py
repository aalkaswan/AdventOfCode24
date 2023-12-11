def load(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]

def parse(lines):
    # return points of galaxies
    # return lines and columns without galaxies
    empty_cols = []
    new_lines = []
    for i, line in enumerate(lines):
        new_lines.append([c for c in line])
        if '#' not in line:
            empty_cols.append(i)
    # transpose
    new_lines = list(map(list, zip(*new_lines)))
    empty_lines = []    
    new_lines2 = []
    for i, line in enumerate(new_lines):
        new_lines2.append(line)
        if '#' not in line:
            empty_lines.append(i)
    lines = new_lines2
    points = [(x,y) for y in range(len(lines)) for x in range(len(lines[y])) if lines[y][x] == '#' ]
    return points, empty_lines, empty_cols

def solve(points, empty_lines, empty_cols, multiplier=1):
    # calc manhattan distance to every other point
    # return sum of all distances
    sum = 0
    for i in range(len(points)):
        for j in range(len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]
            # count empty lines and columns between points
            empty = len([col for col in empty_cols if col > x1 and col < x2]) +\
            len([line for line in empty_lines if line > y1 and line < y2]) +\
            len([col for col in empty_cols if col > x2 and col < x1]) +\
            len([line for line in empty_lines if line > y2 and line < y1])
            sum += abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]) + empty*multiplier - empty
    return int(sum/2)
    

# Test
test_lines = load('./day11-2/test.txt')
points, empty_lines, empty_cols = parse(test_lines)
test_solution = solve(points, empty_lines, empty_cols, 100)
print(test_solution)
assert test_solution == 8410

# Solution
lines = load('./day11-2/input.txt')
points, empty_lines, empty_cols = parse(lines)
solution = solve(points, empty_lines, empty_cols, 1000000)
print(f"Solution: {solution}")