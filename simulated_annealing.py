from generateNeigbor import generateNeighbor
from total_cost import totalCost
from print import printBoard
from init import init
import random
import math

def simulated_annealing(states):
  current = init(states)
  printBoard(current)
  print("Tentukan temperatur awal: ")
  temperature = int(input())
  print("Tentukan iterasi maksimal: ")
  max_i = int(input())
  print("Tentukan derajat pengurangan: ")
  t = int(input())
  i = 0
  while (i < max_i) :
    print(i+1)
    if temperature > 0:
      temperature = temperature - t
    print(temperature) 
    neighbor = generateNeighbor(current)
    next = neighbor[random.randint(0, len(neighbor)-1)]
    next_cost = totalCost(next)
    current_cost = totalCost(current)
    delta_E = (next_cost['total_diff'] - next_cost['total_same']) - (current_cost['total_diff'] - current_cost['total_same'])
    if delta_E > 0 :
      print("BETTER")
      current = next
    else :
      if temperature > 0:
        if delta_E == 0:
          print("same")
        else:
          print("worse")
        print(delta_E)
        probability = math.exp(delta_E/temperature)
        p = random.random()
        print(probability)
        print(p)
        if p <= probability:
          print("accepted")
          current = next
    printBoard(current)
    print(totalCost(current))
    i += 1


# def main():
#   simulated_annealing()

# if __name__ == '__main__':
#   main()