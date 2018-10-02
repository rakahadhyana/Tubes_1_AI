from generateNeigbor import generateNeighbor
from total_cost import totalCost
from print import printBoard
from init import init

def hillClimbing(states):
  current = init(states)
  printBoard(current)
  print(totalCost(current))
  print("Tentukan iterasi maksimal: ")
  max_iteration = int(input())
  print()
  isLocalMax = False
  i = 0
  iteration = 1
  while not(isLocalMax) and iteration <= max_iteration:
    print("iteration number : ", iteration)
    current_cost = totalCost(current)
    neighbors = generateNeighbor(current)
    # print(neighbors)
    first = True
    i = 1
    for neighbor in neighbors:
      # print(i)
      # printBoard(neighbor)
      neighbor_cost = totalCost(neighbor)
      if first:
        best_neighbor = neighbor
        best_neighbor_cost = neighbor_cost
        first = False
        # print(neighbor_cost)
      elif neighbor_cost['total_diff'] - neighbor_cost['total_same'] > best_neighbor_cost['total_diff'] - best_neighbor_cost['total_same']:
        # print("better")
        best_neighbor = neighbor
        best_neighbor_cost = neighbor_cost
      # else:
        # print(neighbor_cost)
        # print("not best")
      i += 1

    if best_neighbor_cost['total_diff'] - best_neighbor_cost['total_same'] < current_cost['total_diff'] - current_cost['total_same']:
      isLocalMax = True
    else:
      print("best_neighbor")
      printBoard(best_neighbor)
      print(totalCost(best_neighbor))
      print()
      print("=============================================")
      print()
      current = best_neighbor
      print("current")
      printBoard(current)
      print(totalCost(current))
      print()
    iteration += 1
  return current        
