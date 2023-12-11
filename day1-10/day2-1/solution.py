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

def ispossible(red, green, blue, game_num, game):
    # check if each of the subgames are possible
    # return game number if possible, else return 0
    for subgame in game:
        if red < subgame["red"] or green < subgame["green"] or blue < subgame["blue"]:
            return 0
    
    return game_num



def solve(red, green, blue, games):
    # sum of all possible games
    possible_games = []
    for game in games:
        possible_games.append(ispossible(red, green, blue, list(game.keys())[0], list(game.values())[0]))
    return sum(possible_games)
    

# Test
test_lines = load('./day2/test.txt')
test_games = parse(test_lines)
test_solution = solve(12 , 13 , 14 , test_games)
assert test_solution == 8

# Solution
lines = load('./day2/input.txt')
games = parse(lines)
solution = solve(12 , 13 , 14 , games)
print(f"Solution: {solution}")
