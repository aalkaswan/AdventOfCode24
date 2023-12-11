import re
def load(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]


def parse(lines):
    # parse lines into list of dicts 
    # format [{gamenum: [{red: n, blue: m, green: o}, ...]}, ...]
    games = []
    for line in lines:
        gamenum, line = line.split(":")
        gamenum = int(gamenum[4:])
        subgames = []
        # split line into subgames
        for subgame in line.split(";"):
            red, blue, green = 0, 0, 0
            # split line into cubes
            for color_tuple in subgame.split(","):
                number, color = color_tuple.strip().split(" ")
                if color == "red":
                    red = red + int(number)
                elif color == "blue":
                    blue = blue + int(number)
                elif color == "green":
                    green = green + int(number)
            subgames.append({"red": red, "blue": blue, "green": green})
        games.append({gamenum: subgames})
    return games

def powerset(game):
    # return the minimum number of cubes needed to make a game
    red, blue, green = 0, 0, 0
    for subgame in game:
        # replace with max
        red = max(red, subgame["red"])
        blue = max(blue, subgame["blue"])
        green = max(green, subgame["green"])
    return red * blue * green
    



def solve(games):
    # sum of all powersets
    powersets = []
    for game in games:
        powersets.append(powerset(list(game.values())[0]))
    return sum(powersets)
    

# Test
test_lines = load('./day2-2/test.txt')
test_games = parse(test_lines)
test_solution = solve(test_games)
assert test_solution == 2286

# Solution
lines = load('./day2-2/input.txt')
games = parse(lines)
solution = solve(games)
print(f"Solution: {solution}")
