import re
def load(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]


def parse(lines):
    # split lines into card, winning, numbers
    # return dict of card: wins
    cards = {}
    for line in lines:
        card, line = line.replace("  ", " ").split(":")
        card = int(card[4:])
        winning, numbers = line.split("|")
        winning = [int(num) for num in winning.strip().split(" ")]
        numbers = [int(num) for num in numbers.strip().split(" ")]
        cards[card] = len([num for num in numbers if num in winning])
    return cards

def solve(lines):
    # calc score
    res = 0
    # go over cards and add new ones
    cards = parse(lines)
    next_cards = list(cards.keys())
    while next_cards:
        card = next_cards.pop()
        res = res + 1
        wins = cards[card]
        if wins > 0:
            for i in range(card + 1, card + wins+1):
                if i in cards:
                    next_cards.append(i)
    return res



# Test
test_lines = load('./day4-2/test.txt')
test_solution = solve(test_lines)
print(test_solution)
assert test_solution == 30

# # Solution
lines = load('./day4-2/input.txt')
solution = solve(lines)
print(f"Solution: {solution}")