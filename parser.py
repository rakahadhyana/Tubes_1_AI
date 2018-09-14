def parse(filename):
    data = open(filename, 'r')
    lines = data.readline()

    states = []

    for line in lines:
        line.split()
        
        state = {}
        state['color'] = line[0]
        state['type'] = line[1]
        state['count'] = line[2]

        states.append(state)

    print(states)