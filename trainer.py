import mancala
import utils
import random

# Parameters:
# Weights for a move with equal likelyhood:
STORED_WEIGHTS = "trained_weights.txt"
start_weights = [10, 10, 10, 10, 10, 10]
rewards = {"win": 10, "lose": -5, "tie": 3}

history = []

BATCH_SIZE = 10
ITERATIONS = 100000


def get_move(state, weights_list):
    choices = ["a", "b", "c", "d", "e", "f"]
    if state["turn"] == "human":
        # Ensure computer picks a pit with some stones in it.
        choice = random.choices(choices, weights=start_weights, k=1)[0]
        while state["computer-pits"][utils.pit_number(choice)] == 0:
            choice = random.choices(choices, weights=start_weights, k=1)[0]
        return choice         
    else:
        choices = ["a", "b", "c", "d", "e", "f"]
        board = utils.board(state)
        if tuple(board) in weights_list:
            weights = weights_list[tuple(board)]
        else:
            weights = start_weights
        choice = random.choices(choices, weights=weights, k=1)[0]
        # Ensure computer picks a pit with some stones in it.
        while state["computer-pits"][utils.pit_number(choice)] == 0:
            choice = random.choices(choices, weights=weights, k=1)[0]
        return choice


def play_game(game_number, weights):
    """
    Plays one game of mancala and returns the dictionary of computer moves.
    """
    state = mancala.new_game()
    computer_moves = {}
    while not mancala.game_over(state, quiet=True):
        move = get_move(state, weights)
        state = mancala.do_move(state, move, computer_moves, quiet=True)
    winner = mancala.get_winner(state, quiet=True)
    history.append((game_number, winner))
    print(f"Game {game_number} winner: {winner}")
    computer_moves["winner"] = winner
    return computer_moves


def update_weights(games, weights):
    """
    Updates the weights based on the games played.
    """
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
                if weights[state][utils.pit_number(game[state])] < 1:
                    weights[state][utils.pit_number(game[state])] = 1
            elif game["winner"] == "computer":
                weights[state][utils.pit_number(game[state])] += rewards["win"]
            else:
                weights[state][utils.pit_number(game[state])] += rewards["tie"]
    return weights


game_num = 0
weights = {}
while game_num < ITERATIONS:
    games = []
    for i in range(BATCH_SIZE):
        games.append(play_game(game_num, weights))
        game_num += 1
    weights = update_weights(games, weights)
    # print(f"weights: {weights}")




count = 0
for game in history[-100:]:
    if game[1] == "computer":
        count += 1

print(f"Computer won {count} of the last 100 games.")

print(f"You have trained weights for {len(weights)} board states.")

with open(STORED_WEIGHTS, "w") as f:
    print(weights, file=f)
    print("Updated weights")


