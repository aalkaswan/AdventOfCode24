from itertools import groupby, product

def load(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]

def parse(lines):
    # return springs and group [('springs', [g1, g2,...]), ...]
    res = []
    for line in lines:
        spring, group = line.split(' ')
        groups = [int(g) for g in group.strip().split(',')]
        res.append((spring, groups))
    return res 

# memorize solutions
cache = {}

def is_valid(spring_groups, groups):
    def inner(spring_groups, groups):
        if key in cache:
            return cache[key]
        if len(groups) == 0 and len(spring_groups) == 0:
            return 1
        if len(spring_groups) == 0 or len(groups) == 0: 
            return 0
        avaliable = spring_groups.pop(0)
        next_group = groups.pop(0)
        if avaliable == next_group:
            return is_valid(spring_groups, groups) 
        else:
            return 0 
    # return if valid
    key = (str(spring_groups), str(groups))
    if key in cache:
        return cache[key]
    else:
        res = inner(spring_groups, groups)
        cache[key] = res
        return res
    
def replace(spring):
    # return all possible replacements for spring
    # count number of ? in spring
    num = sum(1 for c in spring if c == '?')
    # generate all possible replacements
    replacements = product(['#', '.'], repeat=num)
    # replace ? with replacements
    res = []
    for replacement in replacements:
        replacement = list(replacement)
        new_spring = list(spring)
        for i, c in enumerate(spring):
            if c == '?':
                new_spring[i] = replacement.pop(0)
        res.append(''.join(new_spring))
    return res
    

def solve(input):
    res = 0 
    for spring, groups in input:
        # combinatorial replacement
        possible_springs = replace(spring)
        possible_res = 0 
        i = 0
        for replaced_spring in possible_springs:
            groups_copy = groups.copy()
            g = groupby(replaced_spring)
            spring_groups = [sum(1 for _ in group) for label, group in g if label == '#']
            possible_res += is_valid(spring_groups, groups_copy)
            i += 1
        res += possible_res
    return res
    

# Test
test_lines = load('./day12-1/test.txt')
parsed = parse(test_lines)
test_solution = solve(parsed)
print(test_solution)
assert test_solution == 21

# Solution
lines = load('./day12-1/input.txt')
parsed = parse(lines)
solution = solve(parsed)
print(f"Solution: {solution}")