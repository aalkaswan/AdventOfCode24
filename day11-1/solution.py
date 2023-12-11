def load(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]

def parse(lines):
    # return points of galaxies
    # double lines if there are no galaxies
    new_lines = []
    for line in lines:
        new_lines.append([c for c in line])
        if '#' not in line:
            new_lines.append([c for c in line])
    # transpose
    new_lines = list(map(list, zip(*new_lines)))
    # double lines if there are no galaxies
    new_lines2 = []
    for line in new_lines:
        new_lines2.append(line)
        if '#' not in line:
            new_lines2.append(line)
    lines = new_lines2

    points = [(x,y) for y in range(len(lines)) for x in range(len(lines[y])) if lines[y][x] == '#' ]
    return points

def solve(points):
    # calc manhattan distance to every other point
    # return sum of all distances
    sum = 0
    for i in range(len(points)):
        for j in range(len(points)):
            sum += abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
    return int(sum/2)
    

# Test
test_lines = load('./day11-1/test.txt')
points = parse(test_lines)
test_solution = solve(points)
print(test_solution)
assert test_solution == 374

# Solution
lines = load('./day11-1/input.txt')
points = parse(lines)
solution = solve(points)
print(f"Solution: {solution}")