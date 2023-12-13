from functools import cache

def load(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]

def parse(lines):
    # return springs and group [('springs', [g1, g2,...]), ...]
    res = []
    for line in lines:
        spring, group = line.split(' ')
        # repeat spring 5 times 
        spring = '?'.join([spring] * 5)
        groups = [int(g) for g in group.strip().split(',')]
        res.append((spring.strip(), groups*5))
    return res 

# much faster implementation
@cache # memoization for the win
def count_solutions(springs, groups):
    if len(springs) == 0: # if both empty, valid
        return len(groups) == 0
    if len(groups) == 0: # if no more groups but only broken or question marks
        return not '#' in springs
    
    res = 0
    if springs[0] == '?' or springs[0] == '.': # do not count next char
        res += count_solutions(springs[1:], groups)

    if springs[0] == '#' or springs[0] == '?': 
        # We can consume the next block if there are enough chars to consume if no broken blocks if the block ends or the sequence ends
        if  groups[0] <= len(springs) and '.' not in springs[:groups[0]] and (len(springs) == groups[0] or springs[groups[0]] != '#'):
            res += count_solutions(springs[groups[0] +1:], groups[1:])
    
    return res


def solve(input):
    res = 0 
    for spring, groups in input:
        res += count_solutions(spring, tuple(groups))
    return res
    

# Test
test_lines = load('./day12-2/test.txt')
parsed = parse(test_lines)
test_solution = solve(parsed)
print(test_solution)
assert test_solution == 525152

# Solution
lines = load('./day12-2/input.txt')
parsed = parse(lines)
solution = solve(parsed)
print(f"Solution: {solution}")