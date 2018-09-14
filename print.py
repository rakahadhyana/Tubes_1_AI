import sys

def printBoard(states):
  board = []
  for i in range(8):
    board.append(['_', '_', '_', '_', '_', '_', '_', '_'])
  for state in states:
    board[state["y"] - 1].pop(state["x"] - 1)
    if state["type"] == "QUEEN":
      if state["color"] == "WHITE":
        board[state["y"] - 1].insert(state["x"] - 1, "Q")
      else:
        board[state["y"] - 1].insert(state["x"] - 1, "q")
    elif state["type"] == "KNIGHT":
      if state["color"] == "WHITE":
        board[state["y"] - 1].insert(state["x"] - 1, "K")
      else:
        board[state["y"] - 1].insert(state["x"] - 1, "k")
    elif state["type"] == "ROOK":
      if state["color"] == "WHITE":
        board[state["y"] - 1].insert(state["x"] - 1, "R")
      else:
        board[state["y"] - 1].insert(state["x"] - 1, "r")
    else:
      if state["color"] == "WHITE":
        board[state["y"] - 1].insert(state["x"] - 1, "B")
      else:
        board[state["y"] - 1].insert(state["x"] - 1, "b")

  i = 8
  for row in reversed(board):
    sys.stdout.write(str(i)+" ")
    i -= 1
    for grid in row:
      sys.stdout.write(grid + " ")
    print()
  print("  1 2 3 4 5 6 7 8")


def main():
  states = [
      {
          "type": "QUEEN",
          "x": 5,
          "y": 5,
          "color": "WHITE"
      },
      {
          "type": "QUEEN",
          "x": 8,
          "y": 8,
          "color": "WHITE"
      },
      {
          "type": "QUEEN",
          "x": 6,
          "y": 5,
          "color": "WHITE"
      },
      {
          "type": "ROOK",
          "x": 6,
          "y": 1,
          "color": "BLACK"
      }
  ]
  printBoard(states)


if __name__ == '__main__':
  main()
