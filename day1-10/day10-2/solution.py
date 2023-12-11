def load(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]

def parse(lines):
    # return [[inst1, inst2, ...], ...]
    return [[inst for inst in line.strip()] for line in lines]

# sets of instructions that connect to a direction 
north = "S|LJ"
south = "S|7F"
east = "S-LF"
west = "S-J7"

def count_crossings(lines, loop, point):
    # return number of crossings to the left of point
    sum = 0
    for i in range(point[1]): # iterate until point
        inst = lines[point[0]][i]
        if inst in '|JL' and (point[0], i) in loop:
            sum += 1
    return sum

def solve(insts):
    # return sum of all prev numbers in sequence
    dists = [[0 for _ in range(len(insts[0]))] for _ in range(len(insts))]
    curr = (0, 0)
    # find the location of the first S
    for i in range(len(insts)):
        for j in range(len(insts[i])):
            if insts[i][j] == 'S':
                dists[i][j] = 0
                curr = (i, j)
                insts[i][j] = 'F' # replace with F
                break
    # depth first flood fill
    stack = [curr]
    seen = set()
    while stack:
        curr = stack.pop(0)
        # if visited, skip
        if curr in seen:
            continue
        seen.add(curr)
        # try up
        if curr[0] > 0 and insts[curr[0]][curr[1]] in north and insts[curr[0]-1][curr[1]] in south:
            if (curr[0]-1, curr[1]) not in seen:
                stack.append((curr[0]-1, curr[1]))
                dists[curr[0]-1][curr[1]] = dists[curr[0]][curr[1]] + 1
        # try down
        if curr[0] < len(insts)-1 and insts[curr[0]][curr[1]] in south and insts[curr[0]+1][curr[1]] in north:
            if (curr[0]+1, curr[1]) not in seen:
                stack.append((curr[0]+1, curr[1]))
                dists[curr[0]+1][curr[1]] = dists[curr[0]][curr[1]] + 1
        # try east
        if curr[1] < len(insts[curr[0]])-1 and insts[curr[0]][curr[1]] in east and insts[curr[0]][curr[1]+1] in west:
            if (curr[0], curr[1]+1) not in seen:
                stack.append((curr[0], curr[1]+1))
                dists[curr[0]][curr[1]+1] = dists[curr[0]][curr[1]] + 1
        # try west
        if curr[1] > 0 and insts[curr[0]][curr[1]] in west and insts[curr[0]][curr[1]-1] in east:
            if (curr[0], curr[1]-1) not in seen:
                stack.append((curr[0], curr[1]-1))
                dists[curr[0]][curr[1]-1] = dists[curr[0]][curr[1]] + 1
    res = 0
    # the points inside the loop
    for i, line in enumerate(insts):
        for j, inst in enumerate(line):
            if inst == '.':
                # count crossings to the left of the point
                res += count_crossings(insts, seen, (i, j)) % 2 == 1
    return res

# Test
test_lines = load('./day10-2/test.txt')
instr = parse(test_lines)
test_solution = solve(instr)
print(test_solution)
assert test_solution == 4

# Solution
lines = load('./day10-2/input.txt')
instr = parse(lines)
solution = solve(instr)
print(f"Solution: {solution}")