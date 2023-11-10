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