# Utility functions for the mancala project

def board(state):
    """Converts a board to a list of values."""
    board = []
    board += state["human-pits"]
    board.append(state["human-store"])
    board += state["computer-pits"]
    board.append(state["computer-store"])
    return board


def update_state(state, board):
    state["human-pits"] = board[:6]
    state["human-store"] = board[6]
    state["computer-pits"] = board[7:13]
    state["computer-store"] = board[13]
    return state


def pit_number(pit):
    """Converts a letter to a number."""
    # convert "a" to 0, "b" to 1, etc.
    return ord(pit) - ord("a")

#Added a rules function to call 
def mancala_rules():
    """
    Outputs the rules to Malcala if called 
    """
    print("\nMancala Rules")
    print("Play always moves around the board in a counter-clockwise circle (to the right)")
    print("The store on your right belongs to you. That is where you keep the seeds you win.")
    print("The six pits near you are your pits.")
    print("Only use one hand to pick up and put down seeds.")
    print("Once you touch the seeds in a pit, you must move those seeds.")
    print("Only put seeds in your own store, not your opponent’s store.")
    print("\nHow to play")
    print("On a turn, a player picks up all the seeds in one pit and “sows” them to the right, placing one seed/stone in each of the pits along the way.")
    print("If you come to your store, then add a seed to your store and continue. You may end up putting seeds in your opponent’s pits along the way.")
    print("Play alternates back and forth, with opponents picking up the seeds in one of their pits and distributing them one at a time into the pits on the right, beginning in the pit immediately to the right.")
    print("The game is over when one player’s pits are completely empty. The other player takes the seeds remaining in her pits and puts those seeds in her store.")
    print("Count up the seeds. Whoever has the most seeds wins.\n")
