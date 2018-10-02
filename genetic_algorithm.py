from generateNeigbor import generateNeighbor
from total_cost import totalCost
from print import printBoard
from init import checkEquals
from init import coordinateRandom
from init import init
import random as rand
from copy import deepcopy

def make_generation(states):
    parents = []
    
    # parent initiation
    for x in range(4):
        current = {}
        current['states'] = deepcopy(init(states))
        current = deepcopy(insert_cost(current))
        print("PARENT " + str(x+1))
        print_info(current['states'])
        parents.append(current)

    return parents

def print_info(state):
    printBoard(state)
    print(totalCost(state))
    print()

def insert_cost(state):
    state_cost = totalCost(state['states'])
    state['total_diff'] = state_cost['total_diff']
    state['total_same'] = state_cost['total_same']

    return state

def fitness_function(states):
    '''
       how to do it?
        find the number of non-attacking pairs of elements 
        (min = 0, max = (total element × (total element-1)))
    '''
    sum_pairs = 0
    max_pairs = len(states[0]['states'])*(len(states[0]['states'])-1)
    x = 0

    # count the total of non-attacking pairs of elements
    for state in states:
        sum_pairs += max_pairs - (state['total_diff'] + state['total_same'])

    x = 0
    # count the fitness value of each state
    for state in states:
        state['fitness_value'] = (max_pairs - (state['total_diff'] + state['total_same']))/sum_pairs
        print("FITNESS " + str(x+1))
        print(state['fitness_value'])
        x += 1

    return states

# sort states based on fitness value (big to small), remove which has the smallest value
def selection(states):
    sorted_states = deepcopy(sorted(states, key=lambda k: k['fitness_value'], reverse=True))
    sorted_states.pop()

    return sorted_states

def crossover(parents):
    k = rand.randint(1, len(parents[0]['states'])-1)
    print("k = " + str(k) + "\n")

    # cross
    children = [{},{},{},{}]
    children[0]['states'] = deepcopy(parents[0]['states'][:k]+parents[1]['states'][k:])
    children[1]['states'] = deepcopy(parents[1]['states'][:k]+parents[0]['states'][k:])
    children[2]['states'] = deepcopy(parents[1]['states'])
    children[3]['states'] = deepcopy(parents[2]['states'])

    x = 0
    for child in children:    
        print("AFTER CROSS " + str(x+1))
        child = deepcopy(insert_cost(child))
        print_info(child['states'])
        x += 1

    return children

def mutation(children):
    for states in children:
        for state in states['states']:
            coordinate = {}
            coordinate['x'] = state['x']
            coordinate['y'] = state['y']
            while checkEquals(coordinate, states['states']) == True:
                coordinate = coordinateRandom()
            state['x'] = coordinate['x']
            state['y'] = coordinate['y']

    return children

def genetic_algorithm(states):
    parents = deepcopy(make_generation(states))
    parents = deepcopy(fitness_function(parents))
    found = False
    x = 1
    iterator = 1

    while not(found):
        print("\n\nCROSS " + str(iterator))
        parents = deepcopy(selection(parents))
        children = deepcopy(crossover(parents))
        children = deepcopy(mutation(children))
        print()
        children = deepcopy(fitness_function(children))
        children = deepcopy(sorted(children, key=lambda k: k['fitness_value'], reverse=True))

        # INI NENTUIN BERENTINYA BELOM FIX
        if iterator == 100:
            found = True
        elif abs(parents[0]['fitness_value'] - children[0]['fitness_value']) < 0.001:
            x += 1
            parents = deepcopy(children)
        elif x == 7:
            found = True
        else:
            x = 1
            parents = deepcopy(children)
        print("\n=============================================\n")
        print("iteration number - " + str(iterator))
        iterator += 1
    print()
    fitness_function(parents)
    print_info(parents[0]['states'])
