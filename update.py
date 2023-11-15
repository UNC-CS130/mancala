# This python script will update the weights for our learning model stored in 'weights.txt' based on the data in 'game_history.txt' and then erase game_history.txt

import utils

# Parameters:
# Weights for a move with equal likelyhood:
start_weights = [10, 10, 10, 10, 10, 10]
rewards = {"win": 5, "lose": -2, "tie": 1}

d = {(3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 3, 3, 0): 'e', (0, 4, 4, 4, 4, 3, 0, 3, 3, 3, 3, 0, 4, 1): 'a', (0, 0, 5, 5, 5, 4, 0, 0, 4, 4, 4, 0, 4, 1): 'd', (0, 0, 5, 5, 5, 4, 2, 0, 4, 4, 0, 0, 5, 2): 'e', (0, 0, 0, 6, 6, 5, 3, 1, 4, 4, 0, 0, 5, 2): 'a', (0, 0, 0, 0, 7, 6, 4, 1, 6, 5, 0, 0, 5, 2): 'c', (1, 0, 0, 0, 0, 7, 5, 2, 7, 1, 2, 2, 6, 3): 'f', (0, 2, 2, 1, 1, 7, 5, 2, 7, 1, 2, 2, 0, 4): 'b', (0, 4, 2, 1, 1, 7, 5, 2, 0, 2, 3, 3, 1, 5): 'c', (0, 0, 3, 2, 2, 8, 5, 2, 0, 0, 4, 4, 1, 5): 'd', (0, 0, 3, 2, 2, 8, 11, 2, 0, 0, 0, 0, 2, 6): 'f', (0, 0, 3, 2, 2, 8, 12, 2, 0, 0, 0, 0, 0, 7): 'a', (0, 0, 0, 1, 3, 9, 12, 0, 1, 0, 0, 0, 0, 10): 'd', (0, 0, 0, 0, 4, 9, 12, 0, 1, 0, 0, 0, 0, 10): 'e', (0, 0, 0, 0, 0, 10, 13, 1, 2, 0, 0, 0, 0, 10): 'f', (1, 0, 0, 0, 0, 0, 16, 2, 3, 1, 1, 0, 1, 11): 'c', 'winner': 'computer'}



# get game data
with open("game_history.txt", "r") as f:
    lines = [line.strip() for line in f]
    games = []
    for line in lines:
        if len(line) > 1:
            games.append(eval(line))


# get weights
with open("weights.txt", "r") as f:
    weights = eval(f.readlines()[-1].strip())


for game in games:
    for state in game:
        if state == "winner":
            continue
        # add state to weights if it is not there
        if state not in weights:
            weights[state] = start_weights.copy()
        # update weights based on winner
        if game["winner"] == "human":
            weights[state][utils.pit_number(game[state])] += rewards["lose"]
        elif game["winner"] == "computer":
            weights[state][utils.pit_number(game[state])] += rewards["win"]
        else:
            weights[state][utils.pit_number(game[state])] += rewards["tie"]


with open("weights.txt", "a") as f:
    print(weights, file=f)
    print("Updated weights")

with open("game_history.txt", "w") as f:
    print("Erased game history")