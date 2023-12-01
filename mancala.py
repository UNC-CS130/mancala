# main file for game
import os
import random
import utils
import time

TRAINING = "weights.txt"


def read_weights():
    with open(TRAINING, "r") as f:
        weights = eval(f.readlines()[-1].strip())
    return weights

computer_moves = {}
WEIGHTS = read_weights()
DEFAULT_WEIGHTS = [10, 10, 10, 10, 10, 10]


def get_move(state):
    if state["turn"] == "human":
        while True:
            choice = input("Which pit do you want to select? [a-f, q to quit, or r for rules] ").lower()
            if choice in ["a", "b", "c", "d", "e", "f", "q", "r"]:
                pit_number = utils.pit_number(choice)
                if choice == "q":
                    print("You left the game.")
                    exit()
                elif choice == "r": 
                    utils.mancala_rules()
                elif state["human-pits"][pit_number] > 0: #Updated get_move to handle a "zero" pit in human pits
                    return choice
                else:
                    print("Invalid Input. The selected pit is empty. Please choose a pit with stones.")
                
            else:
                print("Invalid Input. Please only enter a letter from a to f.")
            
    else:
        choices = ["a", "b", "c", "d", "e", "f"]
        board = utils.board(state)
        if tuple(board) in WEIGHTS:
            weights = WEIGHTS[tuple(board)]
        else:
            weights = DEFAULT_WEIGHTS
        choice = random.choices(choices, weights=weights, k=1)[0]
        # Ensure computer picks a pit with some stones in it.
        while state["computer-pits"][utils.pit_number(choice)] == 0:
            choice = random.choices(choices, weights=weights, k=1)[0]
        return choice


def show_board(state):
    print("+-----+------+------+------+------+------+------+-----+")
    comp_display = f"|     |{state['computer-pits'][5]:^6}|{state['computer-pits'][4]:^6}|{state['computer-pits'][3]:^6}|{state['computer-pits'][2]:^6}|{state['computer-pits'][1]:^6}|{state['computer-pits'][0]:^6}|     |"
    print(comp_display)
    print(
        f"|{state['computer-store']:^5}|------|------|------|------|------|------|{state['human-store']:^5}|"
    )
    human_display = f"|     |{state['human-pits'][0]:^6}|{state['human-pits'][1]:^6}|{state['human-pits'][2]:^6}|{state['human-pits'][3]:^6}|{state['human-pits'][4]:^6}|{state['human-pits'][5]:^6}|     |"
    print(human_display)
    print("+-----+------+------+------+------+------+------+-----+")
    print("         a      b      c      d      e      f          ")


def swap_turn(state):
    if state["turn"] == "human":
        state["turn"] = "computer"
    else:
        state["turn"] = "human"
    return state


def steal(board, end_pit, player, quiet=False):
    if board[end_pit] == 1:
        if player == "human" and end_pit < 6:
            # Do something, say end_pit = 4, this is across from pit 8
            # 0 -> 12, 1 -> 11, 2 -> 10, 3 -> 9, 4 -> 8, 5 -> 7
            board[end_pit] = 0
            board[6] += 1
            board[6] += board[12 - end_pit]
            board[12 - end_pit] = 0
            if not quiet:
                print("Shoot! you stole some stones!")
        elif player == "computer" and 6 < end_pit < 13:
            board[end_pit] = 0
            board[13] += 1
            board[13] += board[12 - end_pit]
            board[12 - end_pit] = 0
            if not quiet:
                print("HA! I stole your stones!")
    return board


def do_move(state, move, computer_moves=computer_moves, quiet=False):
    board = utils.board(state)
    pit = utils.pit_number(move)
    if state["turn"] == "computer":
        pit += 7
        computer_moves[tuple(board)] = move
        if not quiet:
            print(f"Let's see, what should I play...")
            time.sleep(1)
            print(f"I think I'll play {move}!")
            time.sleep(1)
    else:
        if not quiet:
            os.system("clear")
            print(f"You chose {move}.")
    stones = board[pit]
    board[pit] = 0
    while stones > 0:
        pit = (pit + 1) % 14
        board[pit] += 1
        stones -= 1
    board = steal(board, pit, state["turn"], quiet=quiet)
    state = utils.update_state(state, board)
    # pit is last pit that was dropped into
    if not (pit == 6 and state["turn"] == "human") and not (
        pit == 13 and state["turn"] == "computer"
    ):
        state = swap_turn(state)
    else:
        if not quiet:
            print(f"By ending in their store, {state['turn']} gets to go again.")
            time.sleep(0.5)
    return state


def game_over(state, quiet=False):
    # Check to see if game is over.
    if (
        max(state["human-pits"]) == 0
        or max(state["computer-pits"]) == 0
        or state["human-store"] > 18
        or state["computer-store"] > 18
    ):
        return True
    if not quiet:
        print("Next up: ", state["turn"])
    return False


def get_winner(state, quiet=False):
    human_score = sum(state["human-pits"]) + state["human-store"]
    computer_score = sum(state["computer-pits"]) + state["computer-store"]
    if not quiet:
        print(f"human score is {human_score}")
        print(f"computer score is {computer_score}")
    if human_score > computer_score:
        return "human"
    elif computer_score > human_score:
        return "computer"
    else:
        return "tie"
    
def new_game():
    state = {
    "turn": "computer",
    "human-store": 0,
    "human-pits": [3, 3, 3, 3, 3, 3],
    "computer-store": 0,
    "computer-pits": [3, 3, 3, 3, 3, 3],
    }
    return state




def main():
    #SUGGESTION: Add a while loop that allows for the player to play as many times as they want instead of
    # Having to restart the entire program.



    # Initialize
    print("\nWelcome to Mancala!")
    state = new_game()

    # Check if the player wants to read the rules
    rules_input = input("If you do not know how to play please type 'rules' to read the rules. Otherwise, press Enter to start the game: ").lower()
    if rules_input == "rules":
        utils.mancala_rules()
        ready_input = input("Are you ready to start the game? (yes/no): ").lower()
        while ready_input != "yes":
            ready_input = input("Are you ready to start the game? (yes/no): ").lower()

    # Game loop
    print("\nPlayers ready! Starting Game!")
    show_board(state)
    while not game_over(state):
        move = get_move(state)
        if move == "q":
            exit()
        state = do_move(state, move)
        show_board(state)

    # Display the winner
    winner = get_winner(state)
    print(f"The winner is... {winner.upper()}")
    computer_moves["winner"] = winner


    # Save game history
    with open("game_history.txt", "a") as f:
        print(computer_moves, file=f)
  

if __name__ == "__main__":
  main()