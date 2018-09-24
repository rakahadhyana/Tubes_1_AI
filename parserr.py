import copy

def parse(filename):
    data = open(filename, 'r')
    lines = data.readlines()

    states = []

    for line in lines:
        line = line.split()
        
        state = {}
        state['color'] = line[0]
        state['type'] = line[1]
        state['x'] = 0
        state['y'] = 0

        count = int(line[2])
        for i in range(0,count) :
            statex = copy.deepcopy(state)
            states.append(statex)
    return states
