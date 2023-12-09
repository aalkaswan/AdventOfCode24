def load(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]

def parse(lines):
    # return [[func1], [func2], ...]
    return [[int(n) for n in line.split(' ')] for line in lines]

def get_next(func):
    # return next number in sequence
    if all([n == 0 for n in func]):
        return 0
    return func[-1] + get_next([func[i+1] - func[i] for i in range(len(func)-1)])

def solve(funcs):
    # return sum of all next numbers in sequence
    return sum([get_next(func) for func in funcs])

# Test
test_lines = load('./day9-1/test.txt')
funcs = parse(test_lines)
test_solution = solve(funcs)
print(test_solution)
assert test_solution == 114

# Solution
lines = load('./day9-1/input.txt')
funcs = parse(lines)
solution = solve(funcs)
print(f"Solution: {solution}")