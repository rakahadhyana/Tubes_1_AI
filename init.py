import random

def checkEquals(coordinate,states):
    equals = False
    for state in states:
        if (coordinate['x'] == state['x'] and coordinate['y'] == state['y']) :
            equals = True
            break
    return equals

def coordinateRandom():
    coordinate = {}
    coordinate['x'] = random.randint(1,8)
    coordinate['y'] = random.randint(1,8)
    return coordinate

def init(states) :
    for state in states :
        coordinate = coordinateRandom()
        while checkEquals(coordinate,states) == True:
            coordinate = coordinateRandom()   
        state['x'] = coordinate['x']
        state['y'] = coordinate['y']
    
    return states
    


