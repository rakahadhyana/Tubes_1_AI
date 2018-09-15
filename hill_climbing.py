from generateNeigbor import generateNeighbor
from total_cost import totalCost
from print import printBoard

def hillClimbing():
  current = [
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
  print("current")
  printBoard(current)
  print(totalCost(current))
  isLocalMax = False
  i = 0
  while not(isLocalMax):
    current_cost = totalCost(current)
    neighbors = generateNeighbor(current)
    # print(neighbors)
    first = True
    i = 1
    for neighbor in neighbors:
      print(i)
      printBoard(neighbor)
      neighbor_cost = totalCost(neighbor)
      if first:
        best_neighbor = neighbor
        best_neighbor_cost = neighbor_cost
        first = False
        print(neighbor_cost)
      elif neighbor_cost['total_diff'] - neighbor_cost['total_same'] > best_neighbor_cost['total_diff'] - best_neighbor_cost['total_same']:
        print("better")
        best_neighbor = neighbor
        best_neighbor_cost = neighbor_cost
      else:
        print(neighbor_cost)
        print("not best")
      i += 1
    print("best_neighbor")    
    printBoard(best_neighbor)
    print(totalCost(best_neighbor))
    if best_neighbor_cost['total_diff'] - best_neighbor_cost['total_same'] <= current_cost['total_diff'] - current_cost['total_same']:
      isLocalMax = True
    else:
      current = best_neighbor
      printBoard(current)
      print(totalCost(current))
  return current        

def main():
  hillClimbing()
  # printBoard(hillClimbing())

if __name__ == '__main__':
  main()
