from generateNeigbor import generateNeighbor
from total_cost import totalCost
from print import printBoard
from init import init
import random as rand
from copy import deepcopy

def genetic_cross(states):
    parents = []
    heads = []
    tails = []
    k = rand.randint(1, len(states)-1)
    print("k = " + str(k))
    print()

    # parent initiation
    for x in range(4):
        current = deepcopy(init(states))
        print("PARENT " + str(x+1))
        printBoard(current)
        print(totalCost(current))
        parents.append(current)
        
    # heads initiation
    for x in range(4):
        heads.append(deepcopy(parents[x][:k]))
    
    # tail initiation
    for x in range(4):
        tails.append(deepcopy(parents[0][k:]))

    # cross
    children = [{},{},{},{}]
    children[0]['states'] = deepcopy(heads[0]+tails[1])
    children[1]['states'] = deepcopy(heads[1]+tails[0])
    children[2]['states'] = deepcopy(heads[3]+tails[2])
    children[3]['states'] = deepcopy(heads[3]+tails[2])

    return fitness_function(children)

def fitness_function(states):
    max_diff = 0
    max_same = 0
    total_pairs = len(states[0]['states'])*len(states[0]['states'])
    print(total_pairs)
    x = 0

    # input the cost of each parent
    for state in states:
        print("PARENT AFTER CROSS " + str(x+1))
        x += 1
        printBoard(state['states'])
        state_cost = totalCost(state['states'])
        state['total_diff'] = state_cost['total_diff']
        state['total_same'] = state_cost['total_same']
        print(state_cost)
        max_diff += state['total_diff']
        max_same += (total_pairs - state['total_same'])

    for state in states:
        state['fitness_value'] = state['total_diff']/max_diff + state['total_same']/max_same
        print(state['fitness_value'])
    
    max = 0
    best_state = {}

    for state in states:
        if state['fitness_value'] > max:
            max = state['fitness_value']
            best_state = state

    return best_state['states']

def genetic_algorithm(states):
    printBoard(genetic_cross(states))
