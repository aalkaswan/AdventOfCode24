import math

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
    # find all nodes that end with A
    starts = [node for node in directions.keys() if node[2] == 'A']
    distances = []
    for start in starts:
        i = 0
        curr = start
        # this works because the graph is cyclic, each node has a path to a unique Z, and the path to Z is equal to the cycle length
        while True:
            if curr[2] == 'Z':
                break
            next = instr[i%len(instr)]
            if next == 'L':
                curr = directions[curr][0]
            else:
                curr = directions[curr][1]
            i += 1
        distances.append(i)
    
    # get the least common multiple of all distances
    lcm = distances[0]
    for distance in distances[1:]:
        lcm = lcm * distance // math.gcd(lcm, distance)
    return lcm

# Test
test_lines = load('./day8-2/test.txt')
instr, directions = parse(test_lines)
test_solution = solve(instr, directions)
assert test_solution == 6

# Solution
lines = load('./day8-2/input.txt')
instr, directions = parse(lines)
solution = solve(instr, directions)
print(f"Solution: {solution}")