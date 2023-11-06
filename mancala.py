# main file for game
import os


def get_move():
  move = input("Which pit do you want to select? [1-6]")
  if move in ["1","2","3","4","5","6"]:
    return move
  else:
    print("Invalid Input.  Please only enter a number from 1 to 6.")
    return get_move()


def board(state):
  os.system('clear')
  print("--|"+"       |"*6+"|--")
  print("  |"+"       |"*6+"   ")
  print("  |"+"=======|"*6+"   ")
  print("  |"+"       |"*6+"   ")
  print("--|"+"       |"*6+"|--")

state = ""
board(state)
get_move()
board(state)
# Need a function to show the board