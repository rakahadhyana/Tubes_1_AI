def parse(filename):
    data = open(filename, 'r')
    lines = data.readlines()

    states = []

    print(lines)
    for line in lines:
        line = line.split()
        
        state = {}
        state['color'] = line[0]
        state['type'] = line[1]
        state['count'] = line[2]

        states.append(state)

    print(states)

parse("input.txt")