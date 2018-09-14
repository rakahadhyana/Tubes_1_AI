from print import printBoard

# behavior of horse
def horseEat(horse, states):
    count = 0

    for state in states:
        # up-right
        if (horse['y'] + 2 == state['y']) and (horse['x'] + 1 == state['x']):
            if horse['color'] == state['color']:
                count += 1 
        # up-left
        elif (horse['y'] + 2 == state['y']) and (horse['x'] - 1 == state['x']):
            if horse['color'] == state['color']:
                count += 1
        # down-right
        elif (horse['y'] - 2 == state['y']) and (horse['x'] + 1 == state['x']):
            if horse['color'] == state['color']:
                count += 1
        # down-left
        elif (horse['y'] - 2 == state['y']) and (horse['x'] - 1 == state['x']):
            if horse['color'] == state['color']:
                count += 1
        # right-up
        elif (horse['y'] + 1 == state['y']) and (horse['x'] + 2 == state['x']):
            if horse['color'] == state['color']:
                count += 1
        # right-down
        elif (horse['y'] - 1 == state['y']) and (horse['x'] + 2 == state['x']):
            if horse['color'] == state['color']:
                count += 1
        # left-up
        elif (horse['y'] + 1 == state['y']) and (horse['x'] - 2 == state['x']):
            if horse['color'] == state['color']:
                count += 1
        # left-down
        elif (horse['y'] - 1 == state['y']) and (horse['x'] - 2 == state['x']):
            if horse['color'] == state['color']:
                count += 1
    
    return count

def main():
  states = [
      {
          "type": "HORSE",
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
  printBoard(states)
  print(horseEat(states[0], states))


if __name__ == '__main__':
  main()

