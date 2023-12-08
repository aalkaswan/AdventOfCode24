import re
def load(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]

def parse(lines):
    # split line into seeds and ranges
    # return [[(seed_start, seed_end), ....]], [[(source_start, dest_start, range_len), ....]]
    seedline, lines = lines[0], lines[1:]
    seeds_nums = [int(num) for num in seedline.split(':')[1].strip().split(" ")]
    # for loop take 2 elements at a time
    seeds = []
    for i in range(0, len(seeds_nums), 2):
        seeds.append((seeds_nums[i], seeds_nums[i] + seeds_nums[i+1]))
        
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
    # iteratively find overlaps
    locs =[]
    for rang in ranges:
        next_seeds = []
        while len(seeds) > 0:
            start, end = seeds.pop()
            for (source_start, dest_start, range_len) in rang:
                overlap_start = max(source_start, start)
                overlap_end = min(source_start + range_len, end)
                if overlap_start < overlap_end: # there is an overlap
                    new_start = overlap_start - source_start + dest_start
                    new_end = overlap_end - source_start + dest_start
                    next_seeds.append((new_start, new_end))
                    if overlap_start > start: # gap beginning
                        seeds.append((start, overlap_start))
                    if end > overlap_end: # gap end
                        seeds.append((overlap_end, end))
                    break
            else: # if no overlap
                next_seeds.append((start, end))
        print(next_seeds)
        seeds = next_seeds.copy()
    # find smallest location
    smallest = min(next_seeds)
    return smallest[0]


# Test
test_lines = load('./day5-2/test.txt')
seeds, ranges = parse(test_lines)
# print(seeds)
test_solution = solve(seeds, ranges)
print(test_solution)
assert test_solution == 46

# # Solution
lines = load('./day5-2/input.txt')
seeds, ranges = parse(lines)
solution = solve(seeds, ranges)
print(f"Solution: {solution}")