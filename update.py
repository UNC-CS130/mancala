# This python script will update the weights for our learning model stored in 'weights.txt' based on the data in 'game_history.txt' and then erase game_history.txt

import utils

# Parameters:
# Weights for a move with equal likelyhood:
start_weights = [10, 10, 10, 10, 10, 10]
rewards = {"win": 10, "lose": -3, "tie": 5}


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