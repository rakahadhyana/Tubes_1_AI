from print  import printBoard
from queen  import queenEat
from rook   import rookEat
from bishop import bishopEat
from horse  import horseEat

def totalCost(state):
  total_cost_same = 0
  total_cost_diff = 0
  for bidak in state:
    if bidak["type"] == "QUEEN":
      cost = queenEat(bidak, state)
    elif bidak["type"] == "ROOK":
      cost = rookEat(bidak, state)
    elif bidak["type"] == "BISHOP":
      cost = bishopEat(bidak, state)
    elif bidak["type"] == "KNIGHT":
      cost = horseEat(bidak, state)
    # print(bidak["x"] , bidak["y"] , cost)        
    total_cost_same += cost["same"]
    total_cost_diff += cost["diff"]
  return {"total_same" : total_cost_same, "total_diff" : total_cost_diff}

def main():
  state = [
    {
      "type": "QUEEN",
      "x": 2,
      "y": 3,
      "color": "WHITE"
    },
    {
      "type": "QUEEN",
      "x": 4,
      "y": 5,
      "color": "BLACK"
    },
    {
      "type": "QUEEN",
      "x": 1,
      "y": 4,
      "color": "WHITE"
    },
    {
      "type": "QUEEN",
      "x": 1,
      "y": 2,
      "color": "WHITE"
    },
    {
      "type": "ROOK",
      "x": 6,
      "y": 3,
      "color": "BLACK"
    },
    {
      "type": "KNIGHT",
      "x": 5,
      "y": 6,
      "color": "WHITE"
    }    
  ]
  printBoard(state)
  print(totalCost(state))

if __name__ == '__main__':
  main()