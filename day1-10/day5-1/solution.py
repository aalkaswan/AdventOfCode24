import re
def load(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]

def parse(lines):
    # split line into seeds and ranges
    # return [seed1, seed2, ..], [[(source_start, dest_start, range_len), ....]]
    seedline, lines = lines[0], lines[1:]
    seeds = [int(num) for num in seedline.split(':')[1].strip().split(" ")]
    ranges = []
    lines.pop(0)
    while lines:
        header = lines.pop(0).split(" ")[0].split("-") # we don't need this
        rang = []
        while lines:
            line = lines.pop(0)
            if line == "":
                break
            dest_start, source_start, range_len = [int(num) for num in line.split(" ")]
            rang.append((source_start, dest_start, range_len))
        ranges.append(rang)
    return seeds, ranges


def solve(seeds, ranges):
    # find the location for each seed return smallest location
    locs =[]
    for seed in seeds:
        location = seed
        for rang in ranges:
            for (source_start, dest_start, range_len) in rang:
                if location in range(source_start, source_start + range_len):
                    location = dest_start + (location - source_start)
                    break
                # location = location
        locs.append(location)
    print(locs)
    return min(locs)


# Test
test_lines = load('./day5-1/test.txt')
seeds, ranges = parse(test_lines)
test_solution = solve(seeds, ranges)
print(test_solution)
assert test_solution == 35

# # Solution
lines = load('./day5-1/input.txt')
seeds, ranges = parse(lines)
solution = solve(seeds, ranges)
print(f"Solution: {solution}")