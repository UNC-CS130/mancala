# main file for game
import os
import utils

def get_move():
    choice = input("Which pit do you want to select? [a-f, or q to quit] ")
    if choice in ["a", "b", "c", "d", "e", "f", "q"]:
        return choice
    else:
        print("Invalid Input.  Please only enter a letter from a to f.")
        return get_move()


def show_board(state):
    # os.system("clear")
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
    print(f"It's your turn, {state['turn']}")


def swap_turn(state):
    if state["turn"] == "human":
        state["turn"] = "computer"
    else:
        state["turn"] = "human"
    return state

def steal(board, end_pit, player):
    if board[end_pit] == 1:
        if player == "human" and end_pit < 6:
            # Do something
            pass
        elif player == "computer" and 6 < endpit < 13:
            # Do something else
            pass
    print("Nice work, you stole some stones!")
    return board

def do_move(state, move):
    board = utils.board(state)
    print(board)
    pit = utils.pit_number(move)
    if state["turn"] == "computer":
        pit += 7
    stones = board[pit]
    board[pit] = 0
    while stones > 0:
        pit = (pit + 1) % 14
        board[pit] += 1
        stones -= 1
    print(board)
    state = utils.update_state(state, board)
    print(state)
    #pit is last pit that was dropped into
    if not (pit == 6 and state["turn"] == "human") and not (pit == 13 and state["turn"] == "computer"):
        state = swap_turn(state)
    return state


def game_over(state):
    # Check to see if game is over.
    return False


# initialize
state = {
    "turn": "human",
    "human-store": 0,
    "human-pits": [1, 2, 3, 3, 3, 3],
    "computer-store": 0,
    "computer-pits": [1, 2, 3, 3, 3, 3],
}

# print(state)
# board = utils.board(state)
# print(board)
# print(utils.update_state(state, board))
# input("Press enter to continue")
show_board(state)
while not game_over(state):
    move = get_move()
    if move == "q":
        break
    state = do_move(state, move)
    show_board(state)


