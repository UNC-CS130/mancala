# main file for game
import os


def get_move():
  move = input("Which pit do you want to select? [a-e]")
  if move in ["a","b","c","d","e","f"]:
    return move
  else:
    print("Invalid Input.  Please only enter a letter from a to e.")
    return get_move()


def show_board(state):
  # os.system('clear')
  print("+-----+------+------+------+------+------+------+-----+")
  comp_display = f"|     |{state['computer-pits'][5]:^6}|{state['computer-pits'][4]:^6}|{state['computer-pits'][3]:^6}|{state['computer-pits'][2]:^6}|{state['computer-pits'][1]:^6}|{state['computer-pits'][0]:^6}|     |"
  print(comp_display)
  print(f"|{state['computer-store']:^5}|------|------|------|------|------|------|{state['human-store']:^5}|")
  human_display = f"|     |{state['human-pits'][0]:^6}|{state['human-pits'][1]:^6}|{state['human-pits'][2]:^6}|{state['human-pits'][3]:^6}|{state['human-pits'][4]:^6}|{state['human-pits'][5]:^6}|     |"
  print(human_display)
  print("+-----+------+------+------+------+------+------+-----+")
  print("          a      b      c     d       f     e          ")


def do_move(state, move):
  new_state = state.copy()
  print(new_state)
  if new_state["turn"] == "human":
    new_state["turn"] = "computer"
  else:
    new_state["turn"] = "human"
  print(new_state)
  if move == "b":
    current_pit = state["human-pits"][1]
    new_state["human-pits"][1] = 0
  print(new_state)
  return new_state



# initialize
state = {"turn":"human", "human-store":0, "human-pits":[3,3,3,3,3,3], "computer-store":0, "computer-pits":[3,3,3,3,3,3]}
show_board(state)
end = False
while not end:
  move = get_move()
  state = do_move(state, move)
  show_board(state)
  if True:
    end = True
# Need a function to show the board