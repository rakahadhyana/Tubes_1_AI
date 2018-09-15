import sys
import copy
from print import printBoard

def generateNeighbor(state):
    neighbors = []
    curstate = list(state)
    count = 0
    for movedElmt in curstate:
        initx = movedElmt["x"]
        inity = movedElmt["y"]
        for i in range(1,9):
            for j in range(1,9):
                found = True
                for elmt in state:
                    if (i==elmt["x"] and j==elmt["y"]) or (initx==i and inity==j):
                        found = False
                if (found==True):
                    movedElmt["x"] = i
                    movedElmt["y"] = j
                    neighbors.append(copy.deepcopy(curstate))
                    # print(curstate)
                    # printBoard(curstate)
        movedElmt["x"] = initx
        movedElmt["y"] = inity
    # print(len(neighbors))

    return neighbors

#def evaluateCost(neighbors):


#    for elmt in neighbors:
def main():
  state = [
    {
      "type": "ROOK",
      "x": 2,
      "y": 3,
      "color": "WHITE"
    },
    {
      "type": "QUEEN",
      "x": 2,
      "y": 5,
      "color": "WHITE"
    },
    {
      "type": "QUEEN",
      "x": 2,
      "y": 7,
      "color": "WHITE"
    },
    {
      "type": "QUEEN",
      "x": 2,
      "y": 1,
      "color": "WHITE"
    },
    {
      "type": "BISHOP",
      "x": 6,
      "y": 3,
      "color": "BLACK"
    }
  ]
  neighbor = generateNeighbor(state)
  for x in neighbor:
    print(x)


if __name__ == '__main__':
  main()
