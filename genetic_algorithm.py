from parser import init
from total_cost import totalCost
import random as rand

def genetic_cross(states):
    parents = []
    heads = []
    tails = []
    k = rand.randint(1, len(states))

    for x in range(4):
        parents.append(init(states))

    for x in range(4):
        heads.append(parents[x][:k])

    for x in range(4):
        tails.append(parents[0][k:])

    children = [heads[0]+tails[1], heads[1]+tails[0],
                heads[3]+tails[2], heads[3]+tails[2]]

    return fitness_function(children)

def fitness_function(states):
    max_diff = 0
    max_same = 0
    total_pairs = len(states)*len(states)

    for state in states:
        state['total_diff'] = totalCost(state)['total_diff']
        state['total_same'] = totalCost(state)['total_same']
        max_diff += totalCost(state)['total_diff']
        max_same += total_pairs - totalCost(state)['total_same']

    for state in states:
        state['fitness_value'] = state['total_diff']/max_diff + state['total_same']/max_same
    
    max = 0
    best_state = {}

    for state in states:
        if state['fitness_value'] > max:
            max = state['fitness_value']
            best_state = state

    return best_state

def main():
  states = [
      {
          "type": "KNIGHT",
          "x": 2,
          "y": 3,
          "color": "WHITE"
      },
      {
          "type": "QUEEN",
          "x": 4,
          "y": 4,
          "color": "BLACK"
      },
      {
          "type": "QUEEN",
          "x": 4,
          "y": 2,
          "color": "WHITE"
      },
      {
          "type": "QUEEN",
          "x": 2,
          "y": 1,
          "color": "WHITE"
      }
  ]

  genetic_cross(states)


if __name__ == '__main__':
  main()
