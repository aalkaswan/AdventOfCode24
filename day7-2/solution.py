import itertools
from functools import cmp_to_key

def load(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]

def parse(lines):
    # return [('hand', bid) ...']
    res = []
    for line in lines:
        hand, bid = line.split()
        res.append((hand, int(bid)))
    return res

def get_type(hand):
    # return the type of hand, as a score
    # five of a kind
    if len(set(hand)) == 1:
        return 6
    # four of a kind
    if len(set(hand)) == 2:
        for num in hand:
            if hand.count(num) == 4:
                return 5
    # full house
    if len(set(hand)) == 2:
        for num in hand:
            if hand.count(num) == 3:
                return 4
    # three of a kind
    if len(set(hand)) == 3:
        for num in hand:
            if hand.count(num) == 3:
                return 3
    # two pair
    if len(set(hand)) == 3:
        pairs = 0
        for num in set(hand):
            if hand.count(num) == 2:
                pairs += 1
        if pairs == 2:
            return 2
    # one pair
    if len(set(hand)) == 4:
        return 1
    # high card
    return 0

card_stregth = {'J': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5,'7': 6, '8': 7, '9': 8, 'T': 9, 'Q': 10, 'K': 11, 'A': 12}

def compare(hand1, hand2):
    # compare 2 hands based on their card strength
    # return 1 if hand1 is stronger, -1 if hand2 is stronger, 0 if tie

    for card1, card2 in zip(hand1, hand2):
        if card_stregth[card1] > card_stregth[card2]:
            return 1
        elif card_stregth[card1] < card_stregth[card2]:
            return -1

def joker(hand):
    # return all possible hands with jokers
    jokers = hand.count('J')
    for repl in itertools.product('23456789TQKA', repeat=jokers):
        new_hand = hand
        for card in repl:
            new_hand = new_hand.replace('J', card, 1)
        yield new_hand


def solve(parsed):
    hands = [[] for i in range(7)]
    # score hands
    for hand, bid in parsed:
        if 'J' in hand:
            # get all possible hands with jokers
            possible_hands = joker(hand)
            max_score = 0
            # find the best one 
            for h in possible_hands:
                hand_score = get_type(h)
                max_score = max(max_score, hand_score)
            hands[max_score].append((hand, bid))
        else:
            hand_score = get_type(hand)
            hands[hand_score].append((hand, bid))
    # sort hands with same score
    for hand in hands:
        if len(hand) > 1:
            hand.sort(key=cmp_to_key(lambda c1, c2: compare(c1[0],c2[0])))
    # flatten list of hands
    hands = [item for sublist in hands for item in sublist]
    res = 0
    for i, hand in enumerate(hands):
        res += (i+1) * hand[1]
    return res


# Test
test_lines = load('./day7-2/test.txt')
parsed_test = parse(test_lines)
test_solution = solve(parsed_test)

assert test_solution == 5905

# Solution
lines = load('./day7-2/input.txt')
parsed = parse(lines)
solution = solve(parsed)
print(f"Solution: {solution}")